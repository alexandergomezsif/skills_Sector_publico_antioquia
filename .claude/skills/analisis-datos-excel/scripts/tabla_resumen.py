#!/usr/bin/env python3
"""
Tabla resumen (tipo tabla dinámica) de cualquier Excel/CSV: agrupa, cuenta y suma.

Uso:
    python tabla_resumen.py contratos_secop.xlsx --agrupar "Modalidad de Contratacion" \
        --sumar "Valor del Contrato" [--agrupar2 "Estado Contrato"] [--filtro "Año=2026"] [--salida resumen.xlsx]

Útil para exportes de SECOP II (datos.gov.co), bases de contratos, inventarios, metas físicas.
Convierte cifras con formato colombiano, excluye filas de total y reporta participación %.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils_co import a_numero, leer_tabla, numero, pesos, porcentaje  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivo")
    ap.add_argument("--hoja", default=0)
    ap.add_argument("--agrupar", required=True)
    ap.add_argument("--agrupar2")
    ap.add_argument("--sumar", nargs="*", default=[])
    ap.add_argument("--filtro", nargs="*", default=[], help="Columna=valor (igualdad de texto)")
    ap.add_argument("--salida")
    ap.add_argument("--moneda", action="store_true", help="formatear sumas como pesos")
    a = ap.parse_args()

    df, _ = leer_tabla(a.archivo, a.hoja)
    es_total = df.apply(lambda f: any(isinstance(v, str) and v.strip().lower().startswith(("total", "subtotal")) for v in f), axis=1)
    df = df[~es_total]
    for f in a.filtro:
        c, v = f.split("=", 1)
        df = df[df[c].astype(str).str.strip() == v]
    claves = [a.agrupar] + ([a.agrupar2] if a.agrupar2 else [])
    for c in claves:
        df[c] = df[c].fillna("(sin dato)").astype(str).str.strip()
    for c in a.sumar:
        df[c] = df[c].map(a_numero)
        nulos = df[c].isna().sum()
        if nulos:
            print(f"Aviso: {nulos} valores no numéricos en '{c}' se tratan como vacíos.")
    agg = {c: "sum" for c in a.sumar}
    g = df.groupby(claves).agg(**{"registros": (a.agrupar, "size")}, **{c: (c, s) for c, s in agg.items()}).reset_index()
    orden = a.sumar[0] if a.sumar else "registros"
    g = g.sort_values(orden, ascending=False)
    base = g[orden].sum()
    g["participacion"] = g[orden] / base if base else 0

    fmt = pesos if a.moneda else numero
    enc = claves + ["Registros"] + a.sumar + [f"% de {orden}"]
    print("| " + " | ".join(enc) + " |")
    print("|" + "---|" * len(enc))
    for _, r in g.iterrows():
        print("| " + " | ".join([str(r[c]) for c in claves] + [numero(r["registros"])] +
                                [fmt(r[c]) for c in a.sumar] + [porcentaje(r["participacion"])]) + " |")
    print("| **Total** | " + " | ".join([""] * (len(claves) - 1) + [numero(g["registros"].sum())] +
                                     [fmt(g[c].sum()) for c in a.sumar] + ["100,0 %"]) + " |")
    if a.salida:
        g.to_excel(a.salida, index=False)
        print(f"\nGuardado en {a.salida}")


if __name__ == "__main__":
    main()
