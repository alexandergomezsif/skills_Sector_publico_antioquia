#!/usr/bin/env python3
"""
Calcula topes de menor y mínima cuantía (Ley 1150 de 2007, art. 2 num. 2 lit. b; Ley 1474 de 2011,
art. 94) y fechas de inicio de restricciones de la Ley de Garantías (Ley 996 de 2005).

Uso:
    python calcular_cuantias.py --anio 2026 --presupuesto-smmlv 5000000
    python calcular_cuantias.py --anio 2026 --presupuesto-pesos 12000000000000
    python calcular_cuantias.py --eleccion 2027-10-31 [--presidencial]
    python calcular_cuantias.py --adicion --valor-inicial 500000000 --anio-inicial 2025 \
        --adiciones 2026:150000000 2026:80000000

Actualice SMMLV_POR_ANIO cada enero (fuente: decreto del Ministerio del Trabajo).
"""
import argparse
import calendar
from datetime import date, timedelta

SMMLV_POR_ANIO = {
    2023: 1_160_000,
    2024: 1_300_000,
    2025: 1_423_500,
    2026: 1_750_905,  # Decreto 159 de 2026 (transitorio) — mismo valor del Decreto 1469 de 2025
}

# (presupuesto mínimo en SMMLV, tope de menor cuantía en SMMLV) — Ley 1150, art. 2, num. 2, lit. b)
ESCALA_MENOR_CUANTIA = [
    (1_200_000, 1000),
    (850_000, 850),
    (400_000, 650),
    (120_000, 450),
    (0, 280),
]


def pesos(v):
    return "$ " + f"{v:,.0f}".replace(",", ".")


def smmlv(anio):
    if anio not in SMMLV_POR_ANIO:
        raise SystemExit(f"No hay SMMLV cargado para {anio}. Actualice SMMLV_POR_ANIO.")
    return SMMLV_POR_ANIO[anio]


def cuantias(anio, presupuesto_smmlv):
    s = smmlv(anio)
    tope_menor = next(t for piso, t in ESCALA_MENOR_CUANTIA if presupuesto_smmlv >= piso)
    menor = tope_menor * s
    minima = menor * 0.10
    return {"smmlv": s, "menor_smmlv": tope_menor, "menor": menor, "minima": minima}


def restar_meses(d, meses):
    m = d.month - meses
    y = d.year
    while m <= 0:
        m += 12
        y -= 1
    dia = min(d.day, calendar.monthrange(y, m)[1])
    return date(y, m, dia)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--anio", type=int, default=date.today().year)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--presupuesto-smmlv", type=float)
    g.add_argument("--presupuesto-pesos", type=float)
    ap.add_argument("--eleccion", help="fecha de la elección AAAA-MM-DD")
    ap.add_argument("--presidencial", action="store_true")
    ap.add_argument("--adicion", action="store_true", help="verificar límite del 50 %% (art. 40 Ley 80)")
    ap.add_argument("--valor-inicial", type=float)
    ap.add_argument("--anio-inicial", type=int)
    ap.add_argument("--adiciones", nargs="*", default=[], help="lista AAAA:valor")
    a = ap.parse_args()

    hizo_algo = False
    if a.presupuesto_smmlv or a.presupuesto_pesos:
        hizo_algo = True
        s = smmlv(a.anio)
        ps = a.presupuesto_smmlv if a.presupuesto_smmlv else a.presupuesto_pesos / s
        c = cuantias(a.anio, ps)
        print(f"Año {a.anio} — SMMLV {pesos(c['smmlv'])}")
        print(f"Presupuesto: {ps:,.0f} SMMLV".replace(",", "."))
        print(f"Menor cuantía: hasta {c['menor_smmlv']} SMMLV = {pesos(c['menor'])}")
        print(f"Mínima cuantía: hasta 10 % de la menor = {pesos(c['minima'])}")
        print("Nota: confirme con la publicación oficial de cuantías de la entidad para la vigencia.")

    if a.eleccion:
        hizo_algo = True
        e = date.fromisoformat(a.eleccion)
        inicio = restar_meses(e, 4)
        print(f"\nElección: {e.isoformat()} ({['lunes','martes','miércoles','jueves','viernes','sábado','domingo'][e.weekday()]})")
        print(f"Inicio de restricciones (4 meses antes): {inicio.isoformat()}")
        if a.presidencial:
            print("- Art. 33 Ley 996: prohibida la contratación directa (con excepciones) hasta la 2.ª vuelta.")
        print("- Art. 38 parág. Ley 996: sin convenios interadministrativos para ejecutar recursos ni")
        print("  modificaciones de nómina (salvo excepciones) hasta la elección.")
        print(f"- Último día recomendado para perfeccionar convenios: {(inicio - timedelta(days=1)).isoformat()}")
        print("Verifique con la circular de Colombia Compra Eficiente para esa elección.")

    if a.adicion:
        hizo_algo = True
        if not (a.valor_inicial and a.anio_inicial):
            raise SystemExit("--adicion requiere --valor-inicial y --anio-inicial")
        vi_s = a.valor_inicial / smmlv(a.anio_inicial)
        total_s = 0.0
        for item in a.adiciones:
            anio, valor = item.split(":")
            total_s += float(valor) / smmlv(int(anio))
        pct = total_s / vi_s * 100
        print(f"\nValor inicial: {vi_s:,.2f} SMMLV ({a.anio_inicial})".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"Adiciones acumuladas: {total_s:,.2f} SMMLV".replace(",", "X").replace(".", ",").replace("X", "."))
        estado = "DENTRO" if pct <= 50 else "EXCEDE"
        print(f"Porcentaje: {pct:.2f}".replace(".", ",") + f" % — {estado} del límite del 50 % (Ley 80, art. 40 parág.)")
        print("Reglas especiales: interventoría prorrogada con el contrato vigilado (Ley 1474, art. 85), APP, emergencia (Decreto 1420 de 2026).")

    if not hizo_algo:
        ap.print_help()


if __name__ == "__main__":
    main()
