#!/usr/bin/env python3
"""
Calcula la ejecución presupuestal (apropiación, CDP, compromisos, obligaciones, pagos) por agrupación
y genera un Excel con fórmulas vivas, más un resumen en Markdown.

Uso:
    python ejecucion_presupuestal.py reporte.xlsx --agrupar "Dependencia" [--hoja NOMBRE] \
        [--salida ejecucion.xlsx] [--mapa apropiacion="Aprop. Definitiva" compromisos="RP"]

Detecta columnas por palabras clave (sin tildes, minúsculas):
    apropiacion  -> "apropiacion definitiva", "presupuesto definitivo", "apropiacion"
    cdp          -> "cdp", "disponibilidad"
    compromisos  -> "compromiso", "registro presupuestal", "rp"
    obligaciones -> "obligacion"
    pagos        -> "pago", "giro"
Use --mapa para fijar columnas cuando la detección falle. Revise el perfil (perfilar_excel.py) antes.
"""
import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils_co import a_numero, leer_tabla, normalizar_nombre, pesos, porcentaje  # noqa: E402

CLAVES = {
    "apropiacion": ["apropiacion_definitiva", "presupuesto_definitivo", "definitiva", "apropiacion"],
    "cdp": ["cdp", "disponibilidad"],
    "compromisos": ["compromiso", "registro_presupuestal", "rp"],
    "obligaciones": ["obligacion"],
    "pagos": ["pago", "giro"],
}
ORDEN = ["apropiacion", "cdp", "compromisos", "obligaciones", "pagos"]


def detectar(columnas, mapa):
    norm = {normalizar_nombre(c): c for c in columnas}
    res = {}
    for k in ORDEN:
        if k in mapa:
            res[k] = mapa[k]
            continue
        for clave in CLAVES[k]:
            cand = [orig for n, orig in norm.items()
                    if (n == clave or n.startswith(clave + "_") or ("_" + clave) in n or n.startswith(clave))
                    and orig not in res.values()
                    and not (k == "apropiacion" and "inicial" in n)]
            if cand:
                res[k] = cand[0]
                break
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivo")
    ap.add_argument("--hoja", default=0)
    ap.add_argument("--agrupar", required=True)
    ap.add_argument("--salida", default="ejecucion_presupuestal.xlsx")
    ap.add_argument("--mapa", nargs="*", default=[])
    ap.add_argument("--excluir-totales", action="store_true", default=True)
    a = ap.parse_args()

    mapa = dict(m.split("=", 1) for m in a.mapa)
    df, _ = leer_tabla(a.archivo, a.hoja)
    if a.agrupar not in df.columns:
        raise SystemExit(f"No existe la columna '{a.agrupar}'. Columnas: {list(df.columns)}")
    cols = detectar(df.columns, mapa)
    faltan = [k for k in ("apropiacion", "compromisos") if k not in cols]
    if faltan:
        raise SystemExit(f"No se detectaron columnas {faltan}. Use --mapa. Columnas: {list(df.columns)}")
    print("Columnas usadas:", cols)

    if a.excluir_totales:
        es_total = df.apply(lambda f: any(isinstance(v, str) and v.strip().lower().startswith(("total", "subtotal"))
                                          for v in f), axis=1)
        if es_total.any():
            print(f"Se excluyeron {int(es_total.sum())} filas de total/subtotal.")
        df = df[~es_total]
    for k, c in cols.items():
        df[k] = df[c].map(a_numero).fillna(0.0)
    df[a.agrupar] = df[a.agrupar].fillna("(sin dato)").astype(str).str.strip()
    g = df.groupby(a.agrupar, sort=False)[list(cols)].sum().reset_index()
    g = g.sort_values("apropiacion", ascending=False)

    # ---- Excel con fórmulas ----
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter

    wb = Workbook()
    ws = wb.active
    ws.title = "Ejecución"
    claves = [k for k in ORDEN if k in cols]
    titulos = {"apropiacion": "Apropiación definitiva", "cdp": "CDP", "compromisos": "Compromisos (RP)",
               "obligaciones": "Obligaciones", "pagos": "Pagos"}
    encab = [a.agrupar] + [titulos[k] for k in claves]
    pct = [("compromisos", "% compromisos"), ("obligaciones", "% obligaciones"), ("pagos", "% pagos")]
    pct = [(k, t) for k, t in pct if k in claves]
    encab += [t for _, t in pct]
    ws.append(["Ejecución presupuestal por " + a.agrupar])
    ws.append([f"Fuente: {Path(a.archivo).name}. Cifras en pesos. Porcentajes sobre apropiación definitiva."])
    ws.append([])
    ws.append(encab)
    fila0 = 5
    verde = PatternFill("solid", fgColor="0B5640")
    linea = Side(style="thin", color="D9DEE3")
    for i, (_, r) in enumerate(g.iterrows()):
        f = fila0 + i
        ws.cell(f, 1, r[a.agrupar])
        for j, k in enumerate(claves, start=2):
            ws.cell(f, j, float(r[k])).number_format = '#,##0'
        col_ap = get_column_letter(2)
        for j, (k, _) in enumerate(pct, start=2 + len(claves)):
            col_k = get_column_letter(2 + claves.index(k))
            c = ws.cell(f, j, f"=IF({col_ap}{f}=0,0,{col_k}{f}/{col_ap}{f})")
            c.number_format = "0.0%"
    ultima = fila0 + len(g) - 1
    ft = ultima + 1
    ws.cell(ft, 1, "Total")
    for j in range(2, 2 + len(claves)):
        L = get_column_letter(j)
        ws.cell(ft, j, f"=SUM({L}{fila0}:{L}{ultima})").number_format = '#,##0'
    for j, (k, _) in enumerate(pct, start=2 + len(claves)):
        col_k = get_column_letter(2 + claves.index(k))
        ws.cell(ft, j, f"=IF(B{ft}=0,0,{col_k}{ft}/B{ft})").number_format = "0.0%"
    for c in ws[4]:
        c.fill, c.font = verde, Font(bold=True, color="FFFFFF", name="Arial")
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for c in ws[ft]:
        c.font = Font(bold=True, name="Arial")
        c.fill = PatternFill("solid", fgColor="E6F2EA")
    ws["A1"].font = Font(bold=True, size=13, color="0B5640", name="Arial")
    ws["A2"].font = Font(italic=True, size=9, color="52606D", name="Arial")
    for fila in ws.iter_rows(min_row=4, max_row=ft):
        for c in fila:
            c.border = Border(top=linea, bottom=linea, left=linea, right=linea)
    ws.column_dimensions["A"].width = 42
    for j in range(2, len(encab) + 1):
        ws.column_dimensions[get_column_letter(j)].width = 18
    ws.freeze_panes = "B5"
    wb.save(a.salida)

    # ---- resumen markdown ----
    tot = g[claves].sum()
    print(f"\nExcel generado: {a.salida}\n")
    print("| " + " | ".join(encab) + " |")
    print("|" + "---|" * len(encab))
    for _, r in g.iterrows():
        vals = [pesos(r[k]) for k in claves] + [porcentaje(r[k] / r["apropiacion"] if r["apropiacion"] else 0) for k, _ in pct]
        print(f"| {r[a.agrupar]} | " + " | ".join(vals) + " |")
    vals = [pesos(tot[k]) for k in claves] + [porcentaje(tot[k] / tot["apropiacion"] if tot["apropiacion"] else 0) for k, _ in pct]
    print("| **Total** | " + " | ".join(vals) + " |")


if __name__ == "__main__":
    main()
