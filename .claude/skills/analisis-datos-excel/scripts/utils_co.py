"""Utilidades para datos colombianos en Excel/CSV: números con formato local, encabezados, columnas."""
import re
import unicodedata

import pandas as pd

_RE_LIMPIO = re.compile(r"[^\d,.\-()]")


def quitar_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", str(s)) if unicodedata.category(c) != "Mn")


def normalizar_nombre(col):
    """'Apropiación Definitiva ($)' -> 'apropiacion_definitiva'"""
    s = quitar_tildes(str(col)).lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s or "columna"


def a_numero(valor):
    """Convierte '$ 1.234.567,89', '1,234,567.89', '(1.500)', '12,5 %', 1234 -> float. None si no es número."""
    if valor is None:
        return None
    if isinstance(valor, (int, float)) and not isinstance(valor, bool):
        return None if pd.isna(valor) else float(valor)
    s = str(valor).strip()
    if not s or s.lower() in ("nan", "none", "-", "n/a", "na", "s.d."):
        return None
    pct = s.endswith("%")
    negativo = s.startswith("(") and s.endswith(")") or s.startswith("-")
    s = _RE_LIMPIO.sub("", s).replace("(", "").replace(")", "").replace("-", "")
    if not s or not any(ch.isdigit() for ch in s):
        return None
    if "," in s and "." in s:
        # el último separador es el decimal
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        partes = s.split(",")
        if len(partes) > 2 and any(len(p) != 3 for p in partes[1:]):
            return None  # p. ej. códigos '1,2,3'
        # '1,5' decimal; '1,234,567' miles
        s = s.replace(",", "") if all(len(p) == 3 for p in partes[1:]) and len(partes) > 2 else s.replace(",", ".")
    elif "." in s:
        partes = s.split(".")
        if len(partes) > 2 and any(len(p) != 3 for p in partes[1:]):
            return None  # códigos presupuestales '2.3.1.02' o fechas '1.2.2026'
        if len(partes) > 2 or (len(partes) == 2 and len(partes[1]) == 3 and len(partes[0]) <= 3):
            # '1.234.567' o '1.234' -> miles (ambiguo: '1.234' se asume miles en formato colombiano)
            s = s.replace(".", "")
    try:
        n = float(s)
    except ValueError:
        return None
    n = -n if negativo else n
    return n / 100 if pct else n


def columna_numerica(serie, umbral=0.8):
    """True si al menos `umbral` de los valores no vacíos se convierten a número."""
    vals = serie.dropna()
    vals = vals[vals.astype(str).str.strip() != ""]
    if len(vals) == 0:
        return False
    ok = sum(a_numero(v) is not None for v in vals)
    return ok / len(vals) >= umbral


def detectar_fila_encabezado(df_crudo, max_filas=20):
    """Devuelve el índice de la fila que parece encabezado (más celdas de texto no vacías)."""
    mejor, puntaje_max = 0, -1
    for i in range(min(max_filas, len(df_crudo))):
        fila = df_crudo.iloc[i]
        texto = sum(isinstance(v, str) and v.strip() != "" and a_numero(v) is None for v in fila)
        llenas = fila.notna().sum()
        puntaje = texto * 2 + llenas
        if texto >= 2 and puntaje > puntaje_max:
            mejor, puntaje_max = i, puntaje
    return mejor


def leer_tabla(ruta, hoja=0, fila_encabezado=None):
    """Lee Excel/CSV detectando la fila de encabezado. Devuelve (df, fila_encabezado)."""
    ruta = str(ruta)
    if ruta.lower().endswith((".csv", ".txt")):
        crudo = pd.read_csv(ruta, header=None, dtype=object, sep=None, engine="python", encoding_errors="replace")
    else:
        crudo = pd.read_excel(ruta, sheet_name=hoja, header=None, dtype=object)
    if fila_encabezado is None:
        fila_encabezado = detectar_fila_encabezado(crudo)
    enc = [str(c).strip() if pd.notna(c) else f"col_{i}" for i, c in enumerate(crudo.iloc[fila_encabezado])]
    df = crudo.iloc[fila_encabezado + 1:].copy()
    df.columns = enc
    df = df.dropna(how="all").dropna(axis=1, how="all")
    return df.reset_index(drop=True), fila_encabezado


def pesos(v, decimales=0):
    if v is None or pd.isna(v):
        return ""
    s = f"{v:,.{decimales}f}"
    return "$ " + s.replace(",", "X").replace(".", ",").replace("X", ".")


def numero(v, decimales=0):
    if v is None or pd.isna(v):
        return ""
    return f"{v:,.{decimales}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def porcentaje(v, decimales=1):
    if v is None or pd.isna(v):
        return ""
    return f"{v * 100:.{decimales}f}".replace(".", ",") + " %"
