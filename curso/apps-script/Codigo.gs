/**
 * Registro del Curso de contratación estatal — Gobernación de Antioquia (versión 4)
 * Google Apps Script vinculado a una hoja de cálculo de Google.
 * Desarrollado por: Alexander Gómez Avendaño.
 *
 * Hojas que crea:
 *   Inscritos  -> un renglón por persona: datos de inscripción y estado (pendiente, aprobado, rechazado)
 *   Registros  -> un renglón por evento (ingreso, módulo, taller, evaluación)
 *   Resumen    -> un renglón por persona (último estado y mejor resultado)
 *   Invitaciones -> correos invitados desde la consola de administración (admin.html)
 *
 * Inscripción con aprobación de la coordinación:
 *   1. La persona escribe sus datos en la página (accion=registro). Queda "pendiente".
 *   2. La coordinación recibe un correo con los botones Aprobar y Rechazar (enlaces firmados).
 *   3. Al aprobar, la persona recibe el correo de bienvenida con el botón "Entrar al curso":
 *      un enlace personal que abre el curso ya identificado (accion=entrar). No hay códigos que copiar.
 *   4. Si cambia de equipo, vuelve a escribir cédula y correo y recibe de nuevo su enlace.
 *
 * Las funciones internas terminan en "_" para que no se puedan llamar desde fuera.
 * Instalación: ver INSTALACION.md. Ejecute configurar() y generarClaveCoordinador() una vez.
 */

var HOJA_INS = 'Inscritos';
var HOJA_REG = 'Registros';
var HOJA_RES = 'Resumen';
var HOJA_INV = 'Invitaciones';
var COLS_INS = ['cedula', 'nombre', 'correo', 'dependencia', 'vinculacion', 'estado', 'inscripcion',
  'aprobacion', 'ultimo_ingreso', 'ingresos', 'token'];
var COLS_REG = ['recibido', 'tipo', 'cedula', 'nombre', 'dependencia', 'vinculacion', 'modulo',
  'modulos', 'practica', 'casos', 'final', 'indice', 'nivel', 'areas', 'intentos', 'intento',
  'aciertos', 'duracion_min', 'codigo', 'version', 'fecha_cliente', 'correo'];
var COLS_RES = ['cedula', 'nombre', 'dependencia', 'vinculacion', 'modulos', 'practica', 'casos',
  'final', 'indice', 'nivel', 'intentos', 'codigo', 'primer_registro', 'ultimo', 'correo'];
var TIPOS = ['ingreso', 'modulo', 'taller', 'evaluacion'];
var NIVELES = ['Avanzado', 'Competente', 'En desarrollo', 'Inicial'];
var URL_CURSO = 'https://alexandergomezsif.github.io/skills_Sector_publico_antioquia/curso/';
var NOMBRE_REMITENTE = 'Curso de contratación estatal';
var URL_REGISTRO = 'https://script.google.com/macros/s/AKfycbxsktMrFtqOtP5FrailMoZpr2E5bjN-fNCgu_t12aS65oa1_HwFsW7EtjGpk24d8Vjh/exec';
var MAX_SOLICITUDES_HORA = 5; // solicitudes por cédula por hora
var MAX_AVISOS_HORA = 40;     // avisos a la coordinación por hora (freno ante abusos)

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
    if (d.accion === 'registro') return json_(registro_(d));
    if (d.accion === 'entrar') return json_(entrar_(d));
    if (d.accion === 'revisar' || d.accion === 'decidir') return json_(revisarPost_(d));
    if (d.accion === 'admin') return json_(admin_(d));
    var ev = limpiar_(d);
    if (!ev) return json_({ ok: false, error: 'datos inválidos' });
    var ss = SpreadsheetApp.getActive();
    var ins = buscarInscrito_(ss, ev.cedula);
    if (!ins || !activo_(ins.fila) || !d.token || String(d.token) !== String(ins.fila.token)) {
      return json_({ ok: false, error: 'sesión no verificada' });
    }
    ev.correo = ins.fila.correo;
    ss.getSheetByName(HOJA_REG).appendRow(COLS_REG.map(function (c) { return c === 'recibido' ? new Date() : ev[c]; }));
    actualizarResumen_(ss.getSheetByName(HOJA_RES), ev);
    if (ev.tipo === 'ingreso') {
      var sh = ss.getSheetByName(HOJA_INS);
      sh.getRange(ins.n, COLS_INS.indexOf('ultimo_ingreso') + 1).setValue(new Date());
      sh.getRange(ins.n, COLS_INS.indexOf('ingresos') + 1).setValue((Number(ins.fila.ingresos) || 0) + 1);
    }
    return json_({ ok: true });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

/* ---------------- inscripción con aprobación ---------------- */

function activo_(f) { return f.estado === 'aprobado' || f.estado === 'verificado'; }

function registro_(d) {
  var p = perfilLimpio_(d);
  if (!p) return { ok: false, error: 'Revise la cédula, el nombre y el correo.' };
  var cache = CacheService.getScriptCache();
  var lim = Number(cache.get('lim_' + p.cedula) || 0);
  if (lim >= MAX_SOLICITUDES_HORA) return { ok: false, error: 'Ya hizo varias solicitudes. Espere una hora e intente de nuevo.' };
  if (MailApp.getRemainingDailyQuota() < 2) return { ok: false, error: 'El servicio de correo llegó a su límite diario. Intente mañana.' };
  cache.put('lim_' + p.cedula, String(lim + 1), 3600);

  var ss = SpreadsheetApp.getActive();
  var sh = ss.getSheetByName(HOJA_INS);
  var ins = buscarInscrito_(ss, p.cedula);

  if (ins && activo_(ins.fila)) { // ya aprobado: reenvía su enlace personal al correo registrado
    var tok = ins.fila.token;
    if (!tok) { tok = Utilities.getUuid(); sh.getRange(ins.n, COLS_INS.indexOf('token') + 1).setValue(tok); }
    correoBienvenida_(ins.fila.correo, ins.fila.nombre, ins.fila.cedula, tok, false);
    return { ok: true, estado: 'aprobado', enviado_a: enmascarar_(ins.fila.correo) };
  }
  if (ins && ins.fila.estado === 'rechazado') return { ok: true, estado: 'rechazado' };

  if (!ins) {
    var ahora = new Date();
    sh.appendRow(COLS_INS.map(function (c) {
      return { cedula: p.cedula, nombre: p.nombre, correo: p.correo, dependencia: p.dependencia,
        vinculacion: p.vinculacion, estado: 'pendiente', inscripcion: ahora, ingresos: 0 }[c] || '';
    }));
  } else {
    ['nombre', 'correo', 'dependencia', 'vinculacion'].forEach(function (c) {
      sh.getRange(ins.n, COLS_INS.indexOf(c) + 1).setValue(p[c]);
    });
  }
  // aviso a la coordinación: uno por persona cada 24 horas, con freno global por hora
  var avisos = Number(cache.get('avisos_hora') || 0);
  if (!cache.get('avi_' + p.cedula) && avisos < MAX_AVISOS_HORA) {
    correoCoordinacion_(p);
    cache.put('avi_' + p.cedula, '1', 21600);
    cache.put('avisos_hora', String(avisos + 1), 3600);
  }
  return { ok: true, estado: 'pendiente', enviado_a: enmascarar_(p.correo) };
}

/** La página del curso abre el enlace personal: devuelve el perfil si el enlace es válido. */
function entrar_(d) {
  var ced = String(d.cedula || '').replace(/\D/g, '');
  var tok = String(d.token || '');
  if (!/^\d{5,10}$/.test(ced) || tok.length < 20) return { ok: false, error: 'Enlace inválido.' };
  var ins = buscarInscrito_(SpreadsheetApp.getActive(), ced);
  if (!ins || !activo_(ins.fila) || String(ins.fila.token) !== tok) {
    return { ok: false, error: 'El enlace no es válido o la inscripción aún no está aprobada.' };
  }
  var f = ins.fila;
  return { ok: true, perfil: { cedula: String(f.cedula), nombre: f.nombre, correo: f.correo,
    dependencia: f.dependencia, vinculacion: f.vinculacion } };
}

/** La coordinación abre el botón del correo en la página del curso (#/coordinacion/...).
 *  Se usa la página del curso y no una página del script porque esta última falla cuando el navegador
 *  tiene varias cuentas de Google abiertas (Google agrega /u/1/ a la dirección). */
function revisarPost_(d) {
  var ced = String(d.ced || '').replace(/\D/g, '');
  var a = d.a === 'aprobar' ? 'aprobar' : d.a === 'rechazar' ? 'rechazar' : '';
  if (!a || !/^\d{5,10}$/.test(ced) || String(d.f || '') !== firma_(ced, a)) {
    return { ok: false, error: 'Enlace no válido. Use los botones del correo de inscripción, sin modificarlos.' };
  }
  if (d.accion === 'decidir') { var r = decidir_(ced, a); return { ok: true, titulo: r.titulo, texto: r.texto }; }
  var ins = buscarInscrito_(SpreadsheetApp.getActive(), ced);
  if (!ins) return { ok: false, error: 'No existe una inscripción con esa cédula.' };
  var f = ins.fila;
  return { ok: true, persona: { cedula: String(f.cedula), nombre: f.nombre, correo: f.correo,
    dependencia: f.dependencia, vinculacion: f.vinculacion, estado: f.estado } };
}

/** Aprueba o rechaza una inscripción desde el enlace firmado del correo de la coordinación. */
function decidir_(ced, accion) {
  var ss = SpreadsheetApp.getActive();
  var sh = ss.getSheetByName(HOJA_INS);
  var ins = buscarInscrito_(ss, ced);
  if (!ins) return { titulo: 'No encontrada', texto: 'No existe una inscripción con esa cédula.' };
  var f = ins.fila;
  var set = function (col, v) { sh.getRange(ins.n, COLS_INS.indexOf(col) + 1).setValue(v); };
  if (accion === 'aprobar') {
    if (activo_(f)) return { titulo: 'Ya estaba aprobada', texto: f.nombre + ' ya tenía acceso al curso. No se envió otro correo.' };
    var tok = Utilities.getUuid();
    set('token', tok); set('estado', 'aprobado'); set('aprobacion', new Date());
    correoBienvenida_(f.correo, f.nombre, f.cedula, tok, true);
    return { titulo: 'Inscripción aprobada', texto: 'Se envió el correo de bienvenida a ' + enmascarar_(f.correo) + '. ' + f.nombre + ' ya puede entrar al curso.' };
  }
  if (activo_(f)) {
    set('estado', 'rechazado'); set('token', '');
    return { titulo: 'Acceso retirado', texto: f.nombre + ' tenía acceso; se retiró. Su avance ya registrado se conserva en la hoja.' };
  }
  set('estado', 'rechazado');
  return { titulo: 'Inscripción rechazada', texto: 'La solicitud de ' + f.nombre + ' quedó rechazada. No se le envió correo.' };
}

function firma_(ced, accion) {
  var props = PropertiesService.getScriptProperties();
  var sec = props.getProperty('SECRETO_FIRMA');
  if (!sec) { sec = Utilities.getUuid() + Utilities.getUuid(); props.setProperty('SECRETO_FIRMA', sec); }
  var b = Utilities.computeHmacSha256Signature(accion + '|' + ced, sec);
  return Utilities.base64EncodeWebSafe(b).replace(/=+$/, '');
}

function correoCoordinador_() {
  return PropertiesService.getScriptProperties().getProperty('CORREO_COORDINADOR') || Session.getEffectiveUser().getEmail();
}

function marco_(titulo, cuerpo) {
  return '<div style="font-family:Arial,sans-serif;max-width:560px;color:#1c2723">' +
    '<div style="background:#0b5640;color:#fff;padding:18px 22px;border-radius:10px 10px 0 0">' +
    '<div style="font-size:13px;opacity:.85">Gobernación de Antioquia · formación interna</div>' +
    '<div style="font-size:20px;font-weight:bold;margin-top:4px">' + titulo + '</div></div>' +
    '<div style="border:1px solid #d5ded9;border-top:0;padding:20px 22px;border-radius:0 0 10px 10px">' + cuerpo +
    '<p style="font-size:12px;color:#5b6b64;border-top:1px solid #d5ded9;padding-top:10px;margin-top:18px">Datos tratados conforme a la Ley 1581 de 2012, solo para registrar el avance en el curso. Desarrollado por: Alexander Gómez Avendaño.</p>' +
    '</div></div>';
}
function boton_(url, texto, color) {
  return '<a href="' + url + '" style="display:inline-block;background:' + (color || '#018d38') + ';color:#fff;text-decoration:none;padding:11px 20px;border-radius:8px;font-weight:bold;margin:4px 8px 4px 0">' + texto + '</a>';
}

function correoCoordinacion_(p) {
  var url = function (a) { return URL_CURSO + '#/coordinacion/' + a + '/' + p.cedula + '/' + firma_(p.cedula, a); };
  var fila = function (k, v) { return '<tr><td style="padding:4px 12px 4px 0;color:#5b6b64">' + k + '</td><td style="padding:4px 0"><b>' + escapar_(v) + '</b></td></tr>'; };
  var html = marco_('Nueva inscripción al curso',
    '<p>Una persona pidió inscribirse al Curso de contratación estatal:</p>' +
    '<table style="font-size:14px;border-collapse:collapse">' + fila('Nombre', p.nombre) + fila('Cédula', p.cedula) +
    fila('Correo', p.correo) + fila('Dependencia', p.dependencia) + fila('Vinculación', p.vinculacion) + '</table>' +
    '<p style="margin-top:16px">' + boton_(url('aprobar'), 'Aprobar') + boton_(url('rechazar'), 'Rechazar', '#9b2c2c') + '</p>' +
    '<p style="font-size:13px;color:#5b6b64">Cada botón abre una página donde confirma la decisión. Al aprobar, la persona recibe el correo de bienvenida con su enlace de entrada.</p>');
  var texto = 'Nueva inscripción al curso: ' + p.nombre + ' (C.C. ' + p.cedula + '), ' + p.correo + ', ' + p.dependencia +
    '.\nAprobar: ' + url('aprobar') + '\nRechazar: ' + url('rechazar');
  MailApp.sendEmail({ to: correoCoordinador_(), subject: 'Inscripción al curso: ' + p.nombre + ' — ' + p.dependencia,
    body: texto, htmlBody: html, name: NOMBRE_REMITENTE });
}

function correoBienvenida_(destino, nombre, ced, token, primera) {
  var pila = String(nombre).split(' ')[0];
  var enlace = URL_CURSO + '#/acceso/' + ced + '/' + token;
  var html = marco_('Curso de contratación estatal desde cero',
    '<p>Hola, ' + escapar_(pila) + ':</p>' +
    (primera
      ? '<p>Su inscripción fue aprobada. Le damos la bienvenida al curso: recorrerá la vida de un contrato público en 15 módulos, resolverá un taller de casos de la Gobernación y presentará una evaluación final. Cada módulo se habilita al aprobar el anterior.</p>'
      : '<p>Pidió entrar al curso desde otro equipo o navegador. Use este botón:</p>') +
    '<p>' + boton_(enlace, 'Entrar al curso') + '</p>' +
    '<p style="font-size:13px;color:#5b6b64">Este enlace es personal: le abre el curso con su nombre y guarda su avance. No lo reenvíe. Si cambia de equipo, ingrese con su cédula y su correo y le llegará de nuevo.</p>');
  var texto = 'Hola, ' + pila + '.\n\n' + (primera ? 'Su inscripción al Curso de contratación estatal fue aprobada.' : 'Su enlace de entrada al curso:') +
    '\nEntre aquí: ' + enlace + '\n\nEl enlace es personal; no lo reenvíe.';
  MailApp.sendEmail({ to: destino, subject: primera ? 'Bienvenido(a) al Curso de contratación estatal' : 'Su enlace de entrada al Curso de contratación estatal',
    body: texto, htmlBody: html, name: NOMBRE_REMITENTE });
}

/** Página que abre el botón del correo de la coordinación: primero pide confirmar, luego aplica. */
function paginaRevisar_(p) {
  var ced = String(p.ced || '').replace(/\D/g, '');
  var a = p.a === 'aprobar' ? 'aprobar' : p.a === 'rechazar' ? 'rechazar' : '';
  var cuerpo;
  if (!a || !/^\d{5,10}$/.test(ced) || String(p.f || '') !== firma_(ced, a)) {
    cuerpo = '<h2>Enlace no válido</h2><p>Use los botones del correo de inscripción, sin modificarlos.</p>';
  } else if (p.ok === '1') {
    var lock = LockService.getScriptLock(); lock.waitLock(20000);
    try { var r = decidir_(ced, a); } finally { lock.releaseLock(); }
    cuerpo = '<h2>' + escapar_(r.titulo) + '</h2><p>' + escapar_(r.texto) + '</p><p class="m">Puede cerrar esta página.</p>';
  } else {
    var ins = buscarInscrito_(SpreadsheetApp.getActive(), ced);
    if (!ins) cuerpo = '<h2>No encontrada</h2><p>No existe una inscripción con esa cédula.</p>';
    else {
      var f = ins.fila;
      var url = URL_REGISTRO + '?accion=revisar&a=' + a + '&ced=' + ced + '&f=' + encodeURIComponent(p.f) + '&ok=1';
      cuerpo = '<h2>' + (a === 'aprobar' ? '¿Aprobar esta inscripción?' : '¿Rechazar esta inscripción?') + '</h2>' +
        '<p><b>' + escapar_(f.nombre) + '</b><br>C.C. ' + escapar_(f.cedula) + ' · ' + escapar_(f.correo) + '<br>' +
        escapar_(f.dependencia) + ' · ' + escapar_(f.vinculacion) + '</p><p class="m">Estado actual: ' + escapar_(f.estado) + '</p>' +
        '<p><a class="b' + (a === 'aprobar' ? '' : ' r') + '" href="' + url + '" target="_top">' +
        (a === 'aprobar' ? 'Confirmar aprobación' : 'Confirmar rechazo') + '</a></p>';
    }
  }
  var html = '<!DOCTYPE html><html><head><base target="_top"><meta name="viewport" content="width=device-width,initial-scale=1">' +
    '<style>body{font-family:Arial,sans-serif;background:#eef3f0;margin:0;padding:24px;color:#1c2723}' +
    '.c{max-width:520px;margin:auto;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.08)}' +
    '.h{background:#0b5640;color:#fff;padding:16px 20px;font-weight:bold}.x{padding:8px 20px 20px}h2{font-size:20px}' +
    '.m{color:#5b6b64;font-size:14px}.b{display:inline-block;background:#018d38;color:#fff;text-decoration:none;padding:12px 22px;border-radius:8px;font-weight:bold}.r{background:#9b2c2c}</style></head>' +
    '<body><div class="c"><div class="h">Curso de contratación estatal · coordinación</div><div class="x">' + cuerpo + '</div></div></body></html>';
  return HtmlService.createHtmlOutput(html).setTitle('Curso de contratación estatal · inscripción')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

/* ---------------- consola de administración (admin.html) ---------------- */

/** Todas las operaciones exigen la clave de coordinación en el cuerpo del POST (nunca en la dirección). */
function admin_(d) {
  var cache = CacheService.getScriptCache();
  var fallos = Number(cache.get('adm_fallos') || 0);
  if (fallos >= 20) return { ok: false, error: 'Demasiados intentos con clave errada. Espere una hora.' };
  var clave = PropertiesService.getScriptProperties().getProperty('CLAVE_COORDINADOR');
  if (!clave || String(d.clave || '') !== clave) {
    cache.put('adm_fallos', String(fallos + 1), 3600);
    return { ok: false, error: 'Clave de coordinación incorrecta.' };
  }
  var ss = SpreadsheetApp.getActive();
  if (d.op === 'resumen') {
    var porCed = {};
    tabla_(ss.getSheetByName(HOJA_RES)).forEach(function (r) { porCed[String(r.cedula)] = r; });
    var filas = tabla_(ss.getSheetByName(HOJA_INS)).map(function (i) {
      var r = porCed[String(i.cedula)] || {};
      return { cedula: String(i.cedula), nombre: i.nombre, correo: i.correo, dependencia: i.dependencia,
        vinculacion: i.vinculacion, estado: i.estado, inscripcion: i.inscripcion, aprobacion: i.aprobacion,
        ingresos: i.ingresos || 0, modulos: r.modulos || 0, practica: r.practica || 0, casos: r.casos || 0,
        final: r.final || 0, indice: r.indice || 0, nivel: r.nivel || '', intentos: r.intentos || 0,
        codigo: r.codigo || '', ultimo: r.ultimo || i.ultimo_ingreso || '' };
    });
    var inv = ss.getSheetByName(HOJA_INV) ? tabla_(ss.getSheetByName(HOJA_INV)) : [];
    return { ok: true, filas: filas, invitaciones: inv, cupo: MailApp.getRemainingDailyQuota() };
  }
  if (d.op === 'decidir') {
    var ced = String(d.ced || '').replace(/\D/g, '');
    var a = d.a === 'aprobar' ? 'aprobar' : d.a === 'rechazar' ? 'rechazar' : '';
    if (!a || !/^\d{5,10}$/.test(ced)) return { ok: false, error: 'Datos inválidos.' };
    if (a === 'aprobar' && MailApp.getRemainingDailyQuota() < 1) return { ok: false, error: 'Sin cupo de correo hoy.' };
    var r = decidir_(ced, a);
    return { ok: true, titulo: r.titulo, texto: r.texto };
  }
  if (d.op === 'reenviar') {
    var ins = buscarInscrito_(ss, String(d.ced || '').replace(/\D/g, ''));
    if (!ins || !activo_(ins.fila) || !ins.fila.token) return { ok: false, error: 'La persona no tiene una inscripción aprobada.' };
    if (MailApp.getRemainingDailyQuota() < 1) return { ok: false, error: 'Sin cupo de correo hoy.' };
    correoBienvenida_(ins.fila.correo, ins.fila.nombre, ins.fila.cedula, ins.fila.token, false);
    return { ok: true, texto: 'Enlace de entrada reenviado a ' + enmascarar_(ins.fila.correo) + '.' };
  }
  if (d.op === 'invitar') {
    var lista = (d.correos || []).map(function (c) { return String(c).trim().toLowerCase(); })
      .filter(function (c, i, arr) { return c && arr.indexOf(c) === i; });
    if (!lista.length) return { ok: false, error: 'Escriba al menos un correo.' };
    if (lista.length > 50) return { ok: false, error: 'Máximo 50 correos por envío.' };
    var cupo = MailApp.getRemainingDailyQuota();
    var sh = ss.getSheetByName(HOJA_INV);
    if (!sh) { sh = ss.insertSheet(HOJA_INV); sh.getRange(1, 1, 1, 2).setValues([['fecha', 'correo']]).setFontWeight('bold'); sh.setFrozenRows(1); }
    var enviados = [], errores = [];
    lista.forEach(function (c) {
      if (!/^[^\s@<>"']{1,64}@[^\s@<>"']{1,190}\.[a-z]{2,}$/.test(c)) { errores.push(c + ' (correo no válido)'); return; }
      if (enviados.length >= cupo - 2) { errores.push(c + ' (sin cupo de correo hoy)'); return; }
      try { correoInvitacion_(c); sh.appendRow([new Date(), c]); enviados.push(c); }
      catch (e) { errores.push(c + ' (' + String(e).slice(0, 80) + ')'); }
    });
    return { ok: true, enviados: enviados, errores: errores, cupo: MailApp.getRemainingDailyQuota() };
  }
  return { ok: false, error: 'Operación desconocida.' };
}

function correoInvitacion_(destino) {
  var paso = function (t) { return '<li style="margin:6px 0">' + t + '</li>'; };
  var html = marco_('Curso de contratación estatal desde cero',
    '<p>Cordial saludo:</p>' +
    '<p>Le invitamos a inscribirse en el <b>Curso de contratación estatal desde cero</b>, un curso virtual gratuito de formación interna para servidores y contratistas de la Gobernación de Antioquia. No necesita conocimientos previos ni ser abogado.</p>' +
    '<p>Recorrerá la vida de un contrato público, desde la necesidad hasta la liquidación, en <b>15 módulos cortos</b> (unas 5 horas en total, a su propio ritmo), con un taller de casos y una evaluación final. Con nivel Competente o Avanzado obtiene una constancia con código de verificación.</p>' +
    '<p>' + boton_(URL_CURSO, 'Ir al curso e inscribirme') + '</p>' +
    '<h3 style="color:#0b5640;font-size:16px;margin:18px 0 6px">Cómo inscribirse (3 minutos)</h3><ol style="padding-left:20px;margin:0">' +
    paso('Abra el enlace del botón verde, en computador o celular.') +
    paso('En <b>Ingreso al aula virtual</b> escriba su cédula, nombres y apellidos, correo, dependencia y vinculación.') +
    paso('Acepte la autorización de tratamiento de datos y pulse <b>Continuar</b>. Verá <b>Solicitud enviada</b>.') +
    paso('Cuando la coordinación apruebe su inscripción le llegará el correo <b>Bienvenido(a) al Curso de contratación estatal</b>.') +
    paso('En ese correo pulse <b>Entrar al curso</b> y empiece por el módulo 1.') + '</ol>' +
    '<p style="font-size:13px;color:#5b6b64;margin-top:14px">Si el correo de bienvenida no aparece, revise la carpeta de spam. Si cambia de computador, ingrese de nuevo con su cédula y el mismo correo. Para dudas o comentarios, responda este correo.</p>');
  var texto = 'Le invitamos a inscribirse en el Curso de contratación estatal desde cero (formación interna de la Gobernación de Antioquia).\n' +
    'Inscripción: ' + URL_CURSO + '\n\nEscriba sus datos, acepte la autorización de datos y espere el correo de bienvenida con el botón Entrar al curso.';
  MailApp.sendEmail({ to: destino, subject: 'Inscripción abierta: Curso de contratación estatal desde cero',
    body: texto, htmlBody: html, name: NOMBRE_REMITENTE });
}

/* ---------------- panel y verificación de constancias ---------------- */

function doGet(e) {
  var p = (e && e.parameter) || {};
  if (p.accion === 'revisar') return paginaRevisar_(p);
  if (p.accion === 'verificar') return verificar_(String(p.codigo || ''));
  return json_({ ok: false, error: 'acción desconocida' });
}

function verificar_(codigo) {
  if (!/^[0-9A-Z]{4,10}$/.test(codigo)) return json_({ ok: false, error: 'código inválido' });
  var filas = tabla_(SpreadsheetApp.getActive().getSheetByName(HOJA_RES));
  for (var i = 0; i < filas.length; i++) {
    if (String(filas[i].codigo) === codigo) {
      return json_({ ok: true, valido: true, nivel: filas[i].nivel, indice: filas[i].indice,
        cedula_final: String(filas[i].cedula).slice(-4) });
    }
  }
  return json_({ ok: true, valido: false });
}

/* ---------------- utilidades ---------------- */

function tabla_(sh) {
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

function buscarInscrito_(ss, ced) {
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

function perfilLimpio_(d) {
  var ced = String(d.cedula || '').replace(/\D/g, '');
  var correo = String(d.correo || '').trim().toLowerCase();
  if (!/^\d{5,10}$/.test(ced)) return null;
  if (!/^[^\s@<>"']{1,64}@[^\s@<>"']{1,190}\.[a-z]{2,}$/.test(correo)) return null;
  var p = { cedula: ced, correo: correo, nombre: txt_(d.nombre), dependencia: txt_(d.dependencia),
    vinculacion: txt_(d.vinculacion, 40) };
  if (p.nombre.length < 5) return null;
  return p;
}

function txt_(x, n) { return String(x == null ? '' : x).replace(/[\r\n\t]+/g, ' ').replace(/^[=+\-@]+/, '').slice(0, n || 120); }

function limpiar_(d) {
  var ced = String(d.cedula || '').replace(/\D/g, '');
  if (!/^\d{5,10}$/.test(ced)) return null;
  if (TIPOS.indexOf(d.tipo) < 0) return null;
  var nro = function (x, max) { var n = Number(x); return isFinite(n) && n >= 0 && n <= max ? Math.round(n * 10) / 10 : ''; };
  return {
    tipo: d.tipo, cedula: ced, nombre: txt_(d.nombre), dependencia: txt_(d.dependencia),
    vinculacion: txt_(d.vinculacion, 40), modulo: txt_(d.modulo, 10), modulos: nro(d.modulos, 60),
    practica: nro(d.practica, 100), casos: nro(d.casos, 100), final: nro(d.final, 100),
    indice: nro(d.indice, 100), nivel: NIVELES.indexOf(d.nivel) >= 0 ? d.nivel : '',
    areas: txt_(d.areas, 200), intentos: nro(d.intentos, 999), intento: nro(d.intento, 999),
    aciertos: nro(d.aciertos, 40), duracion_min: nro(d.duracion_min, 1440),
    codigo: txt_(d.codigo, 12), version: txt_(d.version, 30), fecha_cliente: txt_(d.fecha_cliente, 40), correo: ''
  };
}

function actualizarResumen_(sh, ev) {
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

function enmascarar_(c) { var p = String(c).split('@'); return p[0].slice(0, 2) + '•••@' + p[1]; }
function escapar_(s) { return String(s).replace(/[&<>"']/g, function (x) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[x]; }); }
function json_(o) {
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

/** Reenvía el aviso a la coordinación de todas las inscripciones pendientes (ejecútela desde el editor). */
function reenviarAvisosPendientes() {
  var filas = tabla_(SpreadsheetApp.getActive().getSheetByName(HOJA_INS));
  var n = 0;
  filas.forEach(function (f) {
    if (f.estado !== 'pendiente') return;
    correoCoordinacion_({ cedula: String(f.cedula), nombre: f.nombre, correo: f.correo,
      dependencia: f.dependencia, vinculacion: f.vinculacion });
    n++;
  });
  Logger.log('Avisos reenviados: ' + n);
}
