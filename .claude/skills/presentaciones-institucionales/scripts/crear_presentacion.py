#!/usr/bin/env python3
"""
Genera una presentación .pptx 16:9 con la identidad de la Gobernación de Antioquia.

Uso:
    python crear_presentacion.py guion.json salida.pptx [--escudo ruta.png]

Requisitos: python-pptx (pip install python-pptx). Fuente Poppins instalada en el equipo que
abra el archivo (si no está, PowerPoint la sustituye; el manual permite Arial como respaldo).

Esquema del JSON:
{
  "titulo": "Avance del plan de acción 2026",
  "subtitulo": "Comité directivo",
  "dependencia": "Secretaría de Infraestructura Física",
  "fecha": "Noviembre de 2026",
  "diapositivas": [
    {"tipo": "seccion", "titulo": "1. Contexto"},
    {"tipo": "contenido", "titulo": "Mensaje principal de la diapositiva",
     "vinetas": ["Punto 1", "Punto 2"], "fuente": "Fuente: ..."},
    {"tipo": "kpis", "titulo": "...", "items": [{"valor": "78 %", "etiqueta": "Ejecución"}], "fuente": "..."},
    {"tipo": "tabla", "titulo": "...", "encabezados": [...], "filas": [[...]], "fuente": "..."},
    {"tipo": "grafico", "titulo": "...", "grafico": "columnas|barras|lineas",
     "categorias": ["Ene", "Feb"], "series": [{"nombre": "Meta", "valores": [1, 2]}],
     "formato_numero": "0%|#,##0|0.0", "fuente": "..."},
    {"tipo": "dos_columnas", "titulo": "...", "izquierda": {"subtitulo": "...", "vinetas": []},
     "derecha": {"subtitulo": "...", "vinetas": []}},
    {"tipo": "cierre", "titulo": "Decisiones requeridas", "vinetas": ["..."]}
  ]
}
Cada diapositiva acepta "notas" (texto para el presentador).
"""
import argparse
import json
from pathlib import Path

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

VERDE = RGBColor(0x01, 0x8D, 0x38)
VERDE_OSCURO = RGBColor(0x0B, 0x56, 0x40)
MENTA = RGBColor(0x3A, 0xF9, 0xA2)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
TEXTO = RGBColor(0x1F, 0x29, 0x33)
GRIS = RGBColor(0x52, 0x60, 0x6D)
LINEA = RGBColor(0xD9, 0xDE, 0xE3)
FONDO_SUAVE = RGBColor(0xF2, 0xF7, 0xF4)
SERIES = ["018D38", "3561AB", "F28E18", "8B4A97", "B0942B", "8FCAF0", "0B5640"]
FUENTE = "Poppins"

ANCHO, ALTO = Inches(13.333), Inches(7.5)
MARGEN = Inches(0.6)

SCRIPT_DIR = Path(__file__).resolve().parent
ESCUDO_CANDIDATOS = [
    SCRIPT_DIR.parent.parent / "marca-gobernacion" / "assets" / "escudo" / "escudo-color.png",
    SCRIPT_DIR.parent / "assets" / "escudo-color.png",
    # Respaldo: PNG oficial del portal antioquia.gov.co en resolución de pantalla (157 x 70 px).
    SCRIPT_DIR.parent.parent / "marca-gobernacion" / "assets" / "escudo" / "escudo-color-pantalla.png",
]


def texto(slide, x, y, w, h, contenido, tam=18, color=TEXTO, negrita=False, alin=PP_ALIGN.LEFT,
          anclaje=MSO_ANCHOR.TOP):
    caja = slide.shapes.add_textbox(x, y, w, h)
    tf = caja.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anclaje
    tf.margin_left = tf.margin_right = Inches(0.05)
    lineas = contenido if isinstance(contenido, list) else [contenido]
    for i, linea in enumerate(lineas):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = alin
        r = p.add_run()
        r.text = str(linea)
        r.font.name = FUENTE
        r.font.size = Pt(tam)
        r.font.bold = negrita
        r.font.color.rgb = color
    return caja


def rect(slide, x, y, w, h, color, forma=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(forma, x, y, w, h)
    s.fill.solid()
    s.fill.fore_color.rgb = color
    s.line.fill.background()
    s.shadow.inherit = False
    return s


def escudo(slide, ruta, x, y, alto, contenedor=False):
    """Ubica el escudo oficial; si no existe, deja un marcador. En fondo de color usa contenedor blanco."""
    ancho = Emu(int(alto * 2.2))
    if contenedor:
        c = rect(slide, x - Inches(0.12), y - Inches(0.08), ancho + Inches(0.24), alto + Inches(0.16),
                 BLANCO, MSO_SHAPE.ROUNDED_RECTANGLE)
        c.adjustments[0] = 0.12
    if ruta:
        pic = slide.shapes.add_picture(str(ruta), x, y, height=alto)
        return pic
    m = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, ancho, alto)
    m.fill.background()
    m.line.color.rgb = GRIS
    m.line.dash_style = 4
    tf = m.text_frame
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    r = tf.paragraphs[0].add_run()
    r.text = "ESCUDO OFICIAL"
    r.font.size = Pt(9)
    r.font.name = FUENTE
    r.font.color.rgb = GRIS
    return m


def vinetas(slide, x, y, w, h, items, tam=20):
    caja = slide.shapes.add_textbox(x, y, w, h)
    tf = caja.text_frame
    tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(10)
        nivel = 1 if str(it).startswith("  ") else 0
        p.level = nivel
        r1 = p.add_run()
        r1.text = ("–  " if nivel else "■  ")
        r1.font.size = Pt(tam - 8 if not nivel else tam - 4)
        r1.font.color.rgb = VERDE
        r1.font.name = FUENTE
        r2 = p.add_run()
        r2.text = str(it).strip()
        r2.font.size = Pt(tam - (3 if nivel else 0))
        r2.font.color.rgb = TEXTO if not nivel else GRIS
        r2.font.name = FUENTE
    return caja


class Generador:
    def __init__(self, guion, ruta_escudo):
        self.g = guion
        self.esc = ruta_escudo
        self.prs = Presentation()
        self.prs.slide_width, self.prs.slide_height = ANCHO, ALTO
        self.blank = self.prs.slide_layouts[6]
        self.n = 0

    def nueva(self, notas=None):
        s = self.prs.slides.add_slide(self.blank)
        self.n += 1
        if notas:
            s.notes_slide.notes_text_frame.text = notas
        return s

    def marco(self, s, titulo, fuente=None):
        rect(s, 0, 0, ANCHO, Inches(0.12), VERDE_OSCURO)
        texto(s, MARGEN, Inches(0.4), ANCHO - 2 * MARGEN, Inches(1.0), titulo, tam=28,
              color=VERDE_OSCURO, negrita=True, anclaje=MSO_ANCHOR.MIDDLE)
        rect(s, MARGEN, Inches(1.45), Inches(1.2), Inches(0.06), VERDE)
        # pie
        texto(s, MARGEN, ALTO - Inches(0.5), Inches(8), Inches(0.3),
              self.g.get("dependencia", "Gobernación de Antioquia"), tam=10, color=GRIS)
        texto(s, ANCHO - MARGEN - Inches(2.6), ALTO - Inches(0.5), Inches(0.5), Inches(0.3),
              str(self.n), tam=10, color=GRIS, alin=PP_ALIGN.RIGHT)
        escudo(s, self.esc, ANCHO - MARGEN - Inches(1.85), ALTO - Inches(0.85), Inches(0.7))
        if fuente:
            texto(s, MARGEN, ALTO - Inches(0.9), Inches(9.5), Inches(0.35), fuente, tam=10, color=GRIS)

    # ---- tipos ----
    def portada(self):
        s = self.nueva()
        rect(s, 0, 0, ANCHO, ALTO, VERDE_OSCURO)
        rect(s, MARGEN, Inches(2.2), Inches(0.12), Inches(2.2), MENTA)
        texto(s, MARGEN + Inches(0.4), Inches(2.0), Inches(10.5), Inches(1.9), self.g.get("titulo", ""),
              tam=40, color=BLANCO, negrita=True, anclaje=MSO_ANCHOR.BOTTOM)
        sub = [x for x in (self.g.get("subtitulo"), self.g.get("dependencia"), self.g.get("fecha")) if x]
        if sub:
            texto(s, MARGEN + Inches(0.4), Inches(4.0), Inches(10), Inches(1.4), sub, tam=18, color=BLANCO)
        escudo(s, self.esc, ANCHO - MARGEN - Inches(2.2), ALTO - Inches(1.4), Inches(0.9), contenedor=True)

    def seccion(self, d):
        s = self.nueva(d.get("notas"))
        rect(s, 0, 0, ANCHO, ALTO, VERDE)
        texto(s, MARGEN, Inches(2.6), ANCHO - 2 * MARGEN, Inches(1.6), d.get("titulo", ""), tam=40,
              color=BLANCO, negrita=True, anclaje=MSO_ANCHOR.MIDDLE)
        if d.get("subtitulo"):
            texto(s, MARGEN, Inches(4.2), ANCHO - 2 * MARGEN, Inches(0.8), d["subtitulo"], tam=18, color=BLANCO)

    def contenido(self, d):
        s = self.nueva(d.get("notas"))
        self.marco(s, d.get("titulo", ""), d.get("fuente"))
        vinetas(s, MARGEN, Inches(1.8), ANCHO - 2 * MARGEN, Inches(4.6), d.get("vinetas", []),
                tam=d.get("tam", 20))

    def dos_columnas(self, d):
        s = self.nueva(d.get("notas"))
        self.marco(s, d.get("titulo", ""), d.get("fuente"))
        ancho_col = (ANCHO - 2 * MARGEN - Inches(0.5)) / 2
        for i, lado in enumerate(("izquierda", "derecha")):
            col = d.get(lado, {})
            x = MARGEN + i * (ancho_col + Inches(0.5))
            rect(s, x, Inches(1.8), ancho_col, Inches(4.5), FONDO_SUAVE)
            texto(s, x + Inches(0.25), Inches(1.95), ancho_col - Inches(0.5), Inches(0.6),
                  col.get("subtitulo", ""), tam=20, color=VERDE, negrita=True)
            vinetas(s, x + Inches(0.25), Inches(2.6), ancho_col - Inches(0.5), Inches(3.6),
                    col.get("vinetas", []), tam=16)

    def kpis(self, d):
        s = self.nueva(d.get("notas"))
        self.marco(s, d.get("titulo", ""), d.get("fuente"))
        items = d.get("items", [])[:4]
        if not items:
            return
        sep = Inches(0.35)
        w = (ANCHO - 2 * MARGEN - sep * (len(items) - 1)) / len(items)
        for i, it in enumerate(items):
            x = MARGEN + i * (w + sep)
            rect(s, x, Inches(2.2), w, Inches(3.0), FONDO_SUAVE)
            rect(s, x, Inches(2.2), w, Inches(0.1), VERDE)
            texto(s, x, Inches(2.6), w, Inches(1.4), it.get("valor", ""), tam=48, color=VERDE_OSCURO,
                  negrita=True, alin=PP_ALIGN.CENTER, anclaje=MSO_ANCHOR.MIDDLE)
            texto(s, x + Inches(0.2), Inches(4.0), w - Inches(0.4), Inches(1.0), it.get("etiqueta", ""),
                  tam=16, color=GRIS, alin=PP_ALIGN.CENTER)

    def tabla(self, d):
        s = self.nueva(d.get("notas"))
        self.marco(s, d.get("titulo", ""), d.get("fuente"))
        enc, filas = d.get("encabezados", []), d.get("filas", [])
        nfil, ncol = len(filas) + 1, len(enc)
        alto_fila = Inches(0.42)
        shp = s.shapes.add_table(nfil, ncol, MARGEN, Inches(1.8), ANCHO - 2 * MARGEN, alto_fila * nfil)
        t = shp.table
        tam = 14 if nfil <= 8 else 11
        for j, h in enumerate(enc):
            c = t.cell(0, j)
            c.fill.solid()
            c.fill.fore_color.rgb = VERDE_OSCURO
            c.text = str(h)
            p = c.text_frame.paragraphs[0]
            p.font.size, p.font.bold, p.font.color.rgb, p.font.name = Pt(tam), True, BLANCO, FUENTE
        for i, f in enumerate(filas, start=1):
            for j, v in enumerate(f):
                c = t.cell(i, j)
                c.fill.solid()
                c.fill.fore_color.rgb = FONDO_SUAVE if i % 2 == 0 else BLANCO
                c.text = str(v)
                p = c.text_frame.paragraphs[0]
                p.font.size, p.font.color.rgb, p.font.name = Pt(tam), TEXTO, FUENTE
                if str(v).replace(".", "").replace(",", "").replace("%", "").replace("$", "").strip().lstrip("-").isdigit():
                    p.alignment = PP_ALIGN.RIGHT

    def grafico(self, d):
        s = self.nueva(d.get("notas"))
        self.marco(s, d.get("titulo", ""), d.get("fuente"))
        tipos = {"columnas": XL_CHART_TYPE.COLUMN_CLUSTERED, "barras": XL_CHART_TYPE.BAR_CLUSTERED,
                 "lineas": XL_CHART_TYPE.LINE_MARKERS, "columnas_apiladas": XL_CHART_TYPE.COLUMN_STACKED}
        cd = CategoryChartData()
        cd.categories = d.get("categorias", [])
        for se in d.get("series", []):
            cd.add_series(se.get("nombre", ""), se.get("valores", []))
        gf = s.shapes.add_chart(tipos.get(d.get("grafico", "columnas"), XL_CHART_TYPE.COLUMN_CLUSTERED),
                                MARGEN, Inches(1.7), ANCHO - 2 * MARGEN, Inches(4.6), cd)
        ch = gf.chart
        ch.font.name = FUENTE
        ch.font.size = Pt(12)
        ch.font.color.rgb = TEXTO
        multi = len(d.get("series", [])) > 1
        ch.has_legend = multi
        if multi:
            ch.legend.position = XL_LEGEND_POSITION.TOP
            ch.legend.include_in_layout = False
        fmt = d.get("formato_numero", "#,##0")
        for i, serie in enumerate(ch.plots[0].series):
            color = RGBColor.from_string(SERIES[i % len(SERIES)])
            if d.get("grafico") == "lineas":
                serie.format.line.color.rgb = color
                serie.format.line.width = Pt(2.5)
                serie.smooth = False
            else:
                serie.format.fill.solid()
                serie.format.fill.fore_color.rgb = color
        plot = ch.plots[0]
        plot.has_data_labels = d.get("etiquetas", True)
        if plot.has_data_labels:
            plot.data_labels.number_format = fmt
            plot.data_labels.number_format_is_linked = False
            plot.data_labels.font.size = Pt(11)
            if d.get("grafico") in ("columnas", "barras"):
                plot.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
        va = ch.value_axis
        va.has_major_gridlines = True
        va.major_gridlines.format.line.color.rgb = LINEA
        va.tick_labels.number_format = fmt
        va.tick_labels.number_format_is_linked = False
        va.format.line.fill.background()
        ch.category_axis.format.line.color.rgb = LINEA
        if d.get("grafico") in ("columnas", "barras", "columnas_apiladas"):
            plot.gap_width = 80

    def cierre(self, d):
        s = self.nueva(d.get("notas"))
        rect(s, 0, 0, ANCHO, ALTO, VERDE_OSCURO)
        texto(s, MARGEN, Inches(0.8), ANCHO - 2 * MARGEN, Inches(1.0), d.get("titulo", "Gracias"),
              tam=34, color=BLANCO, negrita=True)
        if d.get("vinetas"):
            caja = vinetas(s, MARGEN, Inches(2.0), ANCHO - 2 * MARGEN - Inches(3), Inches(4.0), d["vinetas"], tam=20)
            for p in caja.text_frame.paragraphs:
                for r in p.runs[1:]:
                    r.font.color.rgb = BLANCO
                p.runs[0].font.color.rgb = MENTA
        escudo(s, self.esc, ANCHO - MARGEN - Inches(2.2), ALTO - Inches(1.4), Inches(0.9), contenedor=True)

    def construir(self, salida):
        if self.g.get("portada", True):
            self.portada()
        for d in self.g.get("diapositivas", []):
            metodo = getattr(self, d.get("tipo", "contenido"), None)
            if metodo is None or d.get("tipo") in ("construir", "nueva", "marco", "portada"):
                raise ValueError(f"Tipo de diapositiva no soportado: {d.get('tipo')}")
            metodo(d)
        self.prs.core_properties.title = self.g.get("titulo", "")
        self.prs.core_properties.author = self.g.get("dependencia", "Gobernación de Antioquia")
        self.prs.save(salida)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("json")
    ap.add_argument("salida")
    ap.add_argument("--escudo")
    a = ap.parse_args()
    guion = json.loads(Path(a.json).read_text(encoding="utf-8"))
    esc = Path(a.escudo) if a.escudo else next((p for p in ESCUDO_CANDIDATOS if p.exists()), None)
    Generador(guion, esc).construir(a.salida)
    print(f"Presentación generada: {a.salida}")


if __name__ == "__main__":
    main()
