"""Versión 2.1 del curso: ampliación con los temas detectados al contrastar el curso con un diplomado
externo de contratación estatal (nov. 2026). Todo el texto es redacción propia y cada norma se verificó
en fuentes oficiales o en la relatoría de Colombia Compra Eficiente (ver CHANGELOG del repositorio).

Este archivo también arma la lista final de módulos para build.py y memorias.py (función armar()).
"""
import copy
from contenido import Q, MODULOS
from contenido2 import EXTRA

# ---------------------------------------------------------------------------------------------
# 1. Módulo nuevo: quién no puede contratar, nulidad y responsabilidades
# ---------------------------------------------------------------------------------------------
M_INHABILIDADES = {
 "id": "m15", "etapa": "plan", "c": "Quién no puede contratar", "min": 30,
 "t": "Quién no puede contratar: inhabilidades, nulidad y responsabilidades",
 "obj": "identificar cuándo una persona no puede contratar con la Gobernación, qué pasa si se firma un contrato que no debía firmarse y quién responde y ante quién.",
 "html": """
<p>Antes de adjudicar o firmar, la entidad verifica que el proponente <b>pueda</b> contratar. No basta con que tenga experiencia y buen precio: la ley impide contratar a ciertas personas para proteger la moralidad y la imparcialidad de la función pública. Si se pasa por alto, el contrato nace con un vicio grave.</p>
<h3>Inhabilidad, incompatibilidad y conflicto de interés</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Figura</th><th>Qué es</th><th>Ejemplo</th></tr></thead><tbody>
<tr><td data-l="Figura"><b>Inhabilidad</b></td><td data-l="Qué es">Impedimento para contratar con <b>cualquier</b> entidad estatal por una situación de la persona (Ley 80, art. 8, num. 1)</td><td data-l="Ejemplo">Quien dio lugar a una caducidad o fue condenado por delitos contra la administración pública</td></tr>
<tr><td data-l="Figura"><b>Incompatibilidad</b></td><td data-l="Qué es">Impedimento para contratar con <b>una entidad concreta</b> por un vínculo con ella (Ley 80, art. 8, num. 2)</td><td data-l="Ejemplo">El hermano de un secretario de despacho no puede contratar con el Departamento</td></tr>
<tr><td data-l="Figura"><b>Conflicto de interés</b></td><td data-l="Qué es">El servidor tiene un interés particular en el asunto; debe declararse impedido y apartarse (CPACA, art. 11)</td><td data-l="Ejemplo">El supervisor que evaluaría la oferta de la empresa de su primo</td></tr>
</tbody></table></div>
<p>Las inhabilidades e incompatibilidades son <b>taxativas</b>: solo existen las que fija la Constitución o la ley, y no se extienden por analogía. Por eso se verifican contra la norma, no contra la intuición.</p>
<h3>Las inhabilidades que más se presentan (Ley 80, art. 8, num. 1)</h3>
<div class="scroll"><table class="stack"><thead><tr><th>No pueden contratar</th><th>Por cuánto tiempo</th></tr></thead><tbody>
<tr><td data-l="Quién">Quienes dieron lugar a la declaratoria de caducidad de un contrato (lit. c)</td><td data-l="Tiempo">5 años desde la ejecutoria del acto que la declaró</td></tr>
<tr><td data-l="Quién">Condenados a interdicción de derechos y funciones públicas y sancionados con destitución (lit. d)</td><td data-l="Tiempo">5 años desde la ejecutoria de la sentencia o del acto</td></tr>
<tr><td data-l="Quién">Quienes, sin justa causa, no firmaron el contrato que se les adjudicó (lit. e) y quienes participaron o contrataron estando inhabilitados (lit. b)</td><td data-l="Tiempo">5 años desde el hecho</td></tr>
<tr><td data-l="Quién">Socios de sociedades de personas a las que se declaró la caducidad (lit. i)</td><td data-l="Tiempo">5 años</td></tr>
<tr><td data-l="Quién">Personas naturales y jurídicas condenadas por delitos contra la administración pública, corrupción o soborno transnacional (lit. j, modificado por la Ley 2014 de 2019)</td><td data-l="Tiempo">Según la ley; verifique el texto vigente</td></tr>
<tr><td data-l="Quién">Quienes financiaron campañas a la Gobernación por encima del límite legal, frente a las entidades del nivel departamental (lit. k)</td><td data-l="Tiempo">Todo el periodo del gobernador elegido</td></tr>
<tr><td data-l="Quién">Contratistas con incumplimiento reiterado: 5 o más multas, o declaratorias de incumplimiento en al menos 2 contratos, <b>en los últimos 3 años</b> (Ley 1474, art. 90, modificado por la Ley 1955 de 2019)</td><td data-l="Tiempo">3 años desde la inscripción de la última multa o incumplimiento en el RUP</td></tr>
</tbody></table></div>
<p class="meta">Cuidado con material de estudio desactualizado: la redacción original del art. 90 exigía que las multas o incumplimientos ocurrieran "en la misma vigencia fiscal". Desde 2019 se cuentan los últimos tres años, y la Ley 2195 de 2022 agregó un supuesto para el Programa de Alimentación Escolar.</p>
<h3>Las incompatibilidades con el Departamento (Ley 80, art. 8, num. 2)</h3>
<ul>
<li><b>Exservidores:</b> quienes fueron servidores de la entidad en niveles directivo, asesor o ejecutivo, o miembros de su junta, durante <b>1 año</b> desde el retiro.</li>
<li><b>Exdirectivos de cualquier entidad estatal:</b> durante <b>2 años</b> desde el retiro, cuando el objeto tenga relación con el sector en el que trabajaron (lit. f, adicionado por la Ley 1474 de 2011, art. 4).</li>
<li><b>Parientes:</b> hasta el 2.º grado de consanguinidad (padres, hijos, hermanos, abuelos, nietos), 2.º de afinidad (suegros, cuñados, yernos, nueras) o 1.º civil (hijos adoptivos) de servidores directivos, asesores o ejecutivos, de miembros de la junta o de quienes ejercen control interno o fiscal.</li>
<li><b>Cónyuges o compañeros permanentes</b> de esas mismas personas.</li>
<li><b>Sociedades</b> (salvo las anónimas abiertas) en las que esas personas sean representantes, socias o directivas.</li>
</ul>
<p>Aparte de lo anterior, el exservidor tiene <b>prohibido gestionar intereses privados</b> ante la entidad donde trabajó: durante 2 años no puede asesorar, representar ni asistir a terceros en asuntos relacionados con sus funciones, y nunca en los asuntos concretos que conoció (Ley 1474, art. 3, hoy recogido en el Código General Disciplinario, Ley 1952 de 2019).</p>
<h3>Si la inhabilidad aparece durante la ejecución (art. 9)</h3>
<ol>
<li>El contratista <b>cede</b> el contrato, con autorización previa y escrita de la entidad, a alguien que cumpla las mismas condiciones. Si no es posible, <b>renuncia</b> a su ejecución.</li>
<li>Si la inhabilidad afecta a un integrante de un consorcio o una unión temporal, ese integrante cede su participación a un tercero autorizado por la entidad. Nunca se cede entre los mismos integrantes.</li>
<li>Si la causa es una condena o sanción por corrupción, no hay renuncia: la entidad ordena la cesión unilateral.</li>
</ol>
<p><b>Excepciones (art. 10):</b> no aplican estas restricciones a quien contrata por obligación legal o para usar los bienes y servicios que la entidad ofrece al público en condiciones comunes, ni en los demás casos que enumera la norma.</p>
<h3>El contrato nulo</h3>
<p>Un contrato es <b>absolutamente nulo</b> en los casos del derecho común y, además, cuando (Ley 80, art. 44):</p>
<ol>
<li>se celebra con personas inhabilitadas o incompatibles;</li>
<li>se celebra contra una prohibición constitucional o legal expresa (por ejemplo, saltarse la modalidad de selección que exigía la ley);</li>
<li>se celebra con abuso o desviación de poder;</li>
<li>se basa en actos administrativos declarados nulos;</li>
<li>desconoce el trato a ofertas nacionales y extranjeras o la reciprocidad.</li>
</ol>
<div class="scroll"><table class="stack"><thead><tr><th>Pregunta</th><th>Respuesta</th></tr></thead><tbody>
<tr><td data-l="Pregunta">¿Quién la alega?</td><td data-l="Respuesta">Las partes, el Ministerio Público, cualquier persona, o el juez de oficio. No se sanea por ratificación (art. 45)</td></tr>
<tr><td data-l="Pregunta">¿Qué hace la entidad?</td><td data-l="Respuesta">En las causales 1, 2 y 4, el jefe de la entidad (o su delegado) <b>debe</b> terminar el contrato por acto motivado y ordenar su liquidación en el estado en que se encuentre (art. 45)</td></tr>
<tr><td data-l="Pregunta">¿Y lo ya ejecutado?</td><td data-l="Respuesta">En contratos de ejecución sucesiva se reconoce lo ejecutado hasta la declaratoria. Si hubo objeto o causa ilícita, solo se paga en la medida en que la entidad se benefició (art. 48)</td></tr>
<tr><td data-l="Pregunta">¿Y la nulidad relativa?</td><td data-l="Respuesta">Los demás vicios del derecho común se sanean por ratificación de las partes o por el paso de 2 años desde el hecho (art. 46). Si solo una cláusula es nula, el resto del contrato sigue, salvo que no pueda existir sin ella (art. 47)</td></tr>
</tbody></table></div>
<h3>Quién responde y ante quién</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Responsabilidad</th><th>Quién la declara</th><th>Alcanza a</th></tr></thead><tbody>
<tr><td data-l="Tipo"><b>Fiscal</b></td><td data-l="Quién">Contraloría (en el Departamento, la Contraloría General de Antioquia)</td><td data-l="Alcanza">Quien, como gestor fiscal, cause daño al patrimonio público por dolo o culpa grave: servidores, contratistas, interventores y consultores</td></tr>
<tr><td data-l="Tipo"><b>Disciplinaria</b></td><td data-l="Quién">Control interno disciplinario de la entidad o la Procuraduría (poder preferente)</td><td data-l="Alcanza">Servidores públicos y particulares que ejercen funciones públicas, como los interventores (Ley 1952 de 2019)</td></tr>
<tr><td data-l="Tipo"><b>Penal</b></td><td data-l="Quién">Fiscalía y jueces penales</td><td data-l="Alcanza">Servidores y también contratistas, interventores, consultores y asesores, que para efectos penales se tratan como particulares que cumplen funciones públicas (Ley 80, art. 56)</td></tr>
<tr><td data-l="Tipo"><b>Civil o patrimonial</b></td><td data-l="Quién">Jueces de lo contencioso administrativo</td><td data-l="Alcanza">La entidad responde ante el contratista (art. 50) y luego puede repetir contra el servidor que actuó con dolo o culpa grave (acción de repetición, Ley 678 de 2001)</td></tr>
</tbody></table></div>
<p>Los servidores responden disciplinaria, civil y penalmente por sus actos y omisiones en la contratación (art. 51); los contratistas, civil y penalmente (art. 52); los consultores y asesores, civil, fiscal, penal y disciplinariamente, y los interventores igual cuando el daño provenga del incumplimiento de sus propias obligaciones (art. 53, modificado por la Ley 1882 de 2018). Quien sea declarado responsable civil o penalmente queda inhabilitado por <b>10 años</b> para contratar y ejercer cargos públicos (art. 58).</p>
""",
 "gob": "Antes de adjudicar o firmar, el área de contratación revisa antecedentes (Procuraduría, Contraloría, Policía, medidas correctivas, REDAM, listas restrictivas) y el RUP, y exige la declaración del proponente de no estar incurso en inhabilidades. Revise también a cada integrante de un consorcio o unión temporal y a los socios cuando la norma lo exige. Si tiene un vínculo con un proponente, declárese impedido por escrito ante su superior antes de intervenir.",
 "err": "Revisar solo al representante legal o al integrante líder. Las inhabilidades se miran en cada integrante del consorcio o la unión temporal y, en varias causales, en los socios. Un contrato firmado con un integrante inhábil es absolutamente nulo.",
 "caso": {"t": "La sobrina del secretario",
          "p": "Una consultora cuya gerente es sobrina del secretario de despacho se presenta a un concurso de méritos de su secretaría.",
          "r": "La sobrina es pariente en 3.er grado de consanguinidad. La incompatibilidad del art. 8 de la Ley 80 llega hasta el 2.º grado, así que esa causal no aplica y la firma puede participar. Pero el secretario tiene un conflicto de interés (el CPACA, art. 11, cubre parientes hasta el 4.º grado): debe declararse impedido y no intervenir en la evaluación ni en la adjudicación."},
 "quiz": [
  Q("El hermano de un secretario de despacho de la Gobernación quiere presentar oferta en un proceso del Departamento. ¿Puede?", ["Sí, si ofrece el mejor precio", "No: es pariente en 2.º grado de un servidor del nivel directivo de la entidad contratante", "Sí, siempre que el secretario no firme el contrato"], 1, "Ley 80, art. 8, num. 2, lit. b: la incompatibilidad alcanza a parientes hasta el 2.º grado de consanguinidad de servidores directivos, asesores o ejecutivos de la entidad."),
  Q("Un exdirectivo de una entidad del sector transporte se retiró hace 18 meses y quiere contratar una consultoría vial. ¿Qué regla revisa?", ["Ninguna: ya pasó el año de incompatibilidad", "El lit. f del art. 8, num. 2: 2 años cuando el objeto se relaciona con el sector donde trabajó", "Solo su RUP"], 1, "La Ley 1474 de 2011, art. 4, agregó una incompatibilidad de 2 años para exdirectivos cuando el objeto se relaciona con su antiguo sector."),
  Q("Durante la ejecución, el contratista queda inhabilitado por una sanción que no es por corrupción. ¿Qué procede?", ["Sigue ejecutando hasta terminar", "Cede el contrato con autorización escrita de la entidad o, si no es posible, renuncia a su ejecución", "La entidad lo liquida sin más"], 1, "Ley 80, art. 9: inhabilidad sobreviniente."),
  Q("Se descubre que un contrato en ejecución se firmó con una persona incompatible. ¿Qué debe hacer la Gobernación?", ["Esperar a que un juez lo anule", "Terminarlo por acto motivado y ordenar su liquidación", "Modificarlo para cambiar de contratista"], 1, "Ley 80, art. 45: en las causales 1, 2 y 4 del art. 44 el jefe de la entidad debe terminar el contrato y liquidarlo."),
  Q("La nulidad absoluta de un contrato estatal…", ["Solo la pueden alegar las partes", "Se sanea si las partes la ratifican", "La pueden alegar las partes, el Ministerio Público o cualquier persona, y no se sanea por ratificación"], 2, "Ley 80, art. 45."),
  Q("Un contratista acumula 5 multas en distintos contratos durante los últimos 3 años. ¿Qué ocurre?", ["Nada, porque fueron en años distintos", "Queda inhabilitado por 3 años desde la inscripción de la última multa en el RUP", "Pierde el RUP para siempre"], 1, "Ley 1474, art. 90, modificado por la Ley 1955 de 2019: ya no se exige que sean en la misma vigencia fiscal."),
  Q("Para efectos penales, el interventor de un contrato es…", ["Un particular sin responsabilidad penal especial", "Un particular que cumple funciones públicas, con la responsabilidad penal de los servidores", "Un servidor público de carrera"], 1, "Ley 80, art. 56."),
  Q("Quien es declarado responsable penalmente por hechos de la contratación queda inhabilitado para contratar y ejercer cargos públicos por…", ["1 año", "5 años", "10 años"], 2, "Ley 80, art. 58, num. 3."),
  Q("El supervisor descubre que el proponente mejor calificado es la empresa de su primo. ¿Qué hace?", ["Nada, porque el primo está en 4.º grado y no hay incompatibilidad", "Se declara impedido por escrito y se aparta del proceso", "Le baja el puntaje para evitar sospechas"], 1, "Aunque no haya incompatibilidad para el oferente, el servidor tiene conflicto de interés (CPACA, art. 11) y debe apartarse."),
 ],
}

# ---------------------------------------------------------------------------------------------
# 2. Ampliaciones de módulos existentes (se agregan al final de su contenido)
# ---------------------------------------------------------------------------------------------
AMPLIAR_HTML = {
"m2": """
<h3>El control ciudadano también hace parte del proceso</h3>
<ul>
<li>Todo contrato estatal está sujeto a la vigilancia y el control ciudadano (Ley 80, art. 66).</li>
<li>Las <b>veedurías ciudadanas</b> (Ley 850 de 2003, ajustada por la Ley 1757 de 2015) pueden vigilar cualquier etapa: piden información, asisten a audiencias y denuncian irregularidades.</li>
<li>Cuando la modalidad tiene aviso de convocatoria y acto de apertura, la entidad convoca a las veedurías en esos documentos (Decreto 1082 de 2015, arts. 2.2.1.1.2.1.2 y 2.2.1.1.2.1.5).</li>
<li>La entidad debe darles la información que pidan y responder sus peticiones como cualquier derecho de petición.</li>
<li>La <b>rendición de cuentas</b> a la ciudadanía es una obligación permanente de la administración (Ley 1757 de 2015; documento CONPES 3654 de 2010).</li>
</ul>
<p class="meta">Las inhabilidades e incompatibilidades se estudian a fondo en el módulo "Quién no puede contratar".</p>
""",
"m3": """
<h3>Quién puede ser contratista</h3>
<p>Pueden contratar las personas naturales y jurídicas con capacidad legal que no estén inhabilitadas, y también los <b>consorcios</b> y las <b>uniones temporales</b> (Ley 80, arts. 6 y 7). La diferencia entre estos dos importa cuando algo sale mal:</p>
<div class="scroll"><table class="stack"><thead><tr><th>Tema</th><th>Consorcio</th><th>Unión temporal</th></tr></thead><tbody>
<tr><td data-l="Tema">Frente a la entidad</td><td data-l="Consorcio">Todos responden solidariamente por todas las obligaciones de la oferta y del contrato</td><td data-l="Unión temporal">Todos responden solidariamente por el cumplimiento total de la oferta y del contrato</td></tr>
<tr><td data-l="Tema">Sanciones por incumplimiento</td><td data-l="Consorcio">Afectan a todos los integrantes</td><td data-l="Unión temporal">Se imponen según la participación de cada integrante en la ejecución</td></tr>
<tr><td data-l="Tema">Qué debe decir el documento de conformación</td><td data-l="Consorcio">Integrantes, representante y reglas básicas</td><td data-l="Unión temporal">Además, los términos y la extensión de la participación de cada uno, que no se pueden cambiar sin autorización de la entidad</td></tr>
</tbody></table></div>
<p>Ninguno de los dos es una persona jurídica nueva. Deben designar un representante, y cada integrante debe cumplir por separado las reglas de inhabilidades.</p>
<h3>Quién firma por la entidad</h3>
<p>La competencia para contratar es del jefe o representante legal de la entidad; en el Departamento, del Gobernador (Ley 80, art. 11). La ley le permite delegarla en servidores del nivel directivo o ejecutivo (art. 12), y en la Gobernación esa delegación está en el Decreto 2025070000089 de 2025. Delegar no lo libera de vigilar y controlar la actividad contractual.</p>
<h3>Entidades con régimen especial</h3>
<p>No todas las entidades públicas aplican el Estatuto General. Tienen régimen propio, entre otras, las universidades públicas (Ley 30 de 1992), las empresas sociales del Estado en salud (Ley 100 de 1993), las empresas de servicios públicos domiciliarios (Ley 142 de 1994) y las empresas industriales y comerciales del Estado cuando compiten en el mercado. Aun así, deben aplicar los principios de la función administrativa y de la gestión fiscal, y el régimen de inhabilidades e incompatibilidades (Ley 1150, art. 13).</p>
""",
"m9": """
<h3>Las tres clases de garantía</h3>
<p>El oferente o contratista puede escoger entre (Decreto 1082 de 2015, art. 2.2.1.2.3.1.2): <b>1.</b> contrato de seguro contenido en una póliza; <b>2.</b> patrimonio autónomo; <b>3.</b> garantía bancaria. La responsabilidad civil extracontractual <b>solo</b> se ampara con contrato de seguro (art. 2.2.1.2.3.1.5).</p>
<p class="meta">Algunos materiales antiguos todavía enumeran seis clases (endoso de títulos, depósito de dinero, cartas de crédito). Esa lista venía de normas derogadas; hoy rigen las tres anteriores.</p>
<h3>Cuánto deben cubrir y por cuánto tiempo</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Amparo</th><th>Valor mínimo</th><th>Vigencia mínima</th></tr></thead><tbody>
<tr><td data-l="Amparo">Seriedad de la oferta</td><td data-l="Valor">10 % del valor de la oferta (en subasta inversa y concurso de méritos, del presupuesto oficial)</td><td data-l="Vigencia">Desde la presentación de la oferta hasta la aprobación de la garantía de cumplimiento</td></tr>
<tr><td data-l="Amparo">Buen manejo del anticipo / pago anticipado</td><td data-l="Valor">100 % del anticipo o del pago anticipado</td><td data-l="Vigencia">Hasta la liquidación o hasta que se amortice o verifique, según defina la entidad</td></tr>
<tr><td data-l="Amparo">Cumplimiento</td><td data-l="Valor">10 % del valor del contrato</td><td data-l="Vigencia">Hasta la liquidación</td></tr>
<tr><td data-l="Amparo">Salarios, prestaciones e indemnizaciones</td><td data-l="Valor">5 % del valor del contrato</td><td data-l="Vigencia">Plazo del contrato y 3 años más</td></tr>
<tr><td data-l="Amparo">Estabilidad y calidad de la obra</td><td data-l="Valor">Lo fija la entidad en el pliego</td><td data-l="Vigencia">5 años desde el recibo a satisfacción (menos, solo con justificación técnica)</td></tr>
<tr><td data-l="Amparo">Calidad del servicio / calidad de los bienes</td><td data-l="Valor">Lo fija la entidad según el contrato</td><td data-l="Vigencia">La que fije la entidad (en interventoría, igual a la estabilidad de la obra vigilada)</td></tr>
</tbody></table></div>
<p class="meta">Decreto 1082 de 2015, arts. 2.2.1.2.3.1.9 a 2.2.1.2.3.1.16. Para ofertas o contratos de más de 1.000.000 SMMLV hay porcentajes menores escalonados.</p>
<h3>Responsabilidad civil extracontractual (art. 2.2.1.2.3.1.17)</h3>
<div class="scroll"><table><thead><tr><th>Valor del contrato</th><th>Valor asegurado mínimo</th></tr></thead><tbody>
<tr><td>Hasta 1.500 SMMLV</td><td class="n">200 SMMLV</td></tr>
<tr><td>Más de 1.500 y hasta 2.500 SMMLV</td><td class="n">300 SMMLV</td></tr>
<tr><td>Más de 2.500 y hasta 5.000 SMMLV</td><td class="n">400 SMMLV</td></tr>
<tr><td>Más de 5.000 y hasta 10.000 SMMLV</td><td class="n">500 SMMLV</td></tr>
<tr><td>Más de 10.000 SMMLV</td><td class="n">5 % del contrato, máximo 75.000 SMMLV</td></tr>
</tbody></table></div>
<p>Vigencia: igual al plazo de ejecución del contrato.</p>
<h3>Cuándo no son obligatorias</h3>
<p>En los contratos de empréstito, interadministrativos y de seguro, y en los de valor inferior al 10 % de la menor cuantía; en estos casos la entidad decide si las exige según la naturaleza del objeto y la forma de pago (Ley 1150, art. 7). En la contratación directa tampoco son obligatorias; la exigencia se justifica en el estudio previo.</p>
<h3>Cómo se hacen efectivas (art. 2.2.1.2.3.1.19)</h3>
<p>El acto que declara la caducidad, el que impone multas o el que declara el incumplimiento constituye el siniestro y sirve de reclamación ante la aseguradora, siempre después del procedimiento del art. 86 de la Ley 1474 con citación del garante. Si una reclamación reduce el valor asegurado o el contrato se adiciona o prorroga, el contratista debe restablecer o ampliar la garantía (art. 2.2.1.2.3.1.18).</p>
""",
"m10": """
<h3>Cuando no hay acuerdo: los poderes excepcionales</h3>
<p>Para evitar que se paralice o se afecte gravemente un servicio público, la entidad puede, por acto administrativo motivado, ejercer facultades que un particular no tiene (Ley 80, art. 14). Son obligatorias en contratos de obra, de explotación o concesión de bienes del Estado, de prestación de servicios públicos y de monopolios estatales; en suministro y prestación de servicios se pueden pactar.</p>
<div class="scroll"><table class="stack"><thead><tr><th>Poder</th><th>Cuándo y cómo</th></tr></thead><tbody>
<tr><td data-l="Poder"><b>Interpretación unilateral</b> (art. 15)</td><td data-l="Cuándo">Si un desacuerdo sobre una cláusula puede paralizar o afectar gravemente el servicio y no hay acuerdo, la entidad interpreta la cláusula</td></tr>
<tr><td data-l="Poder"><b>Modificación unilateral</b> (art. 16)</td><td data-l="Cuándo">Para evitar la paralización, la entidad agrega o suprime obras, trabajos, suministros o servicios. Primero intenta el acuerdo. Si el cambio altera el valor en <b>20 % o más</b> del inicial, el contratista puede renunciar a seguir y el contrato se liquida</td></tr>
<tr><td data-l="Poder"><b>Terminación unilateral</b> (art. 17)</td><td data-l="Cuándo">Por necesidades del servicio o de orden público; muerte o incapacidad física permanente del contratista persona natural, o disolución de la persona jurídica; interdicción o quiebra; cesación de pagos, concurso de acreedores o embargos que afecten gravemente el contrato</td></tr>
<tr><td data-l="Poder"><b>Caducidad</b> (art. 18)</td><td data-l="Cuándo">Incumplimiento grave del contratista que puede paralizar el contrato (ver módulo de incumplimiento)</td></tr>
<tr><td data-l="Poder"><b>Reversión</b> (art. 19)</td><td data-l="Cuándo">En contratos de explotación o concesión, al terminar el plazo los bienes vinculados pasan a la entidad sin compensación</td></tr>
</tbody></table></div>
<p>Cuando se ejerce uno de estos poderes, la entidad reconoce las compensaciones e indemnizaciones a que haya lugar para mantener el equilibrio económico del contrato.</p>
""",
}

AMPLIAR_QUIZ = {
"m2": [
 Q("Una veeduría ciudadana pide los informes de supervisión de un contrato de obra. ¿Qué hace la Gobernación?", ["Los niega porque la veeduría no es parte del contrato", "Se los entrega: todo contrato estatal está sujeto a control ciudadano", "Los entrega solo si lo ordena un juez"], 1, "Ley 80, art. 66, y Ley 850 de 2003: las autoridades deben apoyar el control ciudadano y entregar la información que se solicite, salvo la reservada por ley."),
],
"m3": [
 Q("En una unión temporal, las sanciones por incumplimiento se imponen…", ["A todos por igual", "Según la participación de cada integrante en la ejecución", "Solo al representante"], 1, "Ley 80, art. 7, num. 2. En el consorcio, en cambio, afectan a todos."),
 Q("¿Quién tiene la competencia para celebrar contratos en el Departamento?", ["Cualquier secretario por el solo hecho de su cargo", "El Gobernador, que puede delegarla en servidores del nivel directivo o ejecutivo", "La Asamblea Departamental"], 1, "Ley 80, arts. 11 y 12; en la Gobernación, Decreto 2025070000089 de 2025."),
],
"m9": [
 Q("¿Cuáles son las clases de garantía que admite hoy el Decreto 1082 de 2015?", ["Póliza, patrimonio autónomo y garantía bancaria", "Póliza, cheque y pagaré", "Solo póliza de seguros"], 0, "Art. 2.2.1.2.3.1.2. La responsabilidad civil extracontractual solo se cubre con póliza."),
 Q("Un contrato de obra vale 3.000 SMMLV. ¿Cuál es el valor asegurado mínimo de responsabilidad civil extracontractual?", ["200 SMMLV", "400 SMMLV", "5 % del contrato"], 1, "Art. 2.2.1.2.3.1.17: más de 2.500 y hasta 5.000 SMMLV → 400 SMMLV."),
 Q("¿En cuál de estos contratos las garantías NO son obligatorias por ley?", ["Obra por licitación", "Interadministrativo", "Interventoría por concurso de méritos"], 1, "Ley 1150, art. 7: empréstito, interadministrativos, seguros y contratos inferiores al 10 % de la menor cuantía."),
],
"m10": [
 Q("La Gobernación aumenta unilateralmente las cantidades de una obra en un 25 % del valor inicial. ¿Qué puede hacer el contratista?", ["Nada: debe ejecutar", "Renunciar a continuar, porque el cambio supera el 20 %", "Exigir una nueva licitación"], 1, "Ley 80, art. 16: si la modificación unilateral altera el valor en 20 % o más, el contratista puede renunciar."),
 Q("En un contrato de suministro, las cláusulas excepcionales…", ["Son obligatorias siempre", "Están prohibidas", "Se pueden pactar"], 2, "Ley 80, art. 14, num. 2: facultativas en suministro y prestación de servicios; obligatorias en obra, concesiones, servicios públicos y monopolios."),
],
}

AMPLIAR_ERR = {}

# ---------------------------------------------------------------------------------------------
# 3. Casos nuevos del taller
# ---------------------------------------------------------------------------------------------
CASOS_NUEVOS = [
 {"id": "c11", "area": "plan", "t": "El exsecretario que vuelve como consultor",
  "s": "El exsecretario de Infraestructura Física se retiró hace 10 meses. Hoy es socio de una firma de ingeniería que quiere presentarse a un concurso de méritos para diseños viales de la Gobernación.",
  "q": [
   Q("¿Puede la firma presentarse?", ["Sí, porque él ya no es servidor", "No: como exdirectivo, él y las sociedades de las que hace parte no pueden contratar durante 2 años en asuntos relacionados con su antiguo sector", "Sí, si él no firma la oferta"], 1, "Ley 80, art. 8, num. 2, lit. f (adicionado por la Ley 1474, art. 4). Además, durante el primer año aplica la incompatibilidad del lit. a frente al Departamento."),
   Q("¿Puede él, en vez de ser socio, asesorar a otro proponente en ese mismo concurso?", ["Sí, porque asesorar no es contratar", "No: durante 2 años no puede gestionar intereses privados ante la entidad en asuntos relacionados con sus funciones, y nunca en los asuntos concretos que conoció", "Sí, si lo informa a la Procuraduría"], 1, "Ley 1474 de 2011, art. 3, hoy en el Código General Disciplinario (Ley 1952 de 2019)."),
  ]},
 {"id": "c12", "area": "ejec", "t": "Una unión temporal que incumple",
  "s": "La Unión Temporal Vías del Norte (integrante A 70 %, integrante B 30 %) incumple el cronograma de un mejoramiento vial. La entidad prepara el procedimiento del art. 86 de la Ley 1474.",
  "q": [
   Q("¿A quién cita la entidad?", ["Solo al integrante A", "A la unión temporal, por medio de su representante, y a la aseguradora", "A los integrantes por separado, sin la aseguradora"], 1, "Se cita al contratista y al garante."),
   Q("Si se impone una multa, ¿cómo se reparte la sanción?", ["Toda a A, por tener la mayor participación", "Según la participación de cada integrante en la ejecución", "Por partes iguales"], 1, "Ley 80, art. 7, num. 2: en la unión temporal las sanciones se imponen según la participación en la ejecución."),
  ]},
 {"id": "c13", "area": "ejec", "t": "¿Cuánto debe cubrir la póliza?",
  "s": "Se adjudica una obra por $ 5.252.715.000 (3.000 SMMLV de 2026, a $ 1.750.905 cada uno). El plazo es de 10 meses y no hay anticipo.",
  "q": [
   Q("Valor mínimo del amparo de cumplimiento:", ["$ 262.635.750", "$ 525.271.500", "$ 700.362.000"], 1, "10 % del valor del contrato: 0,10 × $ 5.252.715.000."),
   Q("Valor mínimo de la póliza de responsabilidad civil extracontractual:", ["200 SMMLV = $ 350.181.000", "400 SMMLV = $ 700.362.000", "5 % del contrato = $ 262.635.750"], 1, "Contratos de más de 2.500 y hasta 5.000 SMMLV: 400 SMMLV × $ 1.750.905."),
   Q("Vigencia mínima del amparo de salarios y prestaciones:", ["Hasta la liquidación", "El plazo del contrato y 3 años más", "5 años desde el recibo de la obra"], 1, "Decreto 1082 de 2015, art. 2.2.1.2.3.1.13."),
  ]},
 {"id": "c14", "area": "cierre", "t": "El contrato que nació con un vicio",
  "s": "A mitad de un contrato de mantenimiento de sedes, la oficina jurídica descubre que el contratista es cónyuge de una asesora del Departamento desde antes de firmar. El contratista ha ejecutado el 40 % y la entidad recibió esos trabajos.",
  "q": [
   Q("¿Qué decisión corresponde?", ["Dejar terminar el contrato y no volver a contratarlo", "Terminar el contrato por acto motivado y ordenar su liquidación en el estado en que se encuentre", "Suspenderlo hasta que la asesora renuncie"], 1, "Ley 80, art. 44, num. 1, y art. 45."),
   Q("¿Se paga lo ya ejecutado y recibido?", ["No, nada, porque el contrato es nulo", "Sí: en contratos de ejecución sucesiva se reconoce lo ejecutado hasta la terminación", "Solo si el contratista demanda"], 1, "Ley 80, art. 48. Además, se evalúan las responsabilidades de quienes omitieron la verificación."),
  ]},
]

# ---------------------------------------------------------------------------------------------
# 4. Ejercicio: cuadro comparativo de modalidades
# ---------------------------------------------------------------------------------------------
COMPARATIVO = {
 "cols": ["Licitación pública", "Selección abreviada", "Concurso de méritos", "Contratación directa", "Mínima cuantía"],
 "rows": [
  {"t": "Es la regla general: se usa cuando el caso no encaja en otra modalidad", "a": 0, "e": "Ley 1150, art. 2, num. 1."},
  {"t": "Adjudicación en audiencia pública", "a": 0, "e": "La licitación se adjudica en audiencia (Ley 80, art. 30, y Decreto 1082)."},
  {"t": "Bienes y servicios de características técnicas uniformes por subasta inversa", "a": 1, "e": "Ley 1150, art. 2, num. 2, lit. a."},
  {"t": "Contratos de menor cuantía", "a": 1, "e": "Ley 1150, art. 2, num. 2, lit. b."},
  {"t": "Consultoría: estudios, diseños, interventoría; el precio no es factor de evaluación", "a": 2, "e": "Ley 1150, art. 2, num. 3, y art. 5, num. 4."},
  {"t": "Solo procede por causales taxativas, como urgencia manifiesta o contratos interadministrativos", "a": 3, "e": "Ley 1150, art. 2, num. 4."},
  {"t": "Servicios profesionales y de apoyo a la gestión", "a": 3, "e": "Ley 1150, art. 2, num. 4, lit. h."},
  {"t": "Cualquier objeto hasta el 10 % de la menor cuantía; gana el menor precio", "a": 4, "e": "Ley 1150, art. 2, num. 5 (adicionado por la Ley 1474, art. 94)."},
  {"t": "La oferta y la comunicación de aceptación forman el contrato", "a": 4, "e": "Decreto 1082 de 2015, art. 2.2.1.2.1.5.2."},
 ],
}

GLOSARIO_NUEVO = [
 ("Inhabilidad", "Impedimento legal para contratar con cualquier entidad estatal por una situación de la persona (Ley 80, art. 8, num. 1)."),
 ("Incompatibilidad", "Impedimento para contratar con una entidad determinada por un vínculo con ella o con sus servidores (Ley 80, art. 8, num. 2)."),
 ("Nulidad absoluta", "Vicio grave del contrato (Ley 80, art. 44) que no se sanea por ratificación; en algunas causales obliga a terminar y liquidar el contrato."),
 ("Consorcio", "Dos o más personas que presentan una oferta conjunta y responden solidariamente por todo; las sanciones afectan a todos."),
 ("Unión temporal", "Como el consorcio, pero las sanciones por incumplimiento se imponen según la participación de cada integrante en la ejecución."),
 ("Veeduría ciudadana", "Organización de ciudadanos que vigila la gestión pública y la contratación (Ley 850 de 2003)."),
 ("Reversión", "Paso a la entidad, sin compensación, de los bienes vinculados a un contrato de explotación o concesión al terminar el plazo (Ley 80, art. 19)."),
]

VERSION = "2.1 (nov. 2026)"


def armar():
    """Devuelve (modulos, casos_extra, comparativo, glosario_extra) ya integrados y en orden."""
    mods = copy.deepcopy(MODULOS)
    for m in mods:
        m["html"] = m["html"] + AMPLIAR_HTML.get(m["id"], "")
        m["quiz"] = m["quiz"] + EXTRA[m["id"]] + AMPLIAR_QUIZ.get(m["id"], [])
    nuevo = copy.deepcopy(M_INHABILIDADES)
    pos = next(i for i, m in enumerate(mods) if m["id"] == "m5") + 1
    mods.insert(pos, nuevo)
    return mods
