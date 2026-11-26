/**
 * Registro del Curso de contratación estatal — Gobernación de Antioquia
 * Google Apps Script vinculado a una hoja de cálculo de Google.
 *
 * Hojas que crea:
 *   Registros  -> un renglón por evento (ingreso, módulo, taller, evaluación)
 *   Resumen    -> un renglón por persona (último estado y mejor resultado)
 *
 * Instalación: ver INSTALACION.md. Antes de publicar, ejecute configurar() una vez
 * y defina la clave de coordinación en Configuración del proyecto > Propiedades del script:
 *   CLAVE_COORDINADOR = (una clave larga que solo conozca la coordinación)
 */

var HOJA_REG = 'Registros';
var HOJA_RES = 'Resumen';
var COLS_REG = ['recibido', 'tipo', 'cedula', 'nombre', 'dependencia', 'vinculacion', 'modulo',
  'modulos', 'practica', 'casos', 'final', 'indice', 'nivel', 'areas', 'intentos', 'intento',
  'aciertos', 'duracion_min', 'codigo', 'version', 'fecha_cliente'];
var COLS_RES = ['cedula', 'nombre', 'dependencia', 'vinculacion', 'modulos', 'practica', 'casos',
  'final', 'indice', 'nivel', 'intentos', 'codigo', 'primer_registro', 'ultimo'];
var TIPOS = ['ingreso', 'modulo', 'taller', 'evaluacion'];
var NIVELES = ['Avanzado', 'Competente', 'En desarrollo', 'Inicial'];

function configurar() {
  var ss = SpreadsheetApp.getActive();
  [[HOJA_REG, COLS_REG], [HOJA_RES, COLS_RES]].forEach(function (h) {
    var sh = ss.getSheetByName(h[0]) || ss.insertSheet(h[0]);
    if (sh.getLastRow() === 0) {
      sh.appendRow(h[1]);
      sh.setFrozenRows(1);
      sh.getRange(1, 1, 1, h[1].length).setFontWeight('bold');
    }
  });
  var res = ss.getSheetByName(HOJA_RES);
  res.getRange('A:A').setNumberFormat('@'); // la cédula como texto (conserva ceros)
  ss.getSheetByName(HOJA_REG).getRange('C:C').setNumberFormat('@');
}

/** Recibe eventos de la página del curso (POST, cuerpo JSON en texto plano). */
function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    var d = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    var ev = limpiar(d);
    if (!ev) return json({ ok: false, error: 'datos inválidos' });
    var ss = SpreadsheetApp.getActive();
    var reg = ss.getSheetByName(HOJA_REG);
    reg.appendRow(COLS_REG.map(function (c) { return c === 'recibido' ? new Date() : ev[c]; }));
    actualizarResumen(ss.getSheetByName(HOJA_RES), ev);
    return json({ ok: true });
  } catch (err) {
    return json({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

/** Panel de coordinación (requiere clave) y verificación de constancias (sin clave). */
function doGet(e) {
  var p = (e && e.parameter) || {};
  if (p.accion === 'verificar') return verificar(String(p.codigo || ''));
  var clave = PropertiesService.getScriptProperties().getProperty('CLAVE_COORDINADOR');
  if (!clave || p.clave !== clave) return json({ ok: false, error: 'clave inválida' });
  if (p.accion === 'resumen') {
    var sh = SpreadsheetApp.getActive().getSheetByName(HOJA_RES);
    var v = sh.getDataRange().getValues();
    var cab = v.shift();
    var filas = v.map(function (r) {
      var o = {};
      cab.forEach(function (c, i) { o[c] = r[i] instanceof Date ? Utilities.formatDate(r[i], 'America/Bogota', 'yyyy-MM-dd HH:mm') : r[i]; });
      return o;
    });
    return json({ ok: true, filas: filas });
  }
  return json({ ok: false, error: 'acción desconocida' });
}

function verificar(codigo) {
  if (!/^[0-9A-Z]{4,10}$/.test(codigo)) return json({ ok: false, error: 'código inválido' });
  var v = SpreadsheetApp.getActive().getSheetByName(HOJA_RES).getDataRange().getValues();
  var cab = v.shift();
  var ic = cab.indexOf('codigo');
  for (var i = 0; i < v.length; i++) {
    if (String(v[i][ic]) === codigo) {
      return json({ ok: true, valido: true, nivel: v[i][cab.indexOf('nivel')],
        indice: v[i][cab.indexOf('indice')], cedula_final: String(v[i][0]).slice(-4) });
    }
  }
  return json({ ok: true, valido: false });
}

function limpiar(d) {
  var ced = String(d.cedula || '').replace(/\D/g, '');
  if (!/^\d{5,10}$/.test(ced)) return null;
  if (TIPOS.indexOf(d.tipo) < 0) return null;
  var txt = function (x, n) { return String(x == null ? '' : x).replace(/[\r\n\t]+/g, ' ').replace(/^[=+\-@]+/, '').slice(0, n || 120); };
  var nro = function (x, max) { var n = Number(x); return isFinite(n) && n >= 0 && n <= max ? Math.round(n * 10) / 10 : ''; };
  return {
    tipo: d.tipo, cedula: ced, nombre: txt(d.nombre), dependencia: txt(d.dependencia),
    vinculacion: txt(d.vinculacion, 40), modulo: txt(d.modulo, 10), modulos: nro(d.modulos, 14),
    practica: nro(d.practica, 100), casos: nro(d.casos, 100), final: nro(d.final, 100),
    indice: nro(d.indice, 100), nivel: NIVELES.indexOf(d.nivel) >= 0 ? d.nivel : '',
    areas: txt(d.areas, 200), intentos: nro(d.intentos, 999), intento: nro(d.intento, 999),
    aciertos: nro(d.aciertos, 40), duracion_min: nro(d.duracion_min, 1440),
    codigo: txt(d.codigo, 12), version: txt(d.version, 30), fecha_cliente: txt(d.fecha_cliente, 40)
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
    if ((Number(ev.indice) || 0) < viejo) {
      ['nombre', 'dependencia', 'vinculacion'].forEach(function (c) {
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

function json(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
