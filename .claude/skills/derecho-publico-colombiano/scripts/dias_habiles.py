#!/usr/bin/env python3
"""
Días hábiles en Colombia (lunes a viernes, sin festivos de la Ley 51 de 1983 y Ley 37 de 1905).
Útil para términos de derechos de petición (Ley 1755 de 2015), recursos (CPACA art. 76),
publicaciones en SECOP (3 días hábiles) y plazos contractuales expresados en días hábiles.

Uso:
    python dias_habiles.py --desde 2026-11-11 --dias 15            # vencimiento: 15 días hábiles siguientes
    python dias_habiles.py --entre 2026-11-11 2026-12-15            # días hábiles transcurridos
    python dias_habiles.py --festivos 2027                          # lista de festivos
    python dias_habiles.py --desde 2026-12-20 --dias 10 --excluir 2026-12-24 2026-12-31

Regla de cómputo: el día de radicación no cuenta; se cuenta desde el día hábil siguiente
(art. 62 Ley 4 de 1913 y práctica de la Ley 1755). Si el escrito se radica en día inhábil, se entiende
recibido el día hábil siguiente. Verifique horarios de radicación de la entidad.
"""
import argparse
from datetime import date, timedelta


def pascua(anio):
    """Domingo de Pascua (algoritmo anónimo gregoriano)."""
    a = anio % 19
    b, c = divmod(anio, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mes = (h + l - 7 * m + 114) // 31
    dia = ((h + l - 7 * m + 114) % 31) + 1
    return date(anio, mes, dia)


def siguiente_lunes(d):
    return d + timedelta(days=(7 - d.weekday()) % 7)


def festivos(anio):
    fijos = {
        date(anio, 1, 1): "Año Nuevo",
        date(anio, 5, 1): "Día del Trabajo",
        date(anio, 7, 20): "Independencia",
        date(anio, 8, 7): "Batalla de Boyacá",
        date(anio, 12, 8): "Inmaculada Concepción",
        date(anio, 12, 25): "Navidad",
    }
    trasladables = {
        date(anio, 1, 6): "Reyes Magos",
        date(anio, 3, 19): "San José",
        date(anio, 6, 29): "San Pedro y San Pablo",
        date(anio, 8, 15): "Asunción de la Virgen",
        date(anio, 10, 12): "Día de la Diversidad Étnica y Cultural",
        date(anio, 11, 1): "Todos los Santos",
        date(anio, 11, 11): "Independencia de Cartagena",
    }
    p = pascua(anio)
    resultado = dict(fijos)
    for d, n in trasladables.items():
        resultado[siguiente_lunes(d)] = n
    resultado[p - timedelta(days=3)] = "Jueves Santo"
    resultado[p - timedelta(days=2)] = "Viernes Santo"
    resultado[p + timedelta(days=43)] = "Ascensión del Señor"
    resultado[p + timedelta(days=64)] = "Corpus Christi"
    resultado[p + timedelta(days=71)] = "Sagrado Corazón"
    return dict(sorted(resultado.items()))


def es_habil(d, extra=frozenset()):
    return d.weekday() < 5 and d not in festivos(d.year) and d not in extra


def sumar_habiles(desde, n, extra=frozenset()):
    d = desde
    contados = 0
    while contados < n:
        d += timedelta(days=1)
        if es_habil(d, extra):
            contados += 1
    return d


def habiles_entre(a, b, extra=frozenset()):
    """Días hábiles en (a, b] — excluye a, incluye b."""
    n, d = 0, a
    while d < b:
        d += timedelta(days=1)
        if es_habil(d, extra):
            n += 1
    return n


DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--desde")
    ap.add_argument("--dias", type=int)
    ap.add_argument("--entre", nargs=2)
    ap.add_argument("--festivos", type=int)
    ap.add_argument("--excluir", nargs="*", default=[], help="días inhábiles adicionales AAAA-MM-DD")
    a = ap.parse_args()
    extra = frozenset(date.fromisoformat(x) for x in a.excluir)

    if a.festivos:
        for d, n in festivos(a.festivos).items():
            print(f"{d.isoformat()}  {DIAS[d.weekday()]:<10} {n}")
    elif a.desde and a.dias is not None:
        d0 = date.fromisoformat(a.desde)
        venc = sumar_habiles(d0, a.dias, extra)
        aviso = "" if es_habil(d0, extra) else " (radicado en día inhábil: se entiende recibido el siguiente hábil)"
        print(f"Radicación: {d0.isoformat()} ({DIAS[d0.weekday()]}){aviso}")
        print(f"Vencimiento a {a.dias} días hábiles: {venc.isoformat()} ({DIAS[venc.weekday()]})")
    elif a.entre:
        x, y = (date.fromisoformat(v) for v in a.entre)
        print(f"Días hábiles transcurridos entre {x} (excluido) y {y} (incluido): {habiles_entre(x, y, extra)}")
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
