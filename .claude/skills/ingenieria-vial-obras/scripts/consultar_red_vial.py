#!/usr/bin/env python3
"""
Consulta la malla vial de Antioquia publicada en ArcGIS Online (servicio "R10", red vial reportada en la
Circular 10 del Departamento) y entrega tablas limpias con los dominios decodificados.

Servicio: https://services5.arcgis.com/K90UQIB09TmTjUL8/arcgis/rest/services/R10/FeatureServer
  capa 1 = Red vial primaria, capa 2 = Red vial secundaria, capa 3 = Red vial terciaria

Requiere internet y solo la biblioteca estándar de Python (más pandas/openpyxl si exporta a Excel).

Ejemplos:
    # Buscar por código o nombre en las tres capas
    python consultar_red_vial.py buscar "05282VT28"
    python consultar_red_vial.py buscar "Concordia" --capas 2 3

    # Todas las vías terciarias de un municipio (código DANE) y exportar
    python consultar_red_vial.py municipio 05282 --salida fredonia.xlsx

    # Resumen de kilómetros por subregión, competencia, superficie y estado (capa terciaria)
    python consultar_red_vial.py resumen --capa 3 --por SUBREGION ESTADO

    # Interpretar un código de vía sin consultar el servicio
    python consultar_red_vial.py codigo 25AN01-2-1

    # GeoJSON (geometría WGS84) para un mapa o un SIG
    python consultar_red_vial.py buscar "25AN02" --geojson via.geojson

Notas de calidad (verificadas en el servicio en nov. 2026, ver references/red-vial-antioquia-r10.md):
  - La capa 1 (primaria) usa texto libre en COMPETENTE y muchos registros traen L_GPS = 0 y ANCHO_VIA = 1.
  - La capa 2 (secundaria) trae SUBREGION, MUNICIPIO y COMPETENTE vacíos (" ") en muchos registros.
  - La capa 3 (terciaria) es la más completa: dominios en SUPERFICIE, ESTADO, FUENTEINFO.
  - Las longitudes se reportan en km (L_ODOMETRO, L_GPS); Shape__Length está en metros (EPSG:3116).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict

BASE = "https://services5.arcgis.com/K90UQIB09TmTjUL8/arcgis/rest/services/R10/FeatureServer"
CAPAS = {1: "Red vial primaria", 2: "Red vial secundaria", 3: "Red vial terciaria"}
PAGINA = 2000  # maxRecordCount del servicio
TIMEOUT = 60

# Dominios publicados por el servicio (capas 2 y 3). Se usan si el servicio no responde con dominios.
DOMINIOS_RESPALDO = {
    "SUBREGION": {
        "SR01": "Valle de Aburrá", "SR02": "Bajo Cauca", "SR03": "Magdalena Medio", "SR04": "Nordeste",
        "SR05": "Norte", "SR06": "Occidente", "SR07": "Oriente", "SR08": "Suroeste", "SR09": "Urabá",
    },
    "COMPETENTE": {
        "01": "Departamento de Antioquia", "02": "Municipio",
        "03": "Agencia Nacional de Infraestructura - ANI", "04": "INVIAS", "05": "Concesión",
    },
    "ORDEN": {1: "Primer orden", 2: "Segundo orden", 3: "Tercer orden"},
    "TIPO_VIA": {1: "Primaria", 2: "Secundaria", 3: "Terciaria"},
    "SUPERFICIE": {
        "01": "Tierra", "02": "Afirmado", "03": "Pavimento asfáltico", "04": "Tratamiento superficial",
        "05": "Pavimento rígido", "06": "Placa huella", "07": "Pavimento articulado", "08": "Otro",
        "09": "Rieles", "10": "Pavimento",
    },
    "ESTADO": {
        "01": "Bueno", "02": "Regular", "03": "Malo", "04": "Pésimo", "05": "Intransitable",
        "98": "Otro", "99": "Sin información",
    },
    "FUENTEINFO": {
        "01": "SIF", "02": "Municipio", "03": "PVSP", "04": "INVIAS", "05": "ANI",
        "06": "Ministerio de Transporte", "07": "Ortofoto - SIF",
    },
}

# Erratas publicadas en los nombres de dominio del servicio
_ERRATAS = {
    "Angencia Nacional de Infraestructura - ANI": "Agencia Nacional de Infraestructura - ANI",
    "Tratamienot superficial": "Tratamiento superficial",
    "Valle de Aburra": "Valle de Aburrá",
    "Uraba": "Urabá",
}

CAMPOS_TABLA = [
    "CAPA", "CODIGO_VIA", "NOMBRE_VIA", "SUBREGION", "MUNICIPIO", "COMPETENTE", "ORDEN", "TIPO_VIA",
    "INICIO", "FIN", "CENTRO_POBLADO", "L_ODOMETRO", "L_GPS", "LONG_GEOM_KM", "ANCHO_VIA",
    "SUPERFICIE", "ESTADO", "FUENTEINFO", "PRODUCTO_PRINCIPAL", "CONCESION", "OBSERVACIONES", "CIRCULAR",
]


# --------------------------------------------------------------------------- HTTP

def _get(url: str, params: dict, reintentos: int = 3) -> dict:
    q = urllib.parse.urlencode(params)
    completo = f"{url}?{q}"
    ultimo = None
    for intento in range(reintentos):
        try:
            with urllib.request.urlopen(completo, timeout=TIMEOUT) as r:
                datos = json.loads(r.read().decode("utf-8"))
            if isinstance(datos, dict) and "error" in datos:
                raise RuntimeError(f"ArcGIS respondió error: {datos['error']}")
            return datos
        except (urllib.error.URLError, TimeoutError, RuntimeError) as e:
            ultimo = e
            time.sleep(1.5 * (intento + 1))
    raise SystemExit(f"No se pudo consultar el servicio ({ultimo}). ¿Hay conexión a internet?")


_cache_dominios: dict[int, dict] = {}


def dominios(capa: int) -> dict:
    """Dominios codificados de la capa (desde el servicio; si falla, los de respaldo)."""
    if capa in _cache_dominios:
        return _cache_dominios[capa]
    doms = {k: dict(v) for k, v in DOMINIOS_RESPALDO.items()}
    try:
        meta = _get(f"{BASE}/{capa}", {"f": "json"}, reintentos=1)
        for campo in meta.get("fields", []):
            d = campo.get("domain") or {}
            if d.get("type") == "codedValue":
                doms[campo["name"]] = {cv["code"]: _ERRATAS.get(cv["name"], cv["name"])
                                       for cv in d.get("codedValues", [])}
    except SystemExit:
        pass
    _cache_dominios[capa] = doms
    return doms


def consultar(capa: int, where: str, geometria: bool = False) -> list[dict]:
    """Devuelve todas las entidades que cumplen `where`, paginando de a 2000."""
    url = f"{BASE}/{capa}/query"
    salida, offset = [], 0
    while True:
        params = {
            "where": where, "outFields": "*", "returnGeometry": "true" if geometria else "false",
            "resultOffset": offset, "resultRecordCount": PAGINA, "orderByFields": "OBJECTID",
            "f": "geojson" if geometria else "json",
        }
        if geometria:
            params["outSR"] = 4326
        datos = _get(url, params)
        feats = datos.get("features", [])
        for f in feats:
            if geometria:
                f.setdefault("properties", {})["CAPA"] = capa
                salida.append(f)
            else:
                at = dict(f.get("attributes", {}))
                at["CAPA"] = capa
                salida.append(at)
        if not feats or not (datos.get("exceededTransferLimit") or
                             datos.get("properties", {}).get("exceededTransferLimit")):
            break
        offset += len(feats)
    return salida


def contar(capa: int, where: str = "1=1") -> int:
    return int(_get(f"{BASE}/{capa}/query", {"where": where, "returnCountOnly": "true", "f": "json"})
               .get("count", 0))


# --------------------------------------------------------------------------- Limpieza

def _limpio(v):
    if isinstance(v, str):
        v = re.sub(r"\s+", " ", v).strip()
        return v or None
    return v


def decodificar(registro: dict) -> dict:
    """Limpia espacios, traduce dominios y agrega longitud geométrica en km."""
    capa = registro.get("CAPA")
    doms = dominios(capa) if capa else DOMINIOS_RESPALDO
    r = {k: _limpio(v) for k, v in registro.items()}
    # La capa 2 publica TIPO_SUPERFICIE / ESTADO_SUPERFICIE numéricos; la 3, SUPERFICIE / ESTADO texto.
    if r.get("SUPERFICIE") is None and r.get("TIPOSUPERFICIE") not in (None, 0):
        r["SUPERFICIE"] = f"{int(r['TIPOSUPERFICIE']):02d}"
    if r.get("ESTADO") is None and r.get("ESTADO_SUPERFICIE") not in (None, 0):
        r["ESTADO"] = f"{int(r['ESTADO_SUPERFICIE']):02d}"
    for campo, mapa in doms.items():
        v = r.get(campo)
        if v is None:
            continue
        clave = v
        if campo in ("ORDEN", "TIPO_VIA"):
            try:
                clave = int(v)
            except (TypeError, ValueError):
                pass
        r[campo] = mapa.get(clave, v)  # si no está en el dominio, se deja el texto original
    if r.get("ORDEN") == 0:
        r["ORDEN"] = None
    if r.get("Shape__Length") is not None:
        r["LONG_GEOM_KM"] = round(float(r["Shape__Length"]) / 1000, 3)
    return r


# --------------------------------------------------------------------------- Código de vía

def interpretar_codigo(codigo: str) -> dict:
    """
    Interpreta la estructura del código de vía. Convenciones observadas en el servicio R10:
      05282VT28   -> terciaria: código DANE del municipio (05282) + "VT" + consecutivo (28)
      25AN01-2-1  -> secundaria departamental: ruta nacional 25 + "AN" (Antioquia) + consecutivo 01,
                     ramal 2, sub-ramal 1
      25ANF       -> tramo con sufijo literal (variante/paso), ruta 25
    La correspondencia "ruta + AN + consecutivo" es la convención de codificación de vías
    departamentales; confírmela con el inventario oficial antes de citarla en un acto. [INFERENCIA]
    """
    c = (codigo or "").strip().upper().replace(" ", "")
    m = re.fullmatch(r"(05\d{3})VT(\d+)([A-Z]?)", c)
    if m:
        return {"codigo": c, "tipo": "terciaria", "municipio_dane": m.group(1),
                "consecutivo": m.group(2) + m.group(3)}
    m = re.fullmatch(r"(\d{2})AN(\d{2})?([A-Z]*)((?:-\d+)*)", c)
    if m:
        ramales = [x for x in m.group(4).split("-") if x]
        return {"codigo": c, "tipo": "secundaria departamental", "ruta_nacional": m.group(1),
                "consecutivo": m.group(2), "sufijo": m.group(3) or None, "ramales": ramales}
    return {"codigo": c, "tipo": "no reconocido",
            "nota": "No sigue los patrones 05xxxVTnn ni rrANnn; buscar por nombre."}


# --------------------------------------------------------------------------- Salidas

def _fmt_num(x, dec=2):
    if x is None:
        return ""
    s = f"{x:,.{dec}f}"
    return s.replace(",", "_").replace(".", ",").replace("_", ".")


def imprimir_tabla(filas: list[dict], campos: list[str], maximo: int = 50):
    if not filas:
        print("Sin resultados.")
        return
    vista = filas[:maximo]
    anchos = {c: min(40, max(len(c), *(len(str(f.get(c) or "")) for f in vista))) for c in campos}
    print(" | ".join(c.ljust(anchos[c]) for c in campos))
    print("-+-".join("-" * anchos[c] for c in campos))
    for f in vista:
        print(" | ".join(str(f.get(c) if f.get(c) is not None else "")[:40].ljust(anchos[c]) for c in campos))
    if len(filas) > maximo:
        print(f"... {len(filas) - maximo} filas más (use --salida para exportar todo)")


def exportar(filas: list[dict], ruta: str):
    campos = [c for c in CAMPOS_TABLA if any(c in f for f in filas)]
    if ruta.lower().endswith(".xlsx"):
        try:
            import pandas as pd
        except ImportError:
            raise SystemExit("Para .xlsx instale pandas y openpyxl, o use .csv")
        pd.DataFrame(filas)[campos].to_excel(ruta, index=False)
    else:
        import csv
        with open(ruta, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.DictWriter(fh, fieldnames=campos, extrasaction="ignore", delimiter=";")
            w.writeheader()
            w.writerows(filas)
    print(f"Exportado: {ruta} ({len(filas)} filas)")


def resumir(filas: list[dict], por: list[str]) -> list[dict]:
    agg = defaultdict(lambda: {"tramos": 0, "km_gps": 0.0, "km_geom": 0.0, "sin_longitud": 0})
    for f in filas:
        clave = tuple(f.get(p) or "(vacío)" for p in por)
        a = agg[clave]
        a["tramos"] += 1
        km = f.get("L_GPS") or 0
        if not km:
            a["sin_longitud"] += 1
        a["km_gps"] += float(km)
        a["km_geom"] += float(f.get("LONG_GEOM_KM") or 0)
    out = []
    for clave, a in sorted(agg.items(), key=lambda kv: -kv[1]["km_geom"]):
        fila = dict(zip(por, clave))
        fila.update(tramos=a["tramos"], km_gps=round(a["km_gps"], 2), km_geometria=round(a["km_geom"], 2),
                    tramos_sin_L_GPS=a["sin_longitud"])
        out.append(fila)
    return out


# --------------------------------------------------------------------------- CLI

def _like(texto: str) -> str:
    t = texto.replace("'", "''").upper()
    return f"(UPPER(CODIGO_VIA) LIKE '%{t}%' OR UPPER(NOMBRE_VIA) LIKE '%{t}%')"


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("buscar", help="Buscar por código o nombre de vía")
    b.add_argument("texto")
    b.add_argument("--capas", nargs="+", type=int, default=[1, 2, 3])
    b.add_argument("--salida")
    b.add_argument("--geojson")

    m = sub.add_parser("municipio", help="Vías de un municipio por código DANE (capa terciaria por defecto)")
    m.add_argument("dane", help="Código DANE de 5 dígitos, p. ej. 05282")
    m.add_argument("--capas", nargs="+", type=int, default=[3])
    m.add_argument("--salida")
    m.add_argument("--geojson")

    r = sub.add_parser("resumen", help="Kilómetros y tramos agrupados")
    r.add_argument("--capa", type=int, default=3, choices=[1, 2, 3])
    r.add_argument("--por", nargs="+", default=["SUBREGION"])
    r.add_argument("--where", default="1=1")
    r.add_argument("--salida")

    c = sub.add_parser("conteo", help="Número de tramos por capa")

    k = sub.add_parser("codigo", help="Interpretar un código de vía (sin internet)")
    k.add_argument("codigo")

    a = p.parse_args(argv)

    if a.cmd == "codigo":
        print(json.dumps(interpretar_codigo(a.codigo), ensure_ascii=False, indent=2))
        return 0

    if a.cmd == "conteo":
        for capa, nombre in CAPAS.items():
            print(f"Capa {capa} ({nombre}): {contar(capa)} tramos")
        return 0

    if a.cmd in ("buscar", "municipio"):
        if a.cmd == "buscar":
            where = _like(a.texto)
        else:
            if not re.fullmatch(r"05\d{3}", a.dane):
                raise SystemExit("El código DANE de un municipio de Antioquia tiene 5 dígitos y empieza por 05.")
            where = f"MUNICIPIO = '{a.dane}' OR CODIGO_VIA LIKE '{a.dane}%'"
        if a.geojson:
            feats = []
            for capa in a.capas:
                feats += consultar(capa, where, geometria=True)
            for f in feats:
                f["properties"] = decodificar(f["properties"])
            with open(a.geojson, "w", encoding="utf-8") as fh:
                json.dump({"type": "FeatureCollection", "features": feats}, fh, ensure_ascii=False)
            print(f"GeoJSON: {a.geojson} ({len(feats)} tramos, WGS84)")
        filas = []
        for capa in a.capas:
            filas += [decodificar(x) for x in consultar(capa, where)]
        imprimir_tabla(filas, ["CAPA", "CODIGO_VIA", "NOMBRE_VIA", "MUNICIPIO", "COMPETENTE",
                               "L_GPS", "SUPERFICIE", "ESTADO"])
        total = sum(float(f.get("L_GPS") or 0) for f in filas)
        print(f"\nTramos: {len(filas)} | Longitud L_GPS: {_fmt_num(total)} km")
        if a.salida:
            exportar(filas, a.salida)
        return 0

    if a.cmd == "resumen":
        filas = [decodificar(x) for x in consultar(a.capa, a.where)]
        tabla = resumir(filas, a.por)
        imprimir_tabla(tabla, a.por + ["tramos", "km_gps", "km_geometria", "tramos_sin_L_GPS"], maximo=200)
        print(f"\nCapa {a.capa} — tramos: {len(filas)} | km (L_GPS): "
              f"{_fmt_num(sum(t['km_gps'] for t in tabla))} | km (geometría): "
              f"{_fmt_num(sum(t['km_geometria'] for t in tabla))}")
        print("Fuente: servicio R10 (ArcGIS Online, Gobernación de Antioquia). "
              "Fecha de consulta: " + time.strftime("%Y-%m-%d"))
        if a.salida:
            import csv
            with open(a.salida, "w", newline="", encoding="utf-8-sig") as fh:
                w = csv.DictWriter(fh, fieldnames=list(tabla[0].keys()) if tabla else a.por, delimiter=";")
                w.writeheader()
                w.writerows(tabla)
            print(f"Exportado: {a.salida}")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
