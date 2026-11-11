#!/usr/bin/env python3
"""
Perfil de calidad de un archivo Excel/CSV antes de analizarlo.

Uso:
    python perfilar_excel.py archivo.xlsx [--hoja NOMBRE] [--salida perfil.md]

Reporta por hoja: fila de encabezado detectada, dimensiones, hojas ocultas, celdas combinadas,
fórmulas y errores (#REF!, #N/A…), columnas (tipo inferido, vacíos, únicos, ejemplos), números guardados
como texto, duplicados exactos, posibles filas de total/subtotal y estadísticas de columnas numéricas.
"""
import argparse
import re
import sys
from datetime import date, datetime
import warnings
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils_co import a_numero, columna_numerica, leer_tabla, numero  # noqa: E402

warnings.filterwarnings("ignore", category=UserWarning)

ERRORES = ("#REF!", "#N/A", "#DIV/0!", "#VALUE!", "#NAME?", "#NUM!", "#NULL!", "#¡REF!", "#N/D", "#¡DIV/0!", "#¡VALOR!")
PALABRAS_TOTAL = ("total", "subtotal", "suma", "gran total")


def info_openpyxl(ruta):
    """Hojas ocultas, celdas combinadas, fórmulas y errores (solo .xlsx/.xlsm)."""
    try:
        from openpyxl import load_workbook
    except ImportError:
        return {}
    out = {}
    try:
        wb_f = load_workbook(ruta, data_only=False, read_only=False)
    except Exception as e:  # archivo protegido, .xls, etc.
        return {"_error": str(e)}
    for ws in wb_f.worksheets:
        formulas = 0
        errores = 0
        for fila in ws.iter_rows():
            for c in fila:
                v = c.value
                if isinstance(v, str):
                    if v.startswith("="):
                        formulas += 1
                    elif v.strip() in ERRORES:
                        errores += 1
        out[ws.title] = {
            "estado": ws.sheet_state,
            "combinadas": len(ws.merged_cells.ranges),
            "formulas": formulas,
            "errores_texto": errores,
            "dimension": ws.dimensions,
        }
    return out


RE_FECHA = re.compile(r"^\d{1,4}[/-]\d{1,2}[/-]\d{1,4}")


def es_fecha(serie):
    vals = serie.dropna().head(200)
    if len(vals) == 0:
        return False
    ok = sum(isinstance(v, (datetime, date, pd.Timestamp)) or bool(RE_FECHA.match(str(v).strip())) for v in vals)
    return ok / len(vals) > 0.8


def perfil_hoja(ruta, hoja):
    df, fila_enc = leer_tabla(ruta, hoja)
    lineas = [f"- Fila de encabezado detectada: {fila_enc + 1} (base 1)",
              f"- Filas de datos: {len(df)} · Columnas: {len(df.columns)}"]
    dup = df.duplicated().sum()
    lineas.append(f"- Filas duplicadas exactas: {dup}")
    cols_dup = [c for c in df.columns if list(df.columns).count(c) > 1]
    if cols_dup:
        lineas.append(f"- **Encabezados repetidos:** {sorted(set(cols_dup))}")

    # posibles filas de total
    mask_total = df.apply(lambda f: any(isinstance(v, str) and v.strip().lower().startswith(PALABRAS_TOTAL) for v in f), axis=1)
    if mask_total.any():
        idx = [int(i) + fila_enc + 2 for i in df.index[mask_total][:10]]
        lineas.append(f"- **Posibles filas de total/subtotal** (filas Excel ≈ {idx}): exclúyalas antes de sumar.")

    filas_tabla = ["| Columna | Tipo | Vacíos | Únicos | Ejemplos | Observación |", "|---|---|---|---|---|---|"]
    numericas = {}
    for c in df.columns:
        s = df[c] if not isinstance(df[c], pd.DataFrame) else df[c].iloc[:, 0]
        vacios = int(s.isna().sum() + (s.astype(str).str.strip() == "").sum())
        unicos = s.nunique(dropna=True)
        ejemplos = ", ".join(str(v)[:25] for v in s.dropna().unique()[:3])
        obs = []
        if columna_numerica(s):
            tipo = "numérica"
            conv = s.map(a_numero)
            numericas[c] = conv
            textos = sum(isinstance(v, str) for v in s.dropna())
            if textos:
                obs.append(f"{textos} números guardados como texto")
            if (conv < 0).any():
                obs.append(f"{int((conv < 0).sum())} negativos")
        elif es_fecha(s):
            tipo = "fecha"
        else:
            tipo = "texto"
            if unicos and unicos < 30 and len(s.dropna()) > 50:
                obs.append("categórica")
            espacios = s.dropna().astype(str).map(lambda x: x != x.strip()).sum()
            if espacios:
                obs.append(f"{espacios} con espacios sobrantes")
        if vacios / max(len(s), 1) > 0.5:
            obs.append("más de 50 % vacía")
        filas_tabla.append(f"| {c} | {tipo} | {vacios} | {unicos} | {ejemplos} | {'; '.join(obs)} |")

    stats = []
    if numericas:
        stats = ["| Columna numérica | Suma | Mínimo | Mediana | Máximo |", "|---|---|---|---|---|"]
        for c, conv in numericas.items():
            sin_total = conv[~mask_total] if mask_total.any() else conv
            stats.append(f"| {c} | {numero(sin_total.sum())} | {numero(sin_total.min())} | "
                         f"{numero(sin_total.median())} | {numero(sin_total.max())} |")
        if mask_total.any():
            stats.append("\n*Sumas calculadas excluyendo las filas que parecen totales.*")
    return "\n".join(lineas), "\n".join(filas_tabla), "\n".join(stats)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivo")
    ap.add_argument("--hoja")
    ap.add_argument("--salida")
    a = ap.parse_args()
    ruta = a.archivo
    partes = [f"# Perfil de datos: `{Path(ruta).name}`\n"]
    es_excel = not ruta.lower().endswith((".csv", ".txt"))
    meta = info_openpyxl(ruta) if ruta.lower().endswith((".xlsx", ".xlsm")) else {}
    if es_excel:
        hojas = [a.hoja] if a.hoja else pd.ExcelFile(ruta).sheet_names
    else:
        hojas = [0]
    for h in hojas:
        partes.append(f"## Hoja: {h}\n")
        m = meta.get(h, {}) if isinstance(h, str) else {}
        if m:
            partes.append(f"- Estado: {m['estado']} · Rango: {m['dimension']} · Celdas combinadas: {m['combinadas']} · "
                          f"Fórmulas: {m['formulas']} · Errores visibles: {m['errores_texto']}")
            if m["estado"] != "visible":
                partes.append("- **Hoja oculta**: confirme con el usuario si debe incluirse.")
        try:
            resumen, cols, stats = perfil_hoja(ruta, h)
        except Exception as e:
            partes.append(f"- No se pudo leer como tabla: {e}\n")
            continue
        partes += [resumen, "", "### Columnas", cols, ""]
        if stats:
            partes += ["### Columnas numéricas", stats, ""]
    if meta.get("_error"):
        partes.append(f"> Aviso openpyxl: {meta['_error']}")
    partes.append("\n> Revise el perfil antes de concluir: totales incluidos, unidades (pesos vs. millones), "
                  "fechas de corte y filas ocultas cambian los resultados.")
    texto = "\n".join(partes)
    if a.salida:
        Path(a.salida).write_text(texto, encoding="utf-8")
        print(f"Perfil guardado en {a.salida}")
    else:
        print(texto)


if __name__ == "__main__":
    main()
