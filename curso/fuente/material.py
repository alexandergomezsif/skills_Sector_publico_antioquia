"""Material de consulta por módulo: normas con enlace oficial y guías de Colombia Compra Eficiente.

Enlaces verificados el 27-nov-2026:
- Gestor Normativo de Función Pública (norma.php?i=...): título de la norma comprobado en la página.
- Colombia Compra Eficiente: páginas de guías y manuales, control de versiones de Documentos Tipo, SECOP II y TVEC.
Los artículos citados orientan la lectura; verifique siempre el texto vigente en la fuente.
"""

FP = "https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i="
CCE = "https://www.colombiacompra.gov.co"

NORMAS = {
    "L80":   ("Ley 80 de 1993", "Estatuto General de Contratación de la Administración Pública", FP + "304"),
    "L1150": ("Ley 1150 de 2007", "Eficiencia y transparencia en la contratación", FP + "184686"),
    "L1474": ("Ley 1474 de 2011", "Estatuto Anticorrupción", FP + "43292"),
    "L1882": ("Ley 1882 de 2018", "Fortalecimiento de la contratación pública e infraestructura", FP + "84899"),
    "L2022": ("Ley 2022 de 2020", "Documentos Tipo obligatorios", FP + "136375"),
    "L2195": ("Ley 2195 de 2022", "Transparencia, prevención y lucha contra la corrupción", FP + "175606"),
    "L850":  ("Ley 850 de 2003", "Veedurías ciudadanas", FP + "10570"),
    "L996":  ("Ley 996 de 2005", "Ley de Garantías Electorales", FP + "18232"),
    "L1952": ("Ley 1952 de 2019", "Código General Disciplinario", FP + "90324"),
    "L1437": ("Ley 1437 de 2011", "Código de Procedimiento Administrativo (CPACA)", FP + "41249"),
    "L1712": ("Ley 1712 de 2014", "Transparencia y acceso a la información pública", FP + "56882"),
    "L1682": ("Ley 1682 de 2013", "Proyectos de infraestructura de transporte", FP + "55612"),
    "D1082": ("Decreto 1082 de 2015", "Único Reglamentario del Sector Planeación (compilación contractual)", FP + "77653"),
}

GUIAS = {
    "guias": ("Guías y manuales de Colombia Compra Eficiente", CCE + "/normativa-y-relatoria/guias-y-manuales"),
    "dt":    ("Documentos Tipo: control de versiones", CCE + "/normativa-y-relatoria/control-de-versiones-documentos-tipo"),
    "secop": ("SECOP II", CCE + "/secop/secop-ii"),
    "tvec":  ("Tienda Virtual del Estado Colombiano", CCE + "/secop/tvec"),
    "rel":   ("Relatoría de Colombia Compra Eficiente (normas y conceptos)", "https://relatoria.colombiacompra.gov.co"),
}

# Por módulo: (clave de norma, artículos que conviene leer) y guías.
MATERIAL = {
    "m1":  {"n": [("L80", "arts. 1 a 3 y 32"), ("L1150", "art. 1"), ("D1082", "Parte 2, Título 1")], "g": ["guias", "secop"]},
    "m2":  {"n": [("L80", "arts. 23 a 26"), ("L1150", "art. 5"), ("L1474", ""), ("L850", ""), ("L1712", "")], "g": ["rel"]},
    "m3":  {"n": [("L80", "arts. 6, 7, 11 y 12"), ("D1082", "")], "g": ["secop", "tvec"]},
    "m4":  {"n": [("L80", "art. 25"), ("L1474", "art. 87"), ("D1082", "arts. 2.2.1.1.1.4.1 y 2.2.1.1.2.1.1")], "g": ["guias"]},
    "m5":  {"n": [("L1150", "arts. 5 y 6"), ("D1082", "art. 2.2.1.1.1.6.3")], "g": ["guias"]},
    "m15": {"n": [("L80", "arts. 8 a 10, 44 a 48 y 50 a 58"), ("L1474", "arts. 1 a 4 y 90"), ("L1437", "art. 11"), ("L1952", ""), ("L2195", "")], "g": ["rel"]},
    "m6":  {"n": [("L1150", "art. 2"), ("L1474", "art. 94"), ("D1082", "")], "g": ["tvec", "guias"]},
    "m7":  {"n": [("L80", "art. 30"), ("L1150", ""), ("D1082", "")], "g": ["secop", "guias"]},
    "m8":  {"n": [("L1882", "art. 4"), ("L2022", "")], "g": ["dt"]},
    "m9":  {"n": [("L80", "art. 41"), ("L1150", "art. 7"), ("D1082", "art. 2.2.1.2.3.1.1 y siguientes")], "g": ["guias"]},
    "m10": {"n": [("L80", "arts. 14 a 19"), ("L1474", "arts. 83 y 84"), ("D1082", "")], "g": ["guias"]},
    "m11": {"n": [("L80", "arts. 17 y 18"), ("L1150", "art. 17"), ("L1474", "art. 86"), ("L1437", "")], "g": ["rel"]},
    "m12": {"n": [("L80", "art. 60"), ("L1150", "art. 11"), ("L1437", "art. 164")], "g": ["guias", "secop"]},
    "m13": {"n": [("L1682", ""), ("L1882", ""), ("L1474", "art. 83")], "g": ["dt"]},
    "m14": {"n": [("D1082", "con sus modificaciones de 2026 (Decretos 287 y 0997)"), ("L996", "art. 38, parágrafo")], "g": ["rel", "dt"]},
}


def para_pagina(ids):
    """Devuelve la estructura que usa la página: {id: {normas:[[t,d,url,art]], guias:[[t,url]]}}."""
    assert set(ids) == set(MATERIAL), set(ids) ^ set(MATERIAL)
    out = {}
    for mid in ids:
        m = MATERIAL[mid]
        out[mid] = {
            "normas": [[*NORMAS[k], art] for k, art in m["n"]],
            "guias": [list(GUIAS[g]) for g in m["g"]],
        }
    return out
