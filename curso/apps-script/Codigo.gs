/**
 * Registro del Curso de contratación estatal — Gobernación de Antioquia (versión 3)
 * Google Apps Script vinculado a una hoja de cálculo de Google.
 * Desarrollado por: Alexander Gómez Avendaño.
 *
 * Hojas que crea:
 *   Inscritos  -> un renglón por persona: datos de inscripción, correo verificado y estado
 *   Registros  -> un renglón por evento (ingreso, módulo, taller, evaluación)
 *   Resumen    -> un renglón por persona (último estado y mejor resultado)
 *
 * Inscripción: la página pide un código (accion=registro); el script lo envía por correo con un mensaje
 * de bienvenida. La persona lo escribe en la página (accion=confirmar) y recibe un token de sesión que
 * acompaña todos sus eventos. Una cédula queda ligada al primer correo verificado: si alguien intenta
 * ingresar con otra dirección, el código se envía al correo ya registrado.
 *
 * Instalación: ver INSTALACION.md. Ejecute configurar() y generarClaveCoordinador() una vez.
 */

var HOJA_INS = 'Inscritos';
var HOJA_REG = 'Registros';
var HOJA_RES = 'Resumen';
var COLS_INS = ['cedula', 'nombre', 'correo', 'dependencia', 'vinculacion', 'estado', 'inscripcion',
  'verificacion', 'ultimo_ingreso', 'ingresos', 'token'];
var COLS_REG = ['recibido', 'tipo', 'cedula', 'nombre', 'dependencia', 'vinculacion', 'modulo',
  'modulos', 'practica', 'casos', 'final', 'indice', 'nivel', 'areas', 'intentos', 'intento',
  'aciertos', 'duracion_min', 'codigo', 'version', 'fecha_cliente', 'correo'];
var COLS_RES = ['cedula', 'nombre', 'dependencia', 'vinculacion', 'modulos', 'practica', 'casos',
  'final', 'indice', 'nivel', 'intentos', 'codigo', 'primer_registro', 'ultimo', 'correo'];
var TIPOS = ['ingreso', 'modulo', 'taller', 'evaluacion'];
var NIVELES = ['Avanzado', 'Competente', 'En desarrollo', 'Inicial'];
var URL_CURSO = 'https://alexandergomezsif.github.io/skills_Sector_publico_antioquia/curso/';
var NOMBRE_REMITENTE = 'Curso de contratación estatal';
var MIN_CODIGO = 15;          // vigencia del código, en minutos
var MAX_CODIGOS_HORA = 5;     // solicitudes de código por cédula por hora
var MAX_INTENTOS_CODIGO = 5;  // intentos para escribir un código

function configurar() {
  var ss = SpreadsheetApp.getActive();
  [[HOJA_INS, COLS_INS], [HOJA_REG, COLS_REG], [HOJA_RES, COLS_RES]].forEach(function (h) {
    var sh = ss.getSheetByName(h[0]) || ss.insertSheet(h[0]);
    sh.getRange(1, 1, 1, h[1].length).setValues([h[1]]).setFontWeight('bold');
    sh.setFrozenRows(1);
  });
  [[HOJA_INS, 'A:A'], [HOJA_REG, 'C:C'], [HOJA_RES, 'A:A']].forEach(function (x) {
    ss.getSheetByName(x[0]).getRange(x[1]).setNumberFormat('@'); // cédula como texto
  });
  var ins = ss.getSheetByName(HOJA_INS);
  ins.hideColumns(COLS_INS.indexOf('token') + 1);
  ss.setActiveSheet(ins);
  ss.moveActiveSheet(1);
}

/** Recibe peticiones de la página del curso (POST, cuerpo JSON en texto plano). */
function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    var d = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    if (d.accion === 'registro') return json(registro(d));
    if (d.accion === 'confirmar') return json(confirmar(d));
    var ev = limpiar(d);
    if (!ev) return json({ ok: false, error: 'datos inválidos' });
    var ss = SpreadsheetApp.getActive();
    var ins = buscarInscrito(ss, ev.cedula);
    if (!ins || ins.fila.estado !== 'verificado' || !d.token || String(d.token) !== String(ins.fila.token)) {
      return json({ ok: false, error: 'sesión no verificada' });
    }
    ev.correo = ins.fila.correo;
    ss.getSheetByName(HOJA_REG).appendRow(COLS_REG.map(function (c) { return c === 'recibido' ? new Date() : ev[c]; }));
    actualizarResumen(ss.getSheetByName(HOJA_RES), ev);
    if (ev.tipo === 'ingreso') {
      var sh = ss.getSheetByName(HOJA_INS);
      sh.getRange(ins.n, COLS_INS.indexOf('ultimo_ingreso') + 1).setValue(new Date());
      sh.getRange(ins.n, COLS_INS.indexOf('ingresos') + 1).setValue((Number(ins.fila.ingresos) || 0) + 1);
    }
    return json({ ok: true });
  } catch (err) {
    return json({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

/* ---------------- inscripción y verificación por correo ---------------- */

function registro(d) {
  var p = perfilLimpio(d);
  if (!p) return { ok: false, error: 'Revise la cédula, el nombre y el correo.' };
  var cache = CacheService.getScriptCache();
  var lim = Number(cache.get('lim_' + p.cedula) || 0);
  if (lim >= MAX_CODIGOS_HORA) return { ok: false, error: 'Ya pidió varios códigos. Espere una hora e intente de nuevo.' };
  if (MailApp.getRemainingDailyQuota() < 1) return { ok: false, error: 'El servicio de correo llegó a su límite diario. Intente mañana.' };

  var ss = SpreadsheetApp.getActive();
  var sh = ss.getSheetByName(HOJA_INS);
  var ins = buscarInscrito(ss, p.cedula);
  var destino = p.correo;
  var nuevo = !ins;
  if (ins && ins.fila.estado === 'verificado' && ins.fila.correo && ins.fila.correo !== p.correo) {
    destino = ins.fila.correo; // la cédula ya tiene un correo verificado: el código va a ese correo
  }
  var ahora = new Date();
  if (!ins) {
    sh.appendRow(COLS_INS.map(function (c) {
      return { cedula: p.cedula, nombre: p.nombre, correo: p.correo, dependencia: p.dependencia,
        vinculacion: p.vinculacion, estado: 'pendiente', inscripcion: ahora, ingresos: 0 }[c] || '';
    }));
  } else if (ins.fila.estado !== 'verificado') {
    ['nombre', 'correo', 'dependencia', 'vinculacion'].forEach(function (c) {
      sh.getRange(ins.n, COLS_INS.indexOf(c) + 1).setValue(p[c]);
    });
  }
  var codigo = String(Math.floor(100000 + Math.random() * 900000));
  cache.put('cod_' + p.cedula, JSON.stringify({ h: huella(codigo, destino), n: 0, correo: destino,
    perfil: p }), MIN_CODIGO * 60);
  cache.put('lim_' + p.cedula, String(lim + 1), 3600);
  enviarCorreo(destino, p.nombre, codigo, nuevo || !ins || ins.fila.estado !== 'verificado');
  return { ok: true, enviado_a: enmascarar(destino), otro: destino !== p.correo };
}

function confirmar(d) {
  var ced = String(d.cedula || '').replace(/\D/g, '');
  var cod = String(d.codigo || '').replace(/\D/g, '');
  if (!/^\d{5,10}$/.test(ced) || !/^\d{6}$/.test(cod)) return { ok: false, error: 'Código inválido.' };
  var cache = CacheService.getScriptCache();
  var raw = cache.get('cod_' + ced);
  if (!raw) return { ok: false, error: 'El código venció o no existe. Pida uno nuevo.' };
  var c = JSON.parse(raw);
  if (c.n >= MAX_INTENTOS_CODIGO) { cache.remove('cod_' + ced); return { ok: false, error: 'Demasiados intentos. Pida un código nuevo.' }; }
  if (huella(cod, c.correo) !== c.h) {
    c.n++; cache.put('cod_' + ced, JSON.stringify(c), MIN_CODIGO * 60);
    return { ok: false, error: 'El código no coincide. Le quedan ' + (MAX_INTENTOS_CODIGO - c.n) + ' intento(s).' };
  }
  cache.remove('cod_' + ced);
  var ss = SpreadsheetApp.getActive();
  var sh = ss.getSheetByName(HOJA_INS);
  var ins = buscarInscrito(ss, ced);
  var token = Utilities.getUuid();
  var ahora = new Date();
  var set = function (col, v) { sh.getRange(ins.n, COLS_INS.indexOf(col) + 1).setValue(v); };
  if (ins.fila.estado !== 'verificado') { set('correo', c.correo); set('verificacion', ahora); set('estado', 'verificado'); }
  ['nombre', 'dependencia', 'vinculacion'].forEach(function (k) { if (c.perfil[k]) set(k, c.perfil[k]); });
  set('token', token);
  return { ok: true, token: token, correo: enmascarar(c.correo) };
}

function enviarCorreo(destino, nombre, codigo, bienvenida) {
  var pila = String(nombre).split(' ')[0];
  var asunto = (bienvenida ? 'Bienvenido(a) al Curso de contratación estatal' : 'Código de ingreso al Curso de contratación estatal') + ' — código ' + codigo;
  var html =
    '<div style="font-family:Arial,sans-serif;max-width:560px;color:#1c2723">' +
    '<div style="background:#0b5640;color:#fff;padding:18px 22px;border-radius:10px 10px 0 0">' +
    '<div style="font-size:13px;opacity:.85">Gobernación de Antioquia · formación interna</div>' +
    '<div style="font-size:20px;font-weight:bold;margin-top:4px">Curso de contratación estatal desde cero</div></div>' +
    '<div style="border:1px solid #d5ded9;border-top:0;padding:20px 22px;border-radius:0 0 10px 10px">' +
    '<p>Hola, ' + escapar(pila) + ':</p>' +
    (bienvenida
      ? '<p>Le damos la bienvenida al curso. Recorrerá la vida de un contrato público en 15 módulos, resolverá un taller de casos de la Gobernación y presentará una evaluación final. Cada módulo se habilita al aprobar el anterior.</p>'
      : '<p>Recibimos una solicitud para ingresar al curso con su cédula.</p>') +
    '<p>Su código de verificación es:</p>' +
    '<p style="font-size:30px;font-weight:bold;letter-spacing:6px;color:#0b5640;margin:6px 0">' + codigo + '</p>' +
    '<p style="font-size:13px;color:#5b6b64">Vence en ' + MIN_CODIGO + ' minutos. Si usted no lo pidió, ignore este mensaje.</p>' +
    '<p><a href="' + URL_CURSO + '" style="display:inline-block;background:#018d38;color:#fff;text-decoration:none;padding:10px 18px;border-radius:8px;font-weight:bold">Ir al curso</a></p>' +
    '<p style="font-size:12px;color:#5b6b64;border-top:1px solid #d5ded9;padding-top:10px;margin-top:18px">Sus datos se tratan conforme a la Ley 1581 de 2012, solo para registrar su avance en el curso. Desarrollado por: Alexander Gómez Avendaño.</p>' +
    '</div></div>';
  var texto = 'Hola, ' + pila + '.\n\nSu código de verificación para el Curso de contratación estatal es: ' + codigo +
    '\nVence en ' + MIN_CODIGO + ' minutos.\n\nCurso: ' + URL_CURSO + '\n\nSi usted no lo pidió, ignore este mensaje.';
  MailApp.sendEmail({ to: destino, subject: asunto, body: texto, htmlBody: html, name: NOMBRE_REMITENTE });
}

/* ---------------- panel y verificación de constancias ---------------- */

function doGet(e) {
  var p = (e && e.parameter) || {};
  if (p.accion === 'verificar') return verificar(String(p.codigo || ''));
  var clave = PropertiesService.getScriptProperties().getProperty('CLAVE_COORDINADOR');
  if (!clave || p.clave !== clave) return json({ ok: false, error: 'clave inválida' });
  if (p.accion === 'resumen') {
    var ss = SpreadsheetApp.getActive();
    var res = tabla(ss.getSheetByName(HOJA_RES));
    var porCed = {};
    res.forEach(function (r) { porCed[String(r.cedula)] = r; });
    var filas = tabla(ss.getSheetByName(HOJA_INS)).map(function (i) {
      var r = porCed[String(i.cedula)] || {};
      return { cedula: i.cedula, nombre: i.nombre, correo: i.correo, dependencia: i.dependencia,
        vinculacion: i.vinculacion, estado: i.estado, inscripcion: i.inscripcion,
        modulos: r.modulos || 0, practica: r.practica || 0, casos: r.casos || 0, final: r.final || 0,
        indice: r.indice || 0, nivel: r.nivel || '', intentos: r.intentos || 0, codigo: r.codigo || '',
        ultimo: r.ultimo || i.ultimo_ingreso || '' };
    });
    return json({ ok: true, filas: filas });
  }
  return json({ ok: false, error: 'acción desconocida' });
}

function verificar(codigo) {
  if (!/^[0-9A-Z]{4,10}$/.test(codigo)) return json({ ok: false, error: 'código inválido' });
  var filas = tabla(SpreadsheetApp.getActive().getSheetByName(HOJA_RES));
  for (var i = 0; i < filas.length; i++) {
    if (String(filas[i].codigo) === codigo) {
      return json({ ok: true, valido: true, nivel: filas[i].nivel, indice: filas[i].indice,
        cedula_final: String(filas[i].cedula).slice(-4) });
    }
  }
  return json({ ok: true, valido: false });
}

/* ---------------- utilidades ---------------- */

function tabla(sh) {
  var v = sh.getDataRange().getValues();
  var cab = v.shift();
  return v.filter(function (r) { return String(r[0]) !== ''; }).map(function (r) {
    var o = {};
    cab.forEach(function (c, i) {
      if (c === 'token') return;
      o[c] = r[i] instanceof Date ? Utilities.formatDate(r[i], 'America/Bogota', 'yyyy-MM-dd HH:mm') : r[i];
    });
    return o;
  });
}

function buscarInscrito(ss, ced) {
  var sh = ss.getSheetByName(HOJA_INS);
  var v = sh.getDataRange().getValues();
  var cab = v[0];
  for (var i = 1; i < v.length; i++) {
    if (String(v[i][0]) === String(ced)) {
      var o = {};
      cab.forEach(function (c, k) { o[c] = v[i][k]; });
      return { n: i + 1, fila: o };
    }
  }
  return null;
}

function perfilLimpio(d) {
  var ced = String(d.cedula || '').replace(/\D/g, '');
  var correo = String(d.correo || '').trim().toLowerCase();
  if (!/^\d{5,10}$/.test(ced)) return null;
  if (!/^[^\s@<>"']{1,64}@[^\s@<>"']{1,190}\.[a-z]{2,}$/.test(correo)) return null;
  var p = { cedula: ced, correo: correo, nombre: txt(d.nombre), dependencia: txt(d.dependencia),
    vinculacion: txt(d.vinculacion, 40) };
  if (p.nombre.length < 5) return null;
  return p;
}

function txt(x, n) { return String(x == null ? '' : x).replace(/[\r\n\t]+/g, ' ').replace(/^[=+\-@]+/, '').slice(0, n || 120); }

function limpiar(d) {
  var ced = String(d.cedula || '').replace(/\D/g, '');
  if (!/^\d{5,10}$/.test(ced)) return null;
  if (TIPOS.indexOf(d.tipo) < 0) return null;
  var nro = function (x, max) { var n = Number(x); return isFinite(n) && n >= 0 && n <= max ? Math.round(n * 10) / 10 : ''; };
  return {
    tipo: d.tipo, cedula: ced, nombre: txt(d.nombre), dependencia: txt(d.dependencia),
    vinculacion: txt(d.vinculacion, 40), modulo: txt(d.modulo, 10), modulos: nro(d.modulos, 60),
    practica: nro(d.practica, 100), casos: nro(d.casos, 100), final: nro(d.final, 100),
    indice: nro(d.indice, 100), nivel: NIVELES.indexOf(d.nivel) >= 0 ? d.nivel : '',
    areas: txt(d.areas, 200), intentos: nro(d.intentos, 999), intento: nro(d.intento, 999),
    aciertos: nro(d.aciertos, 40), duracion_min: nro(d.duracion_min, 1440),
    codigo: txt(d.codigo, 12), version: txt(d.version, 30), fecha_cliente: txt(d.fecha_cliente, 40), correo: ''
  };
}

function actualizarResumen(sh, ev) {
  var v = sh.getDataRange().getValues();
  var fila = -1;
  for (var i = 1; i < v.length; i++) if (String(v[i][0]) === ev.cedula) { fila = i + 1; break; }
  var ahora = new Date();
  // Conserva el mejor estado: si llega un índice menor (p. ej. desde otro navegador sin avance),
  // solo se actualizan los datos de identificación y la fecha del último registro.
  if (fila > 0) {
    var viejo = Number(v[fila - 1][COLS_RES.indexOf('indice')]) || 0;
    var modViejo = Number(v[fila - 1][COLS_RES.indexOf('modulos')]) || 0;
    if ((Number(ev.indice) || 0) < viejo || ((Number(ev.indice) || 0) === viejo && (Number(ev.modulos) || 0) < modViejo)) {
      ['nombre', 'dependencia', 'vinculacion', 'correo'].forEach(function (c) {
        sh.getRange(fila, COLS_RES.indexOf(c) + 1).setValue(ev[c]);
      });
      sh.getRange(fila, COLS_RES.indexOf('ultimo') + 1).setValue(ahora);
      return;
    }
  }
  var r = COLS_RES.map(function (c) {
    if (c === 'primer_registro') return fila > 0 ? v[fila - 1][COLS_RES.indexOf(c)] : ahora;
    if (c === 'ultimo') return ahora;
    return ev[c];
  });
  if (fila > 0) sh.getRange(fila, 1, 1, r.length).setValues([r]);
  else sh.appendRow(r);
}

function huella(codigo, correo) {
  var b = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, codigo + '|' + correo + '|curso-ce');
  return Utilities.base64Encode(b);
}
function enmascarar(c) { var p = String(c).split('@'); return p[0].slice(0, 2) + '•••@' + p[1]; }
function escapar(s) { return String(s).replace(/[&<>"']/g, function (x) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[x]; }); }
function json(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

/** Genera una clave de coordinación aleatoria si aún no existe. No la muestra en el registro:
 *  consúltela en Configuración del proyecto > Propiedades del script > CLAVE_COORDINADOR. */
function generarClaveCoordinador() {
  var props = PropertiesService.getScriptProperties();
  if (props.getProperty('CLAVE_COORDINADOR')) { Logger.log('Ya existe una clave; no se cambió.'); return; }
  var clave = Utilities.getUuid().replace(/-/g, '').slice(0, 20);
  props.setProperty('CLAVE_COORDINADOR', clave);
  Logger.log('Clave creada. Consúltela en Configuración del proyecto > Propiedades del script.');
}

/** Envía un correo de prueba a la cuenta dueña del script, para autorizar el permiso de correo. */
function probarCorreo() {
  enviarCorreo(Session.getEffectiveUser().getEmail(), 'Coordinación del curso', '123456', true);
}
