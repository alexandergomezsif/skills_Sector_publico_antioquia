#!/usr/bin/env python3
"""
Genera un informe institucional .docx con la identidad de la Gobernación de Antioquia.

Uso:
    python crear_informe.py contenido.json salida.docx [--escudo ruta.png]

Requisitos: python-docx (pip install python-docx)

Esquema del JSON (todos los campos opcionales salvo "titulo" y "bloques"):
{
  "dependencia": "Secretaría de Hacienda",          # va en el encabezado
  "titulo": "Informe de ejecución presupuestal",
  "subtitulo": "Tercer trimestre de 2026",
  "fecha": "15 de octubre de 2026",
  "lugar": "Medellín",
  "periodo": "1 de enero a 30 de septiembre de 2026",
  "fecha_corte": "30 de septiembre de 2026",
  "clasificacion": "Información pública",            # Ley 1712: pública / clasificada / reservada
  "portada": true,                                    # portada en página aparte
  "bloques": [
    {"tipo": "h1", "texto": "1. Resumen ejecutivo"},
    {"tipo": "h2", "texto": "1.1 Subtítulo"},
    {"tipo": "p", "texto": "Texto con **negritas** en línea."},
    {"tipo": "vinetas", "items": ["uno", "dos"]},
    {"tipo": "numerada", "items": ["paso 1", "paso 2"]},
    {"tipo": "kpis", "items": [{"valor": "78 %", "etiqueta": "Ejecución"}]},
    {"tipo": "tabla", "encabezados": ["A", "B"], "filas": [["1", "2"]],
     "anchos_cm": [8, 8], "alineacion": ["izq", "der"], "total": ["Total", "2"],
     "nota": "Fuente: ..."},
    {"tipo": "alerta", "nivel": "alto|medio|bajo", "texto": "..."},
    {"tipo": "imagen", "ruta": "grafico.png", "ancho_cm": 15, "pie": "Gráfico 1. ..."},
    {"tipo": "salto"}
  ],
  "firmas": [{"nombre": "NOMBRE", "cargo": "Cargo", "dependencia": "..."}],
  "control": [{"rol": "Proyectó", "nombre": "...", "cargo": "..."}],
  "aviso_ia": true
}
"""
import argparse
import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

VERDE = RGBColor(0x01, 0x8D, 0x38)
VERDE_OSCURO = RGBColor(0x0B, 0x56, 0x40)
TEXTO = RGBColor(0x1F, 0x29, 0x33)
GRIS = RGBColor(0x52, 0x60, 0x6D)
FUENTE = "Arial"  # Manual de Identidad: Arial 12 para documentos
NIVELES = {"alto": "C62828", "medio": "F28E18", "bajo": "018D38"}

SCRIPT_DIR = Path(__file__).resolve().parent
ESCUDO_CANDIDATOS = [
    SCRIPT_DIR.parent.parent / "marca-gobernacion" / "assets" / "escudo" / "escudo-color.png",
    SCRIPT_DIR.parent / "assets" / "escudo-color.png",
    # Respaldo: PNG oficial del portal antioquia.gov.co en resolución de pantalla (157 x 70 px).
    SCRIPT_DIR.parent.parent / "marca-gobernacion" / "assets" / "escudo" / "escudo-color-pantalla.png",
]


# ---------- utilidades XML ----------
def sombrear(celda, hex_color):
    tcPr = celda._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def bordes_celda(celda, color="D9DEE3", tam=4):
    tcPr = celda._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for lado in ("top", "left", "bottom", "right"):
        b = OxmlElement(f"w:{lado}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), str(tam))
        b.set(qn("w:color"), color)
        borders.append(b)
    tcPr.append(borders)


def borde_parrafo(parrafo, lado="bottom", color="018D38", tam=12):
    pPr = parrafo._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    b = OxmlElement(f"w:{lado}")
    b.set(qn("w:val"), "single")
    b.set(qn("w:sz"), str(tam))
    b.set(qn("w:space"), "4")
    b.set(qn("w:color"), color)
    pbdr.append(b)
    pPr.append(pbdr)


def campo(parrafo, instruccion):
    """Inserta un campo de Word (PAGE, NUMPAGES)."""
    run = parrafo.add_run()
    for tipo, texto in (("begin", None), (None, instruccion), ("end", None)):
        if tipo:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), tipo)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = texto
        run._r.append(el)
    return run


def repetir_encabezado(fila):
    trPr = fila._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    trPr.append(el)


def no_partir_fila(fila):
    trPr = fila._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    el.set(qn("w:val"), "true")
    trPr.append(el)


# ---------- texto con **negritas** ----------
PATRON_NEGRITA = re.compile(r"(\*\*[^*]+\*\*)")


def agregar_texto(parrafo, texto, tam=12, color=TEXTO, negrita=False):
    for trozo in PATRON_NEGRITA.split(str(texto)):
        if not trozo:
            continue
        es_neg = trozo.startswith("**") and trozo.endswith("**")
        run = parrafo.add_run(trozo[2:-2] if es_neg else trozo)
        run.font.name = FUENTE
        run.font.size = Pt(tam)
        run.font.color.rgb = color
        run.bold = negrita or es_neg
    return parrafo


# ---------- estilos ----------
def configurar_estilos(doc):
    st = doc.styles
    normal = st["Normal"]
    normal.font.name = FUENTE
    normal.font.size = Pt(12)
    normal.font.color.rgb = TEXTO
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FUENTE)
    pf = normal.paragraph_format
    pf.space_after = Pt(6)
    pf.line_spacing = 1.15

    for nombre, tam, color, antes, despues in (
        ("Title", 22, VERDE_OSCURO, 0, 6),
        ("Heading 1", 15, VERDE_OSCURO, 18, 6),
        ("Heading 2", 13, VERDE, 12, 4),
        ("Heading 3", 12, VERDE_OSCURO, 10, 4),
    ):
        s = st[nombre]
        s.font.name = FUENTE
        s.font.size = Pt(tam)
        s.font.bold = True
        s.font.color.rgb = color
        rpr = s.element.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts")
            rpr.append(rfonts)
        for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            if rfonts.get(qn(a)) is not None:
                del rfonts.attrib[qn(a)]
        for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            rfonts.set(qn(a), FUENTE)
        s.paragraph_format.space_before = Pt(antes)
        s.paragraph_format.space_after = Pt(despues)
        s.paragraph_format.keep_with_next = True


def configurar_pagina(seccion):
    seccion.page_width = Cm(21.59)   # carta
    seccion.page_height = Cm(27.94)
    seccion.top_margin = Cm(3.0)
    seccion.bottom_margin = Cm(2.5)
    seccion.left_margin = Cm(2.5)
    seccion.right_margin = Cm(2.5)
    seccion.header_distance = Cm(1.0)
    seccion.footer_distance = Cm(1.0)


def encabezado_pie(seccion, datos, escudo):
    h = seccion.header
    p = h.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if escudo:
        p.add_run().add_picture(str(escudo), width=Cm(3.5))  # mínimo impreso del manual
    else:
        r = p.add_run("[ ESCUDO OFICIAL ]")
        r.font.name = FUENTE
        r.font.size = Pt(9)
        r.font.color.rgb = GRIS
        r.bold = True
        p2 = h.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        agregar_texto(p2, "GOBERNACIÓN DE ANTIOQUIA", tam=9, color=VERDE_OSCURO, negrita=True)
    if datos.get("dependencia"):
        p3 = h.add_paragraph()
        p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        agregar_texto(p3, datos["dependencia"], tam=9, color=GRIS)
        borde_parrafo(p3, color="018D38", tam=8)

    f = seccion.footer
    pf = f.paragraphs[0]
    pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for parte in ("Página ", None, " de ", "NUMPAGES"):
        if parte is None:
            r = campo(pf, "PAGE")
        elif parte == "NUMPAGES":
            r = campo(pf, "NUMPAGES")
        else:
            r = pf.add_run(parte)
        r.font.name = FUENTE
        r.font.size = Pt(8)
        r.font.color.rgb = GRIS
    if datos.get("clasificacion"):
        pc = f.add_paragraph()
        pc.alignment = WD_ALIGN_PARAGRAPH.CENTER
        agregar_texto(pc, datos["clasificacion"], tam=8, color=GRIS)


# ---------- bloques ----------
def bloque_tabla(doc, b, ancho_util):
    enc = b.get("encabezados", [])
    filas = b.get("filas", [])
    total = b.get("total")
    ncol = len(enc) or (len(filas[0]) if filas else 0)
    if ncol == 0:
        return
    anchos = b.get("anchos_cm") or [ancho_util / ncol] * ncol
    escala = ancho_util / sum(anchos) if sum(anchos) > ancho_util else 1
    anchos = [a * escala for a in anchos]
    alin = b.get("alineacion") or ["izq"] * ncol
    mapa = {"izq": WD_ALIGN_PARAGRAPH.LEFT, "der": WD_ALIGN_PARAGRAPH.RIGHT, "cen": WD_ALIGN_PARAGRAPH.CENTER}

    t = doc.add_table(rows=0, cols=ncol)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False

    def llenar(fila_datos, tipo):
        fila = t.add_row()
        no_partir_fila(fila)
        for i, valor in enumerate(fila_datos):
            c = fila.cells[i]
            c.width = Cm(anchos[i])
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            bordes_celda(c)
            par = c.paragraphs[0]
            par.paragraph_format.space_after = Pt(0)
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER if tipo == "enc" else mapa.get(alin[i], WD_ALIGN_PARAGRAPH.LEFT)
            if tipo == "enc":
                sombrear(c, "0B5640")
                agregar_texto(par, valor, tam=9, color=RGBColor(0xFF, 0xFF, 0xFF), negrita=True)
            elif tipo == "total":
                sombrear(c, "E6F2EA")
                agregar_texto(par, valor, tam=9, negrita=True)
            else:
                agregar_texto(par, valor, tam=9)
        return fila

    for i, col in enumerate(t.columns):
        col.width = Cm(anchos[i])
    if enc:
        repetir_encabezado(llenar(enc, "enc"))
    for i, fd in enumerate(filas):
        fila = llenar([str(x) for x in fd], "dato")
        if i % 2 == 1:
            for c in fila.cells:
                sombrear(c, "F2F7F4")
    if total:
        llenar([str(x) for x in total], "total")
    if b.get("nota"):
        pn = doc.add_paragraph()
        pn.paragraph_format.space_before = Pt(3)
        agregar_texto(pn, b["nota"], tam=8, color=GRIS)
    else:
        doc.add_paragraph().paragraph_format.space_after = Pt(2)


def bloque_kpis(doc, b, ancho_util):
    items = b.get("items", [])[:4]
    if not items:
        return
    t = doc.add_table(rows=2, cols=len(items))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, it in enumerate(items):
        for fila in (0, 1):
            c = t.cell(fila, i)
            c.width = Cm(ancho_util / len(items))
            sombrear(c, "F2F7F4")
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(2)
            if fila == 0:
                agregar_texto(p, it.get("valor", ""), tam=20, color=VERDE, negrita=True)
            else:
                agregar_texto(p, it.get("etiqueta", ""), tam=9, color=GRIS)
    doc.add_paragraph()


def bloque_alerta(doc, b, ancho_util):
    nivel = b.get("nivel", "medio").lower()
    t = doc.add_table(rows=1, cols=1)
    c = t.cell(0, 0)
    c.width = Cm(ancho_util)
    sombrear(c, "FFF8EC" if nivel == "medio" else ("FDECEC" if nivel == "alto" else "E6F2EA"))
    tcPr = c._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), "36")
    left.set(qn("w:color"), NIVELES.get(nivel, "F28E18"))
    borders.append(left)
    tcPr.append(borders)
    p = c.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    agregar_texto(p, f"Alerta (nivel {nivel}): ", tam=10, negrita=True)
    agregar_texto(p, b.get("texto", ""), tam=10)
    doc.add_paragraph()


def bloque_lista(doc, b, numerada):
    estilo = "List Number" if numerada else "List Bullet"
    for it in b.get("items", []):
        p = doc.add_paragraph(style=estilo)
        p.paragraph_format.space_after = Pt(3)
        agregar_texto(p, it)


def portada(doc, d):
    for _ in range(6):
        doc.add_paragraph()
    p = doc.add_paragraph(style="Title")
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.add_run(d.get("titulo", ""))
    if d.get("subtitulo"):
        ps = doc.add_paragraph()
        agregar_texto(ps, d["subtitulo"], tam=14, color=VERDE)
    pl = doc.add_paragraph()
    borde_parrafo(pl, color="018D38", tam=18)
    for etiqueta, clave in (("Dependencia", "dependencia"), ("Periodo", "periodo"),
                            ("Fecha de corte", "fecha_corte"), ("Fecha", "fecha")):
        if d.get(clave):
            pp = doc.add_paragraph()
            agregar_texto(pp, f"**{etiqueta}:** {d[clave]}", tam=11, color=GRIS)
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def firmas(doc, d):
    if d.get("firmas"):
        doc.add_paragraph()
        doc.add_paragraph()
        n = len(d["firmas"])
        t = doc.add_table(rows=1, cols=n)
        for i, f in enumerate(d["firmas"]):
            c = t.cell(0, i)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            agregar_texto(p, "_" * 30, tam=10)
            for linea, neg in ((f.get("nombre", "[COMPLETAR: nombre]"), True),
                               (f.get("cargo", ""), False), (f.get("dependencia", ""), False)):
                if linea:
                    pl = c.add_paragraph()
                    pl.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    pl.paragraph_format.space_after = Pt(0)
                    agregar_texto(pl, linea, tam=10, negrita=neg)
    if d.get("control"):
        doc.add_paragraph()
        for c in d["control"]:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(0)
            agregar_texto(p, f"{c.get('rol', '')}: {c.get('nombre', '')} – {c.get('cargo', '')}", tam=8, color=GRIS)
    if d.get("aviso_ia"):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        agregar_texto(p, "Borrador elaborado con apoyo de IA; requiere revisión y firma del servidor competente.",
                      tam=8, color=GRIS)


def construir(d, salida, escudo=None):
    if escudo is None:
        escudo = next((p for p in ESCUDO_CANDIDATOS if p.exists()), None)
    doc = Document()
    configurar_estilos(doc)
    sec = doc.sections[0]
    configurar_pagina(sec)
    encabezado_pie(sec, d, escudo)
    ancho_util = 21.59 - 5.0

    if d.get("portada", True):
        portada(doc, d)
    else:
        p = doc.add_paragraph(style="Title")
        p.add_run(d.get("titulo", ""))
        if d.get("subtitulo"):
            agregar_texto(doc.add_paragraph(), d["subtitulo"], tam=13, color=VERDE)
        if d.get("lugar") or d.get("fecha"):
            agregar_texto(doc.add_paragraph(), ", ".join(x for x in (d.get("lugar"), d.get("fecha")) if x),
                          tam=11, color=GRIS)

    for b in d.get("bloques", []):
        tipo = b.get("tipo")
        if tipo in ("h1", "h2", "h3"):
            doc.add_heading(b.get("texto", ""), level=int(tipo[1]))
        elif tipo == "p":
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if b.get("justificar") else WD_ALIGN_PARAGRAPH.LEFT
            agregar_texto(p, b.get("texto", ""))
        elif tipo == "vinetas":
            bloque_lista(doc, b, False)
        elif tipo == "numerada":
            bloque_lista(doc, b, True)
        elif tipo == "tabla":
            bloque_tabla(doc, b, ancho_util)
        elif tipo == "kpis":
            bloque_kpis(doc, b, ancho_util)
        elif tipo == "alerta":
            bloque_alerta(doc, b, ancho_util)
        elif tipo == "imagen":
            ruta = Path(b.get("ruta", ""))
            if ruta.exists():
                doc.add_picture(str(ruta), width=Cm(min(b.get("ancho_cm", 15), ancho_util)))
                doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                agregar_texto(doc.add_paragraph(), f"[COMPLETAR: imagen {ruta}]", color=GRIS)
            if b.get("pie"):
                pp = doc.add_paragraph()
                pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                agregar_texto(pp, b["pie"], tam=9, color=GRIS)
        elif tipo == "salto":
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        else:
            print(f"Aviso: bloque desconocido '{tipo}' omitido", file=sys.stderr)

    firmas(doc, d)
    doc.core_properties.title = d.get("titulo", "")
    doc.core_properties.author = d.get("dependencia", "Gobernación de Antioquia")
    doc.save(salida)
    return salida


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("json")
    ap.add_argument("salida")
    ap.add_argument("--escudo", help="ruta a escudo oficial PNG")
    a = ap.parse_args()
    datos = json.loads(Path(a.json).read_text(encoding="utf-8"))
    esc = Path(a.escudo) if a.escudo else None
    construir(datos, a.salida, esc)
    print(f"Informe generado: {a.salida}")


if __name__ == "__main__":
    main()
