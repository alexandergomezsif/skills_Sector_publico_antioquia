"""Genera las memorias del curso (HTML -> PDF con Chrome)."""
import base64, copy, sys, asyncio, re, hashlib
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI / 'fuente'))
CHROME = sys.argv[1] if len(sys.argv) > 1 else None  # ruta opcional a Chrome
from contenido import GLOSARIO as GLOS_BASE, PLAZOS
from contenido2 import CASOS as CASOS_BASE, ORDEN_LICITACION
from contenido3 import armar, CASOS_NUEVOS, COMPARATIVO, GLOSARIO_NUEVO
CASOS = CASOS_BASE + CASOS_NUEVOS
GLOSARIO = sorted(GLOS_BASE + GLOSARIO_NUEVO, key=lambda g: g[0].lower())

ESCUDO = base64.b64encode(open(AQUI.parent / '.claude/skills/marca-gobernacion/assets/escudo/escudo-color-pantalla.png', 'rb').read()).decode()
ETAPAS = [("bases", "Bases"), ("plan", "Planeación"), ("sel", "Selección"), ("ejec", "Celebración y ejecución"), ("cierre", "Cierre y temas especiales")]
EN = dict(ETAPAS)
mods = armar()

def strip_stack(h):
    # en impresión las tablas se ven completas: quitamos la clase responsive
    return h.replace(' class="stack"', '')

css = """
@page{size:Letter;margin:22mm 20mm 20mm 20mm}
*{box-sizing:border-box}
body{font-family:Poppins,Arial,sans-serif;color:#1c2723;font-size:10.5pt;line-height:1.5;margin:0}
h1,h2,h3{color:#0b5640;line-height:1.15;margin:0}
h1{font-size:30pt}h2{font-size:19pt;margin-bottom:6pt}h3{font-size:12pt;margin:12pt 0 4pt}
p{margin:5pt 0}ul,ol{margin:4pt 0;padding-left:16pt}li{margin:2pt 0}
table{border-collapse:collapse;width:100%;margin:6pt 0;font-size:9.5pt;page-break-inside:auto}
tr{page-break-inside:avoid}
th,td{border:0.6pt solid #c9d4ce;padding:4pt 6pt;text-align:left;vertical-align:top}
th{background:#e9f2ed;font-weight:600}
td.n{text-align:right;white-space:nowrap}
.cover{height:235mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always}
.cover .band{background:#0b5640;color:#fff;padding:26mm 14mm;border-radius:4mm}
.cover .band h1{color:#fff}.cover .band p{color:#dcefe5;font-size:12pt}
.meta{color:#5b6b64;font-size:9pt}
.mod{page-break-before:always}
.obj{background:#f1f6f3;border-radius:3mm;padding:6pt 10pt;margin:8pt 0}
.box{border:0.8pt solid #c9d4ce;border-radius:3mm;padding:6pt 10pt;margin:8pt 0;page-break-inside:avoid}
.box.warn{background:#fff4e5;border-color:#f2c48a}
.box b:first-child{color:#0b5640}.box.warn b:first-child{color:#9a5a00}
.rep{border-top:1pt solid #0b5640;margin-top:10pt;padding-top:4pt}
.rep ol li{margin:3pt 0}
.rep .ops{color:#5b6b64}
.toc a{color:#1c2723;text-decoration:none}
.toc td{border:0;border-bottom:0.5pt solid #e1e8e4;padding:3pt 4pt}
.caso{page-break-inside:avoid;border:0.8pt solid #c9d4ce;border-radius:3mm;padding:6pt 10pt;margin:8pt 0}
.notas{border-bottom:0.6pt solid #c9d4ce;height:16pt}
details,summary{display:block}
"""

def preguntas(m):
    items = []
    for q in m["quiz"]:
        orden = sorted(range(len(q["o"])), key=lambda i: hashlib.md5((q["q"] + q["o"][i]).encode()).hexdigest())
        ops = " · ".join(f"{'abc'[n]}) {q['o'][i]}" for n, i in enumerate(orden))
        items.append(f"<li>{q['q']}<br><span class='ops'>{ops}</span></li>")
    return "<div class='rep'><h3>Preguntas de repaso</h3><ol>" + "".join(items) + "</ol><p class='meta'>Responda en la página del curso: allí verá la explicación y la norma de cada respuesta.</p></div>"

partes = []
partes.append(f"""
<section class="cover">
<div><img src="data:image/png;base64,{ESCUDO}" width="157" height="70" alt="Escudo de Antioquia"></div>
<div class="band"><p class="meta" style="color:#bfe3cf">Memorias del curso · formación interna</p>
<h1>Curso de contratación estatal desde cero</h1>
<p>Guía de estudio para servidores y contratistas de la Gobernación de Antioquia: la vida de un contrato público, desde la necesidad hasta la liquidación.</p>
<p style="margin-top:14pt">Versión 3.0 · corte normativo: noviembre de 2026</p>
<p style="margin-top:18pt;font-size:13pt;color:#fff">Desarrollado por: <b>Alexander Gómez Avendaño</b></p></div>
<div class="meta">Material de autoestudio elaborado con asistencia de IA a partir de normas verificadas a noviembre de 2026. No es un concepto jurídico ni reemplaza a la Secretaría General, a la Dirección de Asuntos Legales ni al Manual de Contratación del Departamento. Verifique el texto vigente de cada norma antes de decidir.</div>
</section>""")

toc = "".join(f"<tr><td>{i+1}.</td><td>{m['t']}</td><td>{EN[m['etapa']]}</td><td class='n'>{m['min']} min</td></tr>" for i, m in enumerate(mods))
partes.append(f"""
<section>
<h2>Contenido</h2>
<table class="toc"><tr><th></th><th>Módulo</th><th>Etapa</th><th>Estudio</th></tr>{toc}</table>
<p>Anexos: taller de casos · cuadro comparativo de modalidades · las etapas de una licitación · plazos frecuentes · glosario · fuentes.</p>
</section><section class="mod"><h2>Cómo usar estas memorias</h2>
<ol>
<li>Estudie los módulos en orden: siguen la ruta de un contrato. En el aula virtual cada módulo se habilita cuando aprueba el anterior (lección leída completa y al menos 70 % en su evaluación, con refuerzo si hace falta).</li>
<li>Al final de cada módulo responda las preguntas de repaso en la página del curso. Cuenta la primera respuesta.</li>
<li>Resuelva el taller de casos y luego presente la evaluación final (40 preguntas, 8 por etapa).</li>
</ol>
<h2 style="margin-top:16pt">Cómo se califica</h2>
<p><b>Índice de apropiación</b> = 20 % práctica de módulos + 30 % taller de casos + 50 % mejor evaluación final.</p>
<table><tr><th>Nivel</th><th>Requisitos</th></tr>
<tr><td>Avanzado</td><td>Índice ≥ 90, evaluación final ≥ 90 % y cada etapa ≥ 7 de 8; módulos y taller completos</td></tr>
<tr><td>Competente</td><td>Índice ≥ 80, evaluación final ≥ 80 % y cada etapa ≥ 6 de 8; módulos y taller completos</td></tr>
<tr><td>En desarrollo</td><td>Índice ≥ 60 o no cumple algún requisito de Competente</td></tr>
<tr><td>Inicial</td><td>Índice menor que 60</td></tr></table>
<p class="meta">El nivel mide la apropiación del contenido del curso. No acredita idoneidad legal ni reemplaza la evaluación de competencias laborales o del desempeño que corresponde a Talento Humano.</p>
</section>""")

for i, m in enumerate(mods):
    h = strip_stack(m["html"])
    partes.append(f"""<section class="mod" id="{m['id']}">
<p class="meta">Módulo {i+1} · {EN[m['etapa']]} · {m['min']} minutos</p>
<h2>{m['t']}</h2>
<div class="obj"><b>Al terminar podrá:</b> {m['obj']}</div>
{h}
{f"<div class='box'><b>En la Gobernación.</b> {m['gob']}</div>" if m.get('gob') else ''}
{f"<div class='box warn'><b>Error frecuente.</b> {m['err']}</div>" if m.get('err') else ''}
{f"<div class='box'><b>Ejemplo resuelto: {m['caso']['t']}.</b> {m['caso']['p']}<br><b>Respuesta sugerida.</b> {m['caso']['r']}</div>" if m.get('caso') else ''}
{preguntas(m)}
</section>""")

casos = "".join(
    f"<div class='caso'><p class='meta'>Caso {n+1} · {EN[c['area']]}</p><h3 style='margin-top:0'>{c['t']}</h3><p>{c['s']}</p><ol>"
    + "".join(f"<li>{q['q']}<br><span class='meta'>" + " · ".join(f"{'abc'[n]}) {q['o'][i]}" for n, i in enumerate(sorted(range(len(q['o'])), key=lambda i: hashlib.md5((q['q'] + q['o'][i]).encode()).hexdigest()))) + "</span></li>" for q in c["q"])
    + "</ol></div>" for n, c in enumerate(CASOS))
partes.append(f"<section class='mod'><h2>Anexo A. Taller de casos</h2><p>{len(CASOS)} situaciones de la Gobernación. Respóndalas en la página del curso: cuentan el 30 % de la calificación.</p>{casos}</section>")
partes.append("<section class='mod'><h2>Anexo A2. Cuadro comparativo de modalidades</h2><p>Escriba en cada fila la modalidad que corresponde. La solución está en la página del curso.</p><table><tr><th>Característica</th><th style='width:38%'>Modalidad</th></tr>" + "".join(f"<tr><td>{r['t']}</td><td></td></tr>" for r in COMPARATIVO["rows"]) + "</table><p class='meta'>Opciones: " + ", ".join(COMPARATIVO["cols"]) + ".</p></section>")
partes.append("<section class='mod'><h2>Anexo B. Las etapas de una licitación pública</h2><ol>" + "".join(f"<li>{e}</li>" for e in ORDEN_LICITACION) + "</ol>"
              + "<h2 style='margin-top:16pt'>Anexo C. Plazos frecuentes</h2><table><tr><th>Actuación</th><th>Plazo</th></tr>" + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in PLAZOS) + "</table><p class='meta'>Días hábiles. Verifique en el Decreto 1082 de 2015 y en el pliego del proceso.</p></section>")
partes.append("<section class='mod'><h2>Anexo D. Glosario</h2><table><tr><th style='width:28%'>Término</th><th>Significado</th></tr>" + "".join(f"<tr><td><b>{a}</b></td><td>{b}</td></tr>" for a, b in GLOSARIO) + "</table></section>")
partes.append("""<section class='mod'><h2>Anexo E. Fuentes</h2><ul>
<li>Constitución Política, arts. 2, 209, 267-274, 345-346, 355.</li>
<li>Ley 80 de 1993; Ley 1150 de 2007; Ley 1474 de 2011; Ley 1882 de 2018; Ley 2022 de 2020; Ley 2195 de 2022; Ley 2014 de 2019; Ley 1952 de 2019 (Código General Disciplinario); Ley 850 de 2003 y Ley 1757 de 2015 (participación ciudadana); Ley 996 de 2005; Ley 1508 de 2012; Ley 1682 de 2013 y Ley 1742 de 2014.</li>
<li>Decreto 1082 de 2015 y sus modificaciones, en especial los Decretos 287 y 0997 de 2026; Decreto Legislativo 1420 de 2026; Decreto 1076 de 2015 (sector ambiente).</li>
<li>Colombia Compra Eficiente: manuales, guías, Documentos Tipo (control de versiones) y conceptos de su relatoría.</li>
<li>Departamento de Antioquia: Manual de Contratación (Decreto 2018070001630 de 2018, mod. Decreto 2023070004507 de 2023); delegaciones contractuales (Decreto 2025070000089 de 2025); estructura administrativa (Decreto Ordenanzal 2024070003913 de 2024).</li>
<li>Valores 2026: SMMLV $ 1.750.905 (Decreto 159 de 2026, transitorio). Cuantías calculadas; confirmar con la publicación oficial del Departamento.</li>
</ul></section>""")

html = f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'><title>Memorias del curso de contratación estatal</title><link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap'><style>{css}</style></head><body>{''.join(partes)}</body></html>"
open(AQUI / 'memorias.html', 'w', encoding='utf-8').write(html)

async def pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME) if CHROME else await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto((AQUI / 'memorias.html').as_uri())
        await pg.wait_for_timeout(1500)
        foot = "<div style='font-family:Arial;font-size:7.5pt;color:#5b6b64;width:100%;padding:0 20mm;display:flex;justify-content:space-between'><span>Curso de contratación estatal desde cero · Desarrollado por Alexander Gómez Avendaño · v3.0 nov. 2026</span><span>Página <span class='pageNumber'></span> de <span class='totalPages'></span></span></div>"
        await pg.pdf(path=str(AQUI / 'Memorias-curso-contratacion-estatal.pdf'), format='Letter', print_background=True,
                     display_header_footer=True, header_template="<div></div>", footer_template=foot,
                     margin={"top": "20mm", "bottom": "18mm", "left": "20mm", "right": "20mm"})
        await b.close()
asyncio.run(pdf())
print("ok")
