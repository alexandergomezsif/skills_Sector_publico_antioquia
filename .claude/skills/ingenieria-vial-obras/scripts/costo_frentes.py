#!/usr/bin/env python3
"""
Costo estimado de maquinaria por frente: equipos × días (u horas) × tarifa.

Tarifas por defecto: ../assets/tarifas-maquinaria-2026.json (hoja "Listas" del Excel de frentes activos,
oct. 2026; día = 8 horas). Verifique las tarifas contra el contrato vigente antes de usarlas en actas.

Uso:
    # Un frente en línea de comandos: --equipo CODIGO DIAS [CANTIDAD]
    python costo_frentes.py --equipo MT 10 --equipo "VQ DT" 10 2 --equipo RT 10

    # Varios frentes desde CSV (separador ; o ,) con columnas: frente;equipo;dias[;cantidad][;horas_dia]
    python costo_frentes.py --csv frentes.csv --salida costos.xlsx

    # Ver tarifas
    python costo_frentes.py --listar

Fórmula: costo = cantidad × días × horas_día × valor_hora  (con horas_día = 8 → valor_día de la tabla)
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import OrderedDict
from pathlib import Path

TARIFAS_DEFECTO = Path(__file__).resolve().parent.parent / "assets" / "tarifas-maquinaria-2026.json"


def cop(x: float) -> str:
    s = f"{x:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"$ {s}"


def cargar_tarifas(ruta: Path) -> tuple[dict, dict, dict]:
    d = json.loads(Path(ruta).read_text(encoding="utf-8"))
    tabla = {e["codigo"].upper(): e for e in d["equipos"]}
    alias = {k.upper(): v.upper() for k, v in d.get("alias", {}).items()}
    return tabla, alias, d


def normalizar(codigo: str, tabla: dict, alias: dict) -> str:
    c = " ".join(str(codigo).replace("\n", " ").split()).upper()
    c = alias.get(c, c)
    if c not in tabla:
        sugerencias = [k for k in tabla if k.split()[0] == c.split()[0]]
        extra = f" ¿Quiso decir: {', '.join(sugerencias)}?" if sugerencias else ""
        raise SystemExit(f"Equipo '{codigo}' sin tarifa.{extra} Use --listar para ver los códigos.")
    return c


def calcular(filas: list[dict], tabla: dict, alias: dict, horas_defecto: float) -> list[dict]:
    out = []
    for f in filas:
        cod = normalizar(f["equipo"], tabla, alias)
        cant = float(f.get("cantidad") or 1)
        dias = float(f["dias"])
        horas = float(f.get("horas_dia") or horas_defecto)
        vh = tabla[cod]["valor_hora"]
        out.append(OrderedDict(
            frente=f.get("frente") or "Frente",
            equipo=cod, descripcion=tabla[cod]["descripcion"], cantidad=cant, dias=dias, horas_dia=horas,
            dias_maquina=cant * dias, horas_maquina=cant * dias * horas, valor_hora=vh,
            costo=round(cant * dias * horas * vh, 2),
        ))
    return out


def leer_csv(ruta: str) -> list[dict]:
    texto = Path(ruta).read_text(encoding="utf-8-sig")
    sep = ";" if texto.count(";") >= texto.count(",") else ","
    filas = list(csv.DictReader(texto.splitlines(), delimiter=sep))
    norm = []
    for f in filas:
        g = {k.strip().lower(): (v or "").strip() for k, v in f.items() if k}
        for k in ("dias", "cantidad", "horas_dia"):
            if g.get(k):
                g[k] = g[k].replace(".", "").replace(",", ".") if "," in g[k] else g[k]
        norm.append(g)
    return norm


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--tarifas", default=str(TARIFAS_DEFECTO))
    p.add_argument("--equipo", nargs="+", action="append", metavar=("CODIGO", "DIAS"),
                   help="CODIGO DIAS [CANTIDAD]")
    p.add_argument("--frente", default="Frente")
    p.add_argument("--csv")
    p.add_argument("--horas-dia", type=float, default=8.0)
    p.add_argument("--salida", help=".xlsx o .csv")
    p.add_argument("--listar", action="store_true")
    a = p.parse_args(argv)

    tabla, alias, meta = cargar_tarifas(Path(a.tarifas))
    if a.listar:
        for k, e in tabla.items():
            print(f"{k:9} {cop(e['valor_hora']):>16}/h {cop(e['valor_dia_8h']):>18}/día  {e['descripcion']}")
        print(f"\nFuente: {meta['fuente']}\n{meta['advertencia']}")
        return 0

    filas = []
    if a.csv:
        filas += leer_csv(a.csv)
    for e in a.equipo or []:
        if len(e) not in (2, 3):
            raise SystemExit("--equipo requiere CODIGO DIAS [CANTIDAD]")
        filas.append({"frente": a.frente, "equipo": e[0], "dias": e[1], "cantidad": e[2] if len(e) == 3 else 1})
    if not filas:
        p.error("Indique --equipo o --csv (o --listar)")

    res = calcular(filas, tabla, alias, a.horas_dia)
    total = 0.0
    por_frente: dict[str, float] = OrderedDict()
    print(f"{'Frente':20} {'Equipo':9} {'Cant':>4} {'Días':>5} {'Días-máq':>8} {'Costo':>20}")
    for r in res:
        print(f"{r['frente'][:20]:20} {r['equipo']:9} {r['cantidad']:>4g} {r['dias']:>5g} "
              f"{r['dias_maquina']:>8g} {cop(r['costo']):>20}")
        total += r["costo"]
        por_frente[r["frente"]] = por_frente.get(r["frente"], 0) + r["costo"]
    if len(por_frente) > 1:
        print("\nSubtotal por frente:")
        for k, v in por_frente.items():
            print(f"  {k}: {cop(v)}")
    print(f"\nTOTAL: {cop(total)}")
    print(f"Fórmula: cantidad × días × {a.horas_dia:g} h/día × valor hora. {meta['advertencia']}")

    if a.salida:
        if a.salida.lower().endswith(".xlsx"):
            try:
                from openpyxl import Workbook
            except ImportError:
                raise SystemExit("Instale openpyxl o use .csv")
            wb = Workbook()
            ws = wb.active
            ws.title = "Costos"
            cab = list(res[0].keys())
            ws.append(cab)
            for i, r in enumerate(res, start=2):
                fila = list(r.values())
                ws.append(fila)
                # Fórmulas vivas: días-máquina, horas-máquina y costo
                ws.cell(i, cab.index("dias_maquina") + 1).value = f"=D{i}*E{i}"
                ws.cell(i, cab.index("horas_maquina") + 1).value = f"=D{i}*E{i}*F{i}"
                ws.cell(i, cab.index("costo") + 1).value = f"=H{i}*I{i}"
            n = len(res) + 1
            ws.cell(n + 1, 1).value = "TOTAL"
            ws.cell(n + 1, cab.index("costo") + 1).value = f"=SUM(J2:J{n})"
            for col in ("I", "J"):
                for c in ws[col][1:]:
                    c.number_format = '"$" #,##0.00'
            ws.cell(n + 3, 1).value = meta["fuente"]
            ws.cell(n + 4, 1).value = meta["advertencia"]
            wb.save(a.salida)
        else:
            with open(a.salida, "w", newline="", encoding="utf-8-sig") as fh:
                w = csv.DictWriter(fh, fieldnames=list(res[0].keys()), delimiter=";")
                w.writeheader()
                w.writerows(res)
        print(f"Exportado: {a.salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
