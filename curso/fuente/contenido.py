"""Contenido del curso. Fuente: referencias verificadas del repositorio skills_Sector_publico_antioquia (nov. 2026)."""

def Q(q, o, a, e):
    return {"q": q, "o": o, "a": a, "e": e}

MODULOS = [
# ------------------------------------------------------------------ BASES
{"id": "m1", "etapa": "bases", "c": "Qué es contratar con el Estado", "min": 15,
 "t": "Qué es la contratación estatal y por qué importa",
 "obj": "explicar qué es un contrato estatal, para qué sirve y qué tiene de distinto frente a un contrato entre particulares.",
 "html": """
<p>Un <b>contrato estatal</b> es todo acuerdo que celebra una entidad pública para cumplir sus fines: construir una vía, comprar computadores, contratar un estudio o un profesional. La Gobernación no puede comprar como una empresa privada: usa recursos públicos y debe demostrar que eligió bien, al precio justo y sin favorecer a nadie.</p>
<h3>Tres ideas que lo cambian todo</h3>
<ol>
<li><b>Legalidad.</b> El servidor público solo puede hacer lo que la norma le permite. Si no hay norma que lo autorice, no se hace.</li>
<li><b>Planeación.</b> Antes de contratar hay que saber qué se necesita, cuánto cuesta, si hay plata (CDP) y qué puede salir mal.</li>
<li><b>Selección objetiva.</b> Se escoge la mejor oferta según reglas conocidas de antemano, nunca por afinidad o recomendación.</li>
</ol>
<h3>Diferencias con un contrato privado</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Tema</th><th>Contrato privado</th><th>Contrato estatal</th></tr></thead><tbody>
<tr><td data-l="Tema">Con quién</td><td data-l="Privado">Libre elección</td><td data-l="Estatal">Proceso de selección reglado</td></tr>
<tr><td data-l="Tema">Precio</td><td data-l="Privado">Lo que acuerden</td><td data-l="Estatal">Justificado con análisis del sector y presupuesto oficial</td></tr>
<tr><td data-l="Tema">Poderes especiales</td><td data-l="Privado">No existen</td><td data-l="Estatal">Cláusulas excepcionales: interpretación, modificación y terminación unilaterales, caducidad</td></tr>
<tr><td data-l="Tema">Publicidad</td><td data-l="Privado">Reservado</td><td data-l="Estatal">Todo se publica en SECOP II</td></tr>
<tr><td data-l="Tema">Responsabilidad</td><td data-l="Privado">Civil</td><td data-l="Estatal">Civil, fiscal, disciplinaria y penal para servidores, contratistas, supervisores e interventores</td></tr>
</tbody></table></div>
<p>La Gobernación de Antioquia se rige por el <b>Estatuto General de Contratación</b> (Ley 80 de 1993 y normas que la modifican). Algunas entidades descentralizadas, como las empresas industriales y comerciales del Estado, tienen <b>régimen especial</b> (derecho privado), pero aun así deben aplicar los principios de la función pública (Ley 1150, art. 13).</p>
""",
 "gob": "Todo proceso queda en SECOP II y el expediente documental en Mercurio. El Manual de Contratación del Departamento (Decreto 2018070001630 de 2018, modificado por el Decreto 2023070004507 de 2023) detalla cómo se aplica la ley en la entidad.",
 "err": "Creer que \"si es urgente, se contrata con quien sea\". La urgencia manifiesta existe, pero tiene requisitos, se declara por acto motivado (salvo que una norma la dé por configurada) y se reporta de inmediato a la Contraloría.",
 "caso": {"t": "la compra rápida", "p": "Un jefe le pide contratar \"ya mismo\" a un conocido para pintar una sede, sin estudios ni proceso, porque \"es poquita plata\".", "r": "Aunque el valor sea bajo, hay que planear (necesidad, CDP, estudio previo) y usar la modalidad que corresponda; para valores pequeños existe la mínima cuantía, con invitación pública de al menos un día hábil. Elegir a dedo viola la selección objetiva."},
 "quiz": [
  Q("¿Qué principio obliga a escoger la oferta con reglas conocidas de antemano?", ["Economía", "Selección objetiva", "Autonomía de la voluntad"], 1, "La selección objetiva (Ley 1150, art. 5) impide elegir por motivos subjetivos."),
  Q("¿Dónde se publica la contratación de la Gobernación?", ["Solo en la página web", "En SECOP II", "En la Gaceta Departamental únicamente"], 1, "SECOP II es la plataforma transaccional obligatoria; la publicación es en ella."),
  Q("Las cláusulas excepcionales permiten a la entidad, entre otras cosas…", ["Cambiar el objeto del contrato", "Terminar unilateralmente o declarar la caducidad", "No pagar al contratista"], 1, "Interpretación, modificación y terminación unilaterales y caducidad (Ley 80, arts. 14-18)."),
 ]},

{"id": "m2", "etapa": "bases", "c": "Marco normativo y principios", "min": 20,
 "t": "El marco normativo y los principios",
 "obj": "ubicar las normas principales, saber qué regula cada una y aplicar los principios de la contratación.",
 "html": """
<h3>La pirámide que debe conocer</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Norma</th><th>Para qué la va a usar</th></tr></thead><tbody>
<tr><td data-l="Norma"><b>Ley 80 de 1993</b></td><td data-l="Uso">El estatuto: principios, cláusulas excepcionales, inhabilidades (arts. 8-10), adiciones (art. 40), perfeccionamiento (art. 41), urgencia manifiesta (arts. 42-43), liquidación (art. 60)</td></tr>
<tr><td data-l="Norma"><b>Ley 1150 de 2007</b></td><td data-l="Uso">Las modalidades de selección (art. 2), SECOP (art. 3), riesgos (art. 4), selección objetiva (art. 5), plazo de liquidación (art. 11)</td></tr>
<tr><td data-l="Norma"><b>Ley 1474 de 2011</b></td><td data-l="Uso">Estatuto Anticorrupción: supervisión e interventoría (arts. 82-85), multas y caducidad (art. 86), maduración de proyectos (art. 87)</td></tr>
<tr><td data-l="Norma"><b>Ley 1882 de 2018</b></td><td data-l="Uso">Subsanabilidad de ofertas, documentos tipo, ajustes a infraestructura</td></tr>
<tr><td data-l="Norma"><b>Ley 2022 de 2020</b></td><td data-l="Uso">Documentos Tipo obligatorios</td></tr>
<tr><td data-l="Norma"><b>Ley 2195 de 2022</b></td><td data-l="Uso">Medidas anticorrupción y programa de transparencia</td></tr>
<tr><td data-l="Norma"><b>Ley 996 de 2005</b></td><td data-l="Uso">Ley de Garantías: restricciones antes de elecciones</td></tr>
<tr><td data-l="Norma"><b>Decreto 1082 de 2015</b></td><td data-l="Uso">El reglamento, paso a paso de cada modalidad. Modificado en 2026 por los Decretos 287 y 0997</td></tr>
<tr><td data-l="Norma"><b>Normas departamentales</b></td><td data-l="Uso">Manual de Contratación, delegaciones contractuales (Decreto 2025070000089 de 2025), manual de supervisión</td></tr>
</tbody></table></div>
<h3>Los principios en palabras simples</h3>
<ul>
<li><b>Transparencia:</b> todo es público, las reglas se conocen antes y cualquiera puede observar.</li>
<li><b>Economía:</b> procesos ágiles, sin trámites inútiles, con recursos disponibles antes de contratar.</li>
<li><b>Responsabilidad:</b> quien participa responde por sus actos y omisiones.</li>
<li><b>Equilibrio económico:</b> si hechos imprevisibles rompen la ecuación del contrato, se restablece (Ley 80, art. 27).</li>
<li><b>Planeación:</b> no se contrata sin estudios, presupuesto y riesgos analizados.</li>
<li><b>Selección objetiva:</b> se elige la oferta más favorable con factores fijados en el pliego.</li>
</ul>
<h3>Inhabilidades e incompatibilidades</h3>
<p>Son prohibiciones para contratar con el Estado (Ley 80, arts. 8-10, y otras leyes): por ejemplo, personas sancionadas, parientes de ciertos servidores o exservidores en periodos determinados. Antes de firmar se verifican antecedentes: Procuraduría, Contraloría, Policía, medidas correctivas y REDAM, y desde 2026 las listas restrictivas internacionales (Decreto 0997).</p>
""",
 "gob": "Las delegaciones contractuales del Gobernador están en el Decreto 2025070000089 de 2025. Quien firma un contrato es el ordenador del gasto delegado de su secretaría; verifique quién es en su dependencia.",
 "err": "Citar artículos de memoria. Varias normas cambiaron en 2012, 2018, 2020 y 2026: verifique siempre el texto vigente en SUIN-Juriscol o Función Pública antes de citarlo.",
 "quiz": [
  Q("¿Qué norma fija las modalidades de selección?", ["Ley 80 de 1993", "Ley 1150 de 2007, art. 2", "Ley 2195 de 2022"], 1, "El art. 2 de la Ley 1150 define licitación, selección abreviada, concurso de méritos, contratación directa y mínima cuantía."),
  Q("El procedimiento para imponer multas y declarar la caducidad está en…", ["Ley 1474 de 2011, art. 86", "Decreto 1082, art. 2.2.1.1.1.7.1", "Ley 996 de 2005"], 0, "El art. 86 de la Ley 1474 regula la audiencia de incumplimiento."),
  Q("Si un hecho imprevisible rompe la ecuación económica del contrato, aplica el principio de…", ["Planeación", "Equilibrio económico", "Publicidad"], 1, "El art. 27 de la Ley 80 protege el equilibrio de la ecuación contractual."),
 ]},

{"id": "m3", "etapa": "bases", "c": "Actores, roles y herramientas", "min": 15,
 "t": "Quién hace qué: actores, roles y herramientas",
 "obj": "identificar los roles de un proceso contractual en la Gobernación y las plataformas que se usan.",
 "html": """
<div class="scroll"><table class="stack"><thead><tr><th>Rol</th><th>Qué hace</th></tr></thead><tbody>
<tr><td data-l="Rol">Ordenador del gasto</td><td data-l="Qué hace">Decide, firma actos y contratos por delegación del Gobernador. Responde por la contratación de su dependencia.</td></tr>
<tr><td data-l="Rol">Área técnica (dependencia que necesita)</td><td data-l="Qué hace">Define la necesidad, elabora estudios previos, análisis del sector y especificaciones.</td></tr>
<tr><td data-l="Rol">Abogado / área jurídica</td><td data-l="Qué hace">Revisa modalidad, pliegos, minuta, actos; acompaña audiencias.</td></tr>
<tr><td data-l="Rol">Comité evaluador</td><td data-l="Qué hace">Verifica requisitos habilitantes y califica ofertas. Recomienda; no decide.</td></tr>
<tr><td data-l="Rol">Contratista</td><td data-l="Qué hace">Ejecuta el objeto, cumple obligaciones y paga su seguridad social.</td></tr>
<tr><td data-l="Rol">Supervisor</td><td data-l="Qué hace">Servidor de la entidad que vigila la ejecución: técnica, administrativa, financiera, contable y jurídica.</td></tr>
<tr><td data-l="Rol">Interventor</td><td data-l="Qué hace">Persona externa contratada para vigilar contratos complejos; obligatorio en obra que resulta de licitación.</td></tr>
<tr><td data-l="Rol">Hacienda</td><td data-l="Qué hace">Expide CDP y RP, tramita pagos.</td></tr>
<tr><td data-l="Rol">Organismos de control</td><td data-l="Qué hace">Contraloría General de Antioquia (fiscal), Procuraduría (disciplinario), Fiscalía (penal).</td></tr>
</tbody></table></div>
<h3>Herramientas</h3>
<ul>
<li><b>SECOP II:</b> plataforma de Colombia Compra Eficiente donde se publica, se presentan ofertas, se evalúa y se firma.</li>
<li><b>Tienda Virtual del Estado:</b> compras por Acuerdo Marco de Precios.</li>
<li><b>Mercurio:</b> gestión documental y radicados de la Gobernación.</li>
<li><b>RUP:</b> Registro Único de Proponentes, en la Cámara de Comercio; acredita experiencia y capacidad.</li>
<li><b>Datos abiertos (datos.gov.co):</b> consulta pública de contratos de SECOP II.</li>
</ul>
""",
 "gob": "En la Secretaría de Infraestructura Física la Subsecretaría Operativa lidera la contratación, supervisión e interventoría de obras; la Dirección de Asuntos Legales revisa actos, contratos, liquidaciones y procesos sancionatorios.",
 "err": "El supervisor no puede modificar el contrato, autorizar trabajos no pactados ni delegar su función. Todo cambio requiere una modificación firmada por el ordenador del gasto.",
 "quiz": [
  Q("¿Quién vigila un contrato de obra que resultó de una licitación pública?", ["Solo el supervisor de planta", "Un interventor externo, obligatorio en ese caso", "El comité evaluador"], 1, "En la obra licitada la interventoría debe contratarse con una persona independiente (Ley 80, art. 32, num. 1)."),
  Q("El comité evaluador…", ["Adjudica el contrato", "Verifica y recomienda; decide el ordenador", "Firma el contrato"], 1, "El comité recomienda; la decisión es del ordenador del gasto."),
  Q("¿Dónde acredita el proponente su experiencia y capacidad financiera?", ["En el RUP", "En Mercurio", "En la Gaceta"], 0, "El RUP, administrado por las cámaras de comercio."),
 ]},

# ------------------------------------------------------------------ PLANEACIÓN
{"id": "m4", "etapa": "plan", "c": "Planeación y estudios previos", "min": 25,
 "t": "La planeación: de la necesidad al estudio previo",
 "obj": "seguir la lista de planeación y redactar los elementos mínimos de un estudio previo.",
 "html": """
<p>La mayoría de los problemas de un contrato nacen aquí. La planeación responde: <b>qué</b> necesito, <b>por qué</b>, <b>cuánto cuesta</b>, <b>con qué plata</b>, <b>cómo lo voy a elegir</b> y <b>qué puede salir mal</b>.</p>
<h3>Lista de planeación</h3>
<ol>
<li>Necesidad inscrita en el <b>Plan Anual de Adquisiciones</b> (PAA), publicado antes del 31 de enero.</li>
<li>Si es inversión: proyecto en el banco de proyectos y en el Plan de Desarrollo (programa e indicador).</li>
<li><b>CDP</b> (certificado de disponibilidad presupuestal) por el valor estimado; vigencias futuras si el plazo pasa de un año.</li>
<li><b>Análisis del sector</b>: mercado, precios históricos en SECOP, cotizaciones, oferentes posibles, aspectos legales, financieros y técnicos.</li>
<li><b>Estudios previos</b> completos.</li>
<li><b>Matriz de riesgos</b>.</li>
<li>Requisitos habilitantes proporcionales y factores de evaluación.</li>
<li>¿Hay Documento Tipo? ¿Hay Acuerdo Marco?</li>
<li>En obras: licencias, permisos, predios y diseños listos (maduración, Ley 1474, art. 87).</li>
<li>Revisión del comité de contratación según el manual; revisión de Ley de Garantías y de régimen de emergencia.</li>
</ol>
<h3>Contenido mínimo del estudio previo (Decreto 1082, art. 2.2.1.1.2.1.1)</h3>
<ul>
<li>Descripción de la necesidad.</li>
<li>Objeto, especificaciones, autorizaciones, permisos y licencias.</li>
<li>Modalidad de selección y su justificación con fundamentos jurídicos.</li>
<li>Valor estimado y su justificación (cómo se calculó).</li>
<li>Criterios para seleccionar la oferta más favorable.</li>
<li>Análisis de riesgos y forma de mitigarlos.</li>
<li>Garantías exigidas.</li>
<li>Si aplica, acuerdos comerciales.</li>
</ul>
<p>Desde la vigencia gradual del <b>Decreto 0997 de 2026</b> (para Antioquia, ≈ mayo de 2027), el estudio previo y el análisis del sector deben considerar impactos del ciclo de vida y criterios ambientales o sociales, o justificar por qué no se incluyen.</p>
""",
 "gob": "Los presupuestos de obra de la Secretaría de Infraestructura se construyen con APU (análisis de precios unitarios) y AIU (administración, imprevistos y utilidad). Antes de abrir un proceso de obra se usa una lista de maduración: diseños, predios, permisos ambientales, redes y presupuesto.",
 "err": "Copiar el estudio previo de otro proceso sin ajustar la necesidad ni el valor. El análisis del sector debe ser del mercado actual y proporcional al proceso.",
 "caso": {"t": "el presupuesto sin soporte", "p": "El área técnica fija el valor de un contrato con una sola cotización enviada por la empresa que \"siempre lo hace\".", "r": "Una cotización no basta para justificar el valor. Se requieren varias fuentes (cotizaciones de distintos proveedores, precios históricos en SECOP II, Tienda Virtual) y dejar la memoria del cálculo en el análisis del sector."},
 "quiz": [
  Q("¿Qué documento certifica que hay recursos antes de abrir el proceso?", ["RP", "CDP", "Acta de inicio"], 1, "El CDP certifica disponibilidad; el RP se expide después, al comprometer el recurso con el contrato."),
  Q("El Plan Anual de Adquisiciones debe publicarse…", ["Antes del 31 de enero", "En diciembre", "Solo si lo pide la Contraloría"], 0, "Se publica en SECOP II y en la web antes del 31 de enero, con sus actualizaciones."),
  Q("El principio de maduración en obras exige…", ["Firmar rápido y diseñar después", "Tener estudios, diseños, permisos y predios antes de contratar", "Contratar solo con documentos tipo"], 1, "Art. 87 de la Ley 1474: los proyectos deben estar maduros antes de abrir el proceso."),
 ]},

{"id": "m5", "etapa": "plan", "c": "Requisitos y riesgos", "min": 20,
 "t": "Requisitos habilitantes, factores de evaluación y riesgos",
 "obj": "distinguir lo que habilita de lo que otorga puntaje y armar una matriz de riesgos básica.",
 "html": """
<h3>Habilitar no es puntuar</h3>
<div class="scroll"><table class="stack"><thead><tr><th></th><th>Requisitos habilitantes</th><th>Factores de evaluación</th></tr></thead><tbody>
<tr><td data-l="">Para qué</td><td data-l="Habilitantes">Saber si el proponente puede participar</td><td data-l="Evaluación">Escoger la mejor oferta entre los habilitados</td></tr>
<tr><td data-l="">Qué incluyen</td><td data-l="Habilitantes">Capacidad jurídica, financiera, organizacional y experiencia</td><td data-l="Evaluación">Calidad, precio, apoyo a la industria nacional, Mipymes, personas con discapacidad, sostenibilidad</td></tr>
<tr><td data-l="">Resultado</td><td data-l="Habilitantes">Cumple / no cumple (sin puntaje)</td><td data-l="Evaluación">Puntaje</td></tr>
<tr><td data-l="">¿Se subsana?</td><td data-l="Habilitantes">Sí, lo que no asigne puntaje, hasta el traslado del informe de evaluación (Ley 1882)</td><td data-l="Evaluación">No: lo que da puntaje no se mejora después del cierre</td></tr>
</tbody></table></div>
<p>Los requisitos deben ser <b>proporcionales</b> al valor y la complejidad. Pedir experiencia o indicadores exagerados reduce la competencia y es causal de observación de los entes de control.</p>
<h3>La matriz de riesgos (Ley 1150, art. 4)</h3>
<p>Riesgo es un evento que puede afectar el contrato. Para cada uno se registra: descripción, etapa, tipo, probabilidad (1 a 5), impacto (1 a 5), valoración, <b>a quién se asigna</b>, tratamiento y responsable del monitoreo.</p>
<div class="scroll"><table class="stack"><thead><tr><th>Riesgo de ejemplo</th><th>Prob.</th><th>Imp.</th><th>Asignado a</th><th>Tratamiento</th></tr></thead><tbody>
<tr><td data-l="Riesgo">Lluvias que impiden el acceso a frentes de obra</td><td data-l="Prob.">3</td><td data-l="Imp.">4</td><td data-l="Asignado">Compartido</td><td data-l="Tratamiento">Plan de contingencia, cronograma con holguras, suspensión documentada</td></tr>
<tr><td data-l="Riesgo">Pocos oferentes por requisitos desproporcionados</td><td data-l="Prob.">2</td><td data-l="Imp.">3</td><td data-l="Asignado">Entidad</td><td data-l="Tratamiento">Análisis del sector y requisitos proporcionales</td></tr>
<tr><td data-l="Riesgo">Supervisión insuficiente</td><td data-l="Prob.">2</td><td data-l="Imp.">4</td><td data-l="Asignado">Entidad</td><td data-l="Tratamiento">Supervisor con perfil y carga razonable</td></tr>
</tbody></table></div>
<p>Los riesgos <b>imprevisibles</b> no se trasladan al contratista: si ocurren, se restablece el equilibrio. Use el Manual para la identificación y cobertura del riesgo de Colombia Compra Eficiente (versión vigente).</p>
""",
 "err": "Poner en la matriz riesgos genéricos (\"incumplimiento del contratista\") sin tratamiento ni responsable. Cada riesgo debe ser específico del proceso y tener un control.",
 "quiz": [
  Q("La experiencia del proponente es…", ["Un factor de puntaje siempre", "Normalmente un requisito habilitante", "Un riesgo"], 1, "La experiencia habilita; la experiencia adicional puede puntuar solo si el pliego lo prevé (por ejemplo, en concurso)."),
  Q("Un proponente olvidó un certificado que no da puntaje. ¿Qué pasa?", ["Se rechaza de inmediato", "Puede subsanarlo hasta el traslado del informe de evaluación", "Se le suman puntos"], 1, "Ley 1882 de 2018: lo que no asigne puntaje es subsanable dentro de ese término."),
  Q("Los riesgos imprevisibles…", ["Se asignan siempre al contratista", "No se trasladan; si ocurren se restablece el equilibrio", "No existen en la contratación pública"], 1, "Rompen la ecuación contractual (Ley 80, art. 27)."),
 ]},

# ------------------------------------------------------------------ SELECCIÓN
{"id": "m6", "etapa": "sel", "c": "Modalidades y cuantías", "min": 25,
 "t": "Las cinco modalidades de selección y las cuantías 2026",
 "obj": "elegir la modalidad correcta según el objeto y el valor, con las cuantías del Departamento para 2026.",
 "html": """
<h3>Cuantías del Departamento 2026 (cálculo)</h3>
<p>SMMLV 2026: <b>$ 1.750.905</b> (Decreto 159 de 2026, transitorio). Para entidades con presupuesto de 1.200.000 SMMLV o más, la menor cuantía es hasta 1.000 SMMLV, y la mínima cuantía hasta el 10 % de la menor.</p>
<div class="scroll"><table><thead><tr><th>Cuantía</th><th>SMMLV</th><th>Valor 2026</th></tr></thead><tbody>
<tr><td>Mínima cuantía (tope)</td><td class="n">100</td><td class="n">$ 175.090.500</td></tr>
<tr><td>Menor cuantía (tope)</td><td class="n">1.000</td><td class="n">$ 1.750.905.000</td></tr>
</tbody></table></div>
<p class="meta">Cálculo: 1.000 × $ 1.750.905 y 10 % de ese valor. Confirme con la publicación oficial de cuantías del Departamento.</p>
<h3>Las modalidades</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Modalidad</th><th>Cuándo</th><th>Cómo se elige</th></tr></thead><tbody>
<tr><td data-l="Modalidad"><b>Licitación pública</b></td><td data-l="Cuándo">Regla general; obra y lo que no encaje en otra modalidad, por encima de la menor cuantía</td><td data-l="Cómo">Calidad-precio o costo-beneficio; adjudicación en audiencia pública</td></tr>
<tr><td data-l="Modalidad"><b>Selección abreviada</b></td><td data-l="Cuándo">Menor cuantía; bienes y servicios de características técnicas uniformes (subasta, acuerdo marco, bolsa); declaratoria de desierta de licitación; otros casos del art. 2, num. 2</td><td data-l="Cómo">Menor precio (uniformes) o calidad-precio (menor cuantía)</td></tr>
<tr><td data-l="Modalidad"><b>Concurso de méritos</b></td><td data-l="Cuándo">Consultoría: estudios, diseños, interventoría, asesoría técnica</td><td data-l="Cómo">Por calidad; el precio no es factor de evaluación</td></tr>
<tr><td data-l="Modalidad"><b>Contratación directa</b></td><td data-l="Cuándo">Solo causales taxativas: urgencia manifiesta, interadministrativos, prestación de servicios profesionales y de apoyo, no pluralidad de oferentes, arrendamiento o compra de inmuebles, empréstitos, entre otras</td><td data-l="Cómo">Idoneidad y experiencia; acto de justificación cuando lo exige la norma</td></tr>
<tr><td data-l="Modalidad"><b>Mínima cuantía</b></td><td data-l="Cuándo">Cualquier objeto con valor hasta la mínima cuantía</td><td data-l="Cómo">Menor precio; la aceptación de la oferta es el contrato</td></tr>
</tbody></table></div>
<h3>Prestación de servicios: requisitos</h3>
<ol>
<li>Necesidad en el PAA y estudio previo.</li>
<li>Certificado de inexistencia o insuficiencia de personal de planta.</li>
<li>Idoneidad y experiencia acreditadas.</li>
<li>CDP, verificación de inhabilidades y antecedentes, SIGEP II.</li>
<li>Sin subordinación ni funciones permanentes (Corte Constitucional, C-614 de 2009 y C-171 de 2012).</li>
<li>Seguridad social como independiente; publicación en SECOP II; RP.</li>
</ol>
""",
 "gob": "Use la herramienta \"¿Qué modalidad corresponde?\" de este curso para una primera orientación con las cuantías 2026.",
 "err": "Fraccionar un contrato (dividir una compra grande en varias pequeñas) para usar mínima cuantía o evitar la licitación. Es una falta grave y vulnera la selección objetiva.",
 "caso": {"t": "la interventoría de una vía", "p": "La Secretaría de Infraestructura necesita contratar la interventoría de una obra vial de $ 9.000 millones. Un compañero propone hacerlo por selección abreviada de menor cuantía \"porque es más rápido\".", "r": "La interventoría es consultoría: se contrata por concurso de méritos (salvo que su valor fuera de mínima cuantía), y en infraestructura de transporte con el Documento Tipo de interventoría versión 3. La selección abreviada de menor cuantía no aplica a consultoría."},
 "quiz": [
  Q("Un estudio de diseños por $ 600 millones se contrata por…", ["Licitación pública", "Concurso de méritos", "Mínima cuantía"], 1, "Es consultoría por encima de la mínima cuantía."),
  Q("Compra de papelería por $ 40 millones (Departamento, 2026):", ["Mínima cuantía o acuerdo marco si existe", "Licitación", "Contratación directa"], 0, "Está por debajo de $ 175.090.500; si hay Acuerdo Marco en la Tienda Virtual, revíselo primero."),
  Q("Dividir una compra en partes para no licitar se llama…", ["Economía procesal", "Fraccionamiento, y está prohibido", "Selección abreviada"], 1, "El fraccionamiento elude la modalidad que corresponde."),
  Q("¿Cuál es una causal de contratación directa?", ["Que el contratista sea conocido", "Contratos interadministrativos", "Que haya poco tiempo"], 1, "Ley 1150, art. 2, num. 4, lit. c."),
 ]},

{"id": "m7", "etapa": "sel", "c": "El proceso paso a paso", "min": 30,
 "t": "El proceso de selección paso a paso",
 "obj": "seguir las etapas de una licitación, de una mínima cuantía y de una contratación directa en SECOP II.",
 "html": """
<h3>Licitación pública (modelo de todas las competitivas)</h3>
<ol>
<li><b>Aviso de convocatoria</b> en SECOP II.</li>
<li><b>Proyecto de pliego</b> publicado al menos <b>10 días hábiles</b> antes de la apertura; observaciones y respuestas publicadas.</li>
<li><b>Acto de apertura</b> motivado y <b>pliego definitivo</b>, con cláusulas y pacto anticorrupción (Decreto 0997 de 2026).</li>
<li><b>Audiencia de asignación de riesgos y aclaraciones</b>, dentro de los 3 días hábiles siguientes al inicio del plazo para ofertar.</li>
<li><b>Adendas</b> dentro de los plazos permitidos antes del cierre.</li>
<li><b>Cierre</b> y apertura de ofertas en SECOP II.</li>
<li><b>Evaluación</b> por el comité: habilitantes, consulta de listas restrictivas internacionales, puntaje; ofertas artificialmente bajas se explican.</li>
<li><b>Informe de evaluación</b> en traslado <b>5 días hábiles</b>; observaciones y subsanaciones.</li>
<li><b>Audiencia de adjudicación</b>, o declaratoria de desierta motivada.</li>
</ol>
<h3>Mínima cuantía</h3>
<ol>
<li>Estudio previo sencillo y CDP.</li>
<li>Invitación pública por al menos <b>1 día hábil</b>.</li>
<li>Se verifica primero la oferta de <b>menor precio</b>; si cumple, gana. Si no, se revisa la siguiente.</li>
<li><b>Aceptación de la oferta</b>: con ella queda celebrado el contrato.</li>
</ol>
<h3>Contratación directa</h3>
<ol>
<li>Estudio previo que justifique la causal.</li>
<li><b>Acto administrativo de justificación</b> (no se exige en prestación de servicios ni en algunos otros casos).</li>
<li>Verificación de idoneidad, inhabilidades y antecedentes.</li>
<li>Contrato en SECOP II, RP, garantías si aplican.</li>
</ol>
<p>Todo documento del proceso se publica en SECOP II dentro de los <b>3 días hábiles</b> siguientes a su expedición.</p>
""",
 "err": "Responder observaciones de forma genérica (\"se acoge parcialmente\") o publicar adendas fuera de plazo. Cada observación merece una respuesta motivada, y una adenda tardía puede viciar el proceso.",
 "caso": {"t": "el único proponente", "p": "En una licitación se presenta un solo oferente y cumple todo.", "r": "Puede adjudicarse: un oferente habilitado cuya oferta sea favorable basta. Si nadie se presenta o nadie cumple, se declara desierta por acto motivado y puede seguirse una selección abreviada en las condiciones de la norma."},
 "quiz": [
  Q("En licitación, el proyecto de pliego se publica con al menos…", ["1 día hábil", "5 días hábiles", "10 días hábiles"], 2, "Diez días hábiles antes del acto de apertura."),
  Q("En mínima cuantía, ¿qué hace el contrato?", ["El acta de inicio", "La aceptación de la oferta", "La audiencia de adjudicación"], 1, "La comunicación de aceptación junto con la oferta constituyen el contrato."),
  Q("El informe de evaluación de una licitación queda en traslado…", ["5 días hábiles", "1 día", "30 días"], 0, "Cinco días hábiles para observaciones."),
  Q("Desde 2026 los pliegos competitivos deben incluir…", ["Cláusulas y pacto anticorrupción", "Póliza de vida", "Un sorteo obligatorio"], 0, "Decreto 0997 de 2026, vigencia inmediata."),
 ]},

{"id": "m8", "etapa": "sel", "c": "Documentos Tipo", "min": 15,
 "t": "Documentos Tipo: pliegos que no se pueden cambiar",
 "obj": "saber cuándo es obligatorio un Documento Tipo, qué versión aplicar y qué no se puede modificar.",
 "html": """
<p>Los <b>Documentos Tipo</b> son pliegos estándar que expide Colombia Compra Eficiente. Son <b>obligatorios e inalterables</b> (Ley 2022 de 2020) en los requisitos habilitantes y los factores técnicos, económicos y de ponderación. La entidad solo diligencia lo que el documento permite (presupuesto, plazo, rangos).</p>
<h3>Sectores con Documento Tipo</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Sector</th><th>Versiones a noviembre de 2026</th></tr></thead><tbody>
<tr><td data-l="Sector">Infraestructura de transporte</td><td data-l="Versión">Licitación de obra v4 (desde 3-feb-2025); mínima cuantía v2 con modificaciones de la Resolución 464 (desde 3-feb-2025); interventoría por concurso v3</td></tr>
<tr><td data-l="Sector">Agua potable y saneamiento básico</td><td data-l="Versión">Obra v2 (Resolución 546 del 14-sept-2026)</td></tr>
<tr><td data-l="Sector">Infraestructura social</td><td data-l="Versión">Licitación, menor cuantía, mínima cuantía, consultoría e interventoría (Resoluciones 539, 540, 952 y 953 de 2025), obligatorias desde el 16-feb-2026</td></tr>
<tr><td data-l="Sector">Convenios solidarios y gestión catastral</td><td data-l="Versión">Consultar versión vigente</td></tr>
</tbody></table></div>
<h3>Cómo usarlos</h3>
<ol>
<li>Revise la <b>Matriz 1 – Experiencia</b> del sector para saber si su actividad está cubierta.</li>
<li>Descargue la versión vigente a la <b>fecha del aviso de convocatoria</b> (control de versiones en colombiacompra.gov.co).</li>
<li>No agregue requisitos ni cambie puntajes; diligencie solo los espacios permitidos.</li>
</ol>
""",
 "err": "Agregar \"un requisito más\" a un Documento Tipo (por ejemplo, más experiencia o un indicador financiero distinto). Es ilegal y es uno de los hallazgos más comunes.",
 "quiz": [
  Q("¿Qué versión de Documento Tipo se aplica?", ["La vigente a la fecha del aviso de convocatoria", "La que tenga el abogado guardada", "La más antigua"], 0, "El hito es la publicación del aviso."),
  Q("En un Documento Tipo, la entidad puede…", ["Cambiar la experiencia exigida", "Diligenciar solo las variables permitidas", "Eliminar factores de puntaje"], 1, "Los habilitantes y factores son inalterables."),
  Q("La licitación de obra de transporte va en la versión…", ["2", "4", "1"], 1, "Versión 4, desde el 3 de febrero de 2025."),
 ]},

# ------------------------------------------------------------------ EJECUCIÓN
{"id": "m9", "etapa": "ejec", "c": "Firma, legalización y garantías", "min": 20,
 "t": "Celebración, legalización y garantías",
 "obj": "conocer los requisitos de perfeccionamiento y de ejecución y los amparos de las garantías.",
 "html": """
<h3>Perfeccionar y ejecutar no es lo mismo</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Momento</th><th>Requisito</th></tr></thead><tbody>
<tr><td data-l="Momento">Perfeccionamiento</td><td data-l="Requisito">Acuerdo sobre objeto y precio, por escrito (firma en SECOP II) — Ley 80, art. 41</td></tr>
<tr><td data-l="Momento">Ejecución</td><td data-l="Requisito">Registro presupuestal (RP) y aprobación de la garantía; afiliación a seguridad social; acta de inicio si el contrato la prevé</td></tr>
</tbody></table></div>
<h3>Cláusulas que no pueden faltar en la minuta</h3>
<p>Objeto, valor, forma de pago, plazo, obligaciones, garantías, cláusulas excepcionales cuando proceden, multas y cláusula penal, indemnidad, supervisión, solución de controversias, uso de la marca institucional, cláusulas anticorrupción, protección de datos.</p>
<h3>Garantías más usadas</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Amparo</th><th>Cubre</th></tr></thead><tbody>
<tr><td data-l="Amparo">Seriedad de la oferta</td><td data-l="Cubre">Que el proponente firme si gana</td></tr>
<tr><td data-l="Amparo">Cumplimiento</td><td data-l="Cubre">Las obligaciones del contrato; incluye buen manejo del anticipo si lo hay</td></tr>
<tr><td data-l="Amparo">Salarios y prestaciones sociales</td><td data-l="Cubre">Obligaciones laborales del contratista con su personal</td></tr>
<tr><td data-l="Amparo">Calidad del servicio / de los bienes</td><td data-l="Cubre">Defectos después de la entrega</td></tr>
<tr><td data-l="Amparo">Estabilidad y calidad de la obra</td><td data-l="Cubre">Daños de la obra después del recibo; vigencia no inferior a 5 años salvo justificación técnica</td></tr>
<tr><td data-l="Amparo">Responsabilidad civil extracontractual</td><td data-l="Cubre">Daños a terceros; obligatoria en obra</td></tr>
</tbody></table></div>
""",
 "err": "Firmar el acta de inicio sin el RP o sin la garantía aprobada. El contrato existe, pero no puede ejecutarse; lo que se ejecute antes queda sin respaldo.",
 "quiz": [
  Q("El contrato estatal se perfecciona con…", ["El acta de inicio", "El acuerdo sobre objeto y precio por escrito", "El primer pago"], 1, "Ley 80, art. 41."),
  Q("Para iniciar la ejecución se requiere…", ["RP y garantía aprobada", "Solo la firma", "La liquidación"], 0, "Son requisitos de ejecución."),
  Q("La garantía de estabilidad de una obra dura por regla general…", ["6 meses", "Mínimo 5 años desde el recibo", "Hasta la liquidación"], 1, "Decreto 1082, art. 2.2.1.2.3.1.14."),
 ]},

{"id": "m10", "etapa": "ejec", "c": "Supervisión y modificaciones", "min": 25,
 "t": "Supervisión, interventoría y modificaciones",
 "obj": "ejercer la supervisión, revisar un pago y tramitar adiciones, prórrogas y suspensiones con sus límites.",
 "html": """
<h3>El supervisor (Ley 1474, arts. 82-85)</h3>
<p>Hace seguimiento <b>técnico, administrativo, financiero, contable y jurídico</b>. Puede pedir informes y explicaciones, y debe avisar a la entidad sobre posibles incumplimientos o actos de corrupción. Responde civil, fiscal, penal y disciplinariamente.</p>
<h3>Antes de cada pago</h3>
<ul>
<li>Informe de supervisión con evidencias por obligación.</li>
<li>Factura o cuenta de cobro según el régimen tributario.</li>
<li>Pago de seguridad social y parafiscales del periodo (personas naturales: base del 40 % del valor mensual).</li>
<li>Garantías vigentes y publicación en SECOP II.</li>
</ul>
<h3>Modificaciones</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Tipo</th><th>Requisitos</th><th>Límite</th></tr></thead><tbody>
<tr><td data-l="Tipo">Adición</td><td data-l="Requisitos">Justificación técnica y presupuestal, CDP y RP, ampliación de garantías, contrato vigente</td><td data-l="Límite">50 % del valor inicial expresado en SMMLV (Ley 80, art. 40). Excepciones: interventoría (Ley 1474, art. 85), APP, emergencia del sismo (Decreto Legislativo 1420 de 2026)</td></tr>
<tr><td data-l="Tipo">Prórroga</td><td data-l="Requisitos">Justificación; contrato vigente; garantías ampliadas</td><td data-l="Límite">Nunca sobre un contrato vencido</td></tr>
<tr><td data-l="Tipo">Suspensión</td><td data-l="Requisitos">Fuerza mayor, caso fortuito o interés público; acta motivada</td><td data-l="Límite">Acta de reinicio y ajuste de garantías</td></tr>
<tr><td data-l="Tipo">Cesión</td><td data-l="Requisitos">Autorización escrita; cesionario con iguales o mejores condiciones</td><td data-l="Límite">—</td></tr>
</tbody></table></div>
<h3>Señales de alerta</h3>
<ul><li>Avance financiero mayor que el físico.</li><li>Cambio de personal clave sin autorización.</li><li>Facturas sin entregables.</li><li>Mayores cantidades de obra ejecutadas sin acta ni respaldo presupuestal.</li></ul>
""",
 "gob": "En obras de infraestructura las actas de medición, de precios no previstos y de mayores cantidades se firman con la interventoría antes de ejecutar lo nuevo, con disponibilidad presupuestal.",
 "err": "\"Prorrogar\" un contrato el día después de su vencimiento. Un contrato vencido no se puede modificar; la prórroga se firma mientras está vigente.",
 "caso": {"t": "la adición", "p": "Un contrato de $ 400 millones firmado en 2026 necesita una adición de $ 230 millones.", "r": "El tope general es el 50 % del valor inicial en SMMLV: $ 400.000.000 / $ 1.750.905 ≈ 228,45 SMMLV; el 50 % ≈ 114,23 SMMLV ≈ $ 200 millones. Una adición de $ 230 millones lo supera; salvo una excepción legal (por ejemplo, la emergencia del sismo para contratos conexos), hay que revisar el alcance o adelantar un nuevo proceso."},
 "quiz": [
  Q("¿Puede el supervisor autorizar verbalmente un trabajo no pactado?", ["Sí, si es urgente", "No; requiere modificación firmada por el ordenador", "Sí, si lo anota en la bitácora"], 1, "El supervisor no modifica el contrato."),
  Q("El límite general para adicionar un contrato es…", ["100 %", "50 % del valor inicial en SMMLV", "No hay límite"], 1, "Parágrafo del art. 40 de la Ley 80."),
  Q("Antes de pagar a un contratista persona natural se verifica…", ["Su pago de seguridad social del periodo", "Su declaración de renta", "Nada"], 0, "Art. 50 Ley 789 de 2002 y art. 23 Ley 1150."),
 ]},

{"id": "m11", "etapa": "ejec", "c": "Incumplimiento y sanciones", "min": 20,
 "t": "Incumplimiento: multas, cláusula penal y caducidad",
 "obj": "documentar un presunto incumplimiento y seguir la audiencia del artículo 86 de la Ley 1474.",
 "html": """
<h3>Las consecuencias posibles</h3>
<ul>
<li><b>Multa:</b> apremia al contratista a cumplir mientras el contrato está en ejecución.</li>
<li><b>Cláusula penal:</b> tasación anticipada de perjuicios por incumplimiento.</li>
<li><b>Caducidad:</b> la más grave; termina el contrato por incumplimiento que lo paraliza o afecta de manera grave, y genera inhabilidad.</li>
<li><b>Declaratoria de incumplimiento:</b> para hacer efectiva la garantía.</li>
</ul>
<h3>Procedimiento (Ley 1474, art. 86)</h3>
<ol>
<li><b>Informe del supervisor o interventor</b>: hechos, obligaciones incumplidas, pruebas y tasación.</li>
<li><b>Citación</b> al contratista y a la aseguradora: hechos, normas o cláusulas y consecuencias posibles.</li>
<li><b>Audiencia</b>: se presenta el caso, el contratista y el garante presentan descargos y pruebas.</li>
<li><b>Decisión motivada</b> en audiencia, con recurso de reposición que se resuelve en ella.</li>
<li>La audiencia puede suspenderse; el procedimiento termina si cesa el incumplimiento.</li>
<li>Reporte de multas y sanciones en firme a la Cámara de Comercio para el RUP (Decreto 0997 de 2026).</li>
</ol>
<p>Consulte la Guía de Colombia Compra Eficiente para el proceso sancionatorio contractual (2026).</p>
""",
 "err": "Iniciar el procedimiento sin un informe que relacione cada obligación incumplida con su prueba. Sin ese soporte, la decisión se cae en el recurso o ante el juez.",
 "quiz": [
  Q("¿Quién debe llamarse a la audiencia del art. 86 además del contratista?", ["La aseguradora (garante)", "La Fiscalía", "Los demás proponentes"], 0, "Se cita al contratista y al garante."),
  Q("La sanción que termina el contrato y genera inhabilidad es…", ["La multa", "La caducidad", "El apremio"], 1, "La caducidad."),
  Q("Las multas en firme se reportan…", ["A la Cámara de Comercio para el RUP", "Solo a la prensa", "A nadie"], 0, "Reporte mensual (Decreto 0997 de 2026)."),
 ]},

# ------------------------------------------------------------------ CIERRE Y ESPECIALES
{"id": "m12", "etapa": "cierre", "c": "Liquidación y cierre", "min": 15,
 "t": "Terminación, liquidación y cierre del expediente",
 "obj": "liquidar un contrato en los plazos legales y cerrar el expediente.",
 "html": """
<h3>Pasos</h3>
<ol>
<li>Recibo a satisfacción: técnico, administrativo y financiero.</li>
<li>Balance financiero: valor total, pagado y saldo a liberar del RP.</li>
<li>Verificación de aportes a seguridad social durante toda la ejecución.</li>
<li>Ampliación de garantías posteriores (estabilidad, calidad, salarios) si corresponde.</li>
<li>Acta de liquidación con salvedades si las hay.</li>
<li>Cierre del expediente en SECOP II y en el archivo.</li>
</ol>
<h3>Plazos (Ley 1150, art. 11)</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Liquidación</th><th>Plazo</th></tr></thead><tbody>
<tr><td data-l="Liquidación">Bilateral (de común acuerdo)</td><td data-l="Plazo">El del pliego o el contrato; si no hay, 4 meses desde la terminación</td></tr>
<tr><td data-l="Liquidación">Unilateral (la entidad)</td><td data-l="Plazo">Dentro de los 2 meses siguientes, si el contratista no se presenta o no hay acuerdo</td></tr>
<tr><td data-l="Liquidación">Después</td><td data-l="Plazo">Bilateral o unilateral hasta el vencimiento del término para demandar (2 años, art. 164 CPACA)</td></tr>
</tbody></table></div>
<p>Los contratos de prestación de servicios profesionales y de apoyo a la gestión no requieren liquidación obligatoria (Ley 80, art. 60, modificado por el Decreto-Ley 019 de 2012); igual se deja constancia de cierre.</p>
""",
 "gob": "En 2025 la Secretaría de Infraestructura liquidó 61 convenios con municipios en coordinación con su Dirección de Asuntos Legales: los convenios también se liquidan y los saldos no ejecutados se reintegran.",
 "err": "Dejar vencer el plazo para liquidar. Cuando vence el término para demandar se pierde la competencia para liquidar y quedan saldos y garantías sin definir.",
 "quiz": [
  Q("Si el contrato no dice nada, la liquidación bilateral se hace dentro de…", ["4 meses desde la terminación", "10 días", "5 años"], 0, "Ley 1150, art. 11."),
  Q("La entidad puede liquidar unilateralmente dentro de…", ["Los 2 meses siguientes al término bilateral", "1 semana", "Nunca"], 0, "Ley 1150, art. 11."),
  Q("Los contratos de prestación de servicios profesionales…", ["No requieren liquidación obligatoria", "Siempre se liquidan judicialmente", "Se liquidan a los 5 años"], 0, "Art. 60 Ley 80, modificado por el Decreto-Ley 019 de 2012."),
 ]},

{"id": "m13", "etapa": "cierre", "c": "Obra e infraestructura", "min": 25,
 "t": "Contratar obra e infraestructura (Secretaría de Infraestructura Física)",
 "obj": "aplicar las reglas propias de obra, interventoría y consultoría de infraestructura.",
 "html": """
<h3>Qué contrato y qué modalidad</h3>
<div class="scroll"><table class="stack"><thead><tr><th>Necesidad</th><th>Modalidad</th></tr></thead><tbody>
<tr><td data-l="Necesidad">Construcción, mejoramiento, pavimentación por encima de la menor cuantía</td><td data-l="Modalidad">Licitación pública con Documento Tipo de transporte v4</td></tr>
<tr><td data-l="Necesidad">Obra hasta la menor o mínima cuantía</td><td data-l="Modalidad">Selección abreviada de menor cuantía o mínima cuantía, con el Documento Tipo que corresponda</td></tr>
<tr><td data-l="Necesidad">Interventoría y estudios y diseños</td><td data-l="Modalidad">Concurso de méritos (interventoría de transporte: Documento Tipo v3)</td></tr>
<tr><td data-l="Necesidad">Red terciaria con municipios</td><td data-l="Modalidad">Convenio interadministrativo (directa)</td></tr>
<tr><td data-l="Necesidad">Obras con juntas de acción comunal</td><td data-l="Modalidad">Convenio solidario, con límites legales</td></tr>
<tr><td data-l="Necesidad">Infraestructura de largo plazo con capital privado</td><td data-l="Modalidad">Asociación Público Privada (Ley 1508 de 2012)</td></tr>
</tbody></table></div>
<h3>Cinco reglas de la obra pública</h3>
<ol>
<li><b>Interventoría externa obligatoria</b> si la obra resulta de licitación pública.</li>
<li><b>Anticipo</b> hasta el 50 % del valor; en obra (salvo menor y mínima cuantía) y en contratos por licitación se maneja en <b>fiducia o patrimonio autónomo</b> (Ley 1474, art. 91).</li>
<li><b>Estabilidad y calidad de la obra</b>: garantía no inferior a 5 años; la interventoría garantiza la calidad de su servicio por el mismo plazo.</li>
<li><b>Presupuesto con APU y AIU</b>; mayores cantidades y precios no previstos solo con acta, soporte técnico y disponibilidad presupuestal.</li>
<li><b>Maduración</b>: diseños, predios, permisos ambientales y redes antes de abrir el proceso; lo pendiente, asignado en la matriz de riesgos.</li>
</ol>
<h3>Documentos de la obra</h3>
<p>Acta de inicio, programa de obra e inversión del anticipo, bitácora, actas de medición, actas de precios no previstos y de mayores cantidades, actas de suspensión y reinicio, informes mensuales de interventoría, acta de recibo final y acta de liquidación.</p>
""",
 "gob": "La Secretaría de Infraestructura Física tiene una Subsecretaría Operativa (Desarrollo Físico; Gestión Social, Ambiental y Predial; Infraestructura y Apoyo Territorial) y una Subsecretaría de Planeación, Proyectos Estratégicos y APP (Estructuración de Proyectos; Instrumentos de Financiación), con las Direcciones de Asuntos Legales y Administrativa y Financiera (Decreto Ordenanzal 2024070003913 de 2024).",
 "err": "Ejecutar ítems no previstos y \"legalizarlos después\". Sin acta previa, soporte técnico de la interventoría y disponibilidad presupuestal, no hay cómo pagarlos y se abre la puerta a hallazgos fiscales.",
 "caso": {"t": "el anticipo", "p": "Un contrato de obra adjudicado por licitación prevé un anticipo del 30 %. El contratista pide que se le consigne en su cuenta corriente.", "r": "No procede: en contratos de obra adjudicados por licitación el anticipo se maneja en un patrimonio autónomo irrevocable (Ley 1474, art. 91), con garantía de buen manejo, y el supervisor o interventor puede pedir los soportes de pago a proveedores."},
 "quiz": [
  Q("En una obra licitada, el anticipo se maneja…", ["En la cuenta del contratista", "En fiducia o patrimonio autónomo", "En efectivo"], 1, "Ley 1474, art. 91."),
  Q("La interventoría de una obra vial se contrata por…", ["Concurso de méritos", "Subasta inversa", "Mínima cuantía siempre"], 0, "Es consultoría; Documento Tipo de interventoría de transporte v3."),
  Q("¿Qué se necesita antes de ejecutar un ítem no previsto?", ["Nada, se paga al final", "Acta con APU concertado y disponibilidad presupuestal", "Solo una llamada al supervisor"], 1, "Se formaliza antes y con respaldo presupuestal."),
 ]},

{"id": "m14", "etapa": "cierre", "c": "Alertas 2026", "min": 20,
 "t": "Lo nuevo y lo que viene: alertas 2026-2027",
 "obj": "aplicar los cambios normativos de 2026 y planear la contratación frente a la Ley de Garantías de 2027.",
 "html": """
<h3>Decreto 0997 de 2026 (4 de agosto)</h3>
<p><b>Desde el 6-ago-2026, para todos:</b> cláusulas y pacto anticorrupción en los pliegos de todas las modalidades competitivas; consulta y registro de listas restrictivas internacionales (aparecer en una lista no inhabilita automáticamente); reporte mensual de multas y sanciones a la Cámara de Comercio; caución para impugnar el RUP.</p>
<p><b>Gradual — compra pública sostenible:</b> para departamentos de categoría especial como Antioquia, 9 meses desde la publicación (≈ mayo de 2027; calcular con el texto oficial). Incluye PAA estratégico, análisis del sector con ciclo de vida, criterios ambientales y sociales y, en licitación y menor cuantía, oferta más favorable por calidad-precio o costo-beneficio. Los procesos con Documento Tipo siguen la norma anterior hasta que se actualice cada documento.</p>
<h3>Decreto 287 de 2026</h3>
<p>Cambió los incentivos para personas con discapacidad (arts. 2.2.1.2.4.2.6 a 2.2.1.2.4.2.8 del Decreto 1082). Lea el texto antes de definir el puntaje.</p>
<h3>Emergencia por el sismo del 10 de agosto de 2026</h3>
<p>Decreto Legislativo 1420 de 2026: urgencia manifiesta por ministerio del decreto, catálogos de emergencia y adiciones por encima del 50 %, <b>solo para contratos directa y específicamente conexos</b> con la atención del sismo. La publicación en SECOP II y el control fiscal se mantienen. Deje en el expediente la prueba de la conexidad (municipio, daño, reporte).</p>
<h3>Ley de Garantías — elecciones territoriales del 31 de octubre de 2027</h3>
<p>Desde 4 meses antes (≈ 30-jun-2027) gobernadores, secretarios y gerentes no pueden celebrar <b>convenios interadministrativos para ejecutar recursos</b> ni modificar la nómina, salvo excepciones (Ley 996, art. 38, parágrafo). Los procesos competitivos no se suspenden. El contrato debe quedar <b>perfeccionado</b> antes de la fecha. Confirme las fechas con la circular de Colombia Compra Eficiente.</p>
""",
 "err": "Usar la urgencia manifiesta del sismo para contratos que no tienen relación directa con la emergencia. Fuera de esa conexidad aplican las reglas ordinarias.",
 "caso": {"t": "el convenio de junio", "p": "Una dependencia planea firmar en julio de 2027 un convenio interadministrativo con un municipio para ejecutar recursos de placa huella.", "r": "Desde ≈ 30 de junio de 2027 rige la prohibición del parágrafo del art. 38 de la Ley 996. El convenio debe planearse en el PAA 2027 y firmarse antes, o ejecutarse por un proceso competitivo, que no se suspende."},
 "quiz": [
  Q("Las cláusulas anticorrupción del Decreto 0997 rigen…", ["Desde el 6 de agosto de 2026", "Desde 2028", "Solo en mínima cuantía"], 0, "Vigencia inmediata desde el día siguiente a la publicación."),
  Q("La urgencia manifiesta del Decreto Legislativo 1420 aplica a…", ["Cualquier contrato del Departamento", "Contratos directa y específicamente conexos con el sismo", "Solo a contratos de nómina"], 1, "Exige conexidad concreta."),
  Q("Desde ≈ 30-jun-2027 está prohibido…", ["Hacer licitaciones", "Celebrar convenios interadministrativos para ejecutar recursos", "Pagar contratistas"], 1, "Ley 996, art. 38, parágrafo."),
 ]},
]

GLOSARIO = [
 ["Acta de inicio", "Documento que marca el comienzo de la ejecución cuando el contrato la prevé."],
 ["Adenda", "Documento que modifica el pliego de condiciones durante el proceso, dentro de los plazos permitidos."],
 ["Adición", "Aumento del valor del contrato; tope general del 50 % del valor inicial en SMMLV."],
 ["AIU", "Administración, imprevistos y utilidad del presupuesto de obra."],
 ["Análisis del sector", "Estudio del mercado, precios, oferentes y aspectos legales y técnicos que soporta el proceso."],
 ["Anticipo", "Recursos entregados al contratista para iniciar; en obra licitada, en patrimonio autónomo."],
 ["APU", "Análisis de precios unitarios: desglose del costo de cada ítem de obra."],
 ["Acuerdo Marco de Precios", "Contrato de Colombia Compra Eficiente con proveedores para que las entidades compren por la Tienda Virtual."],
 ["Caducidad", "Sanción que termina el contrato por incumplimiento grave y genera inhabilidad."],
 ["CDP", "Certificado de disponibilidad presupuestal: hay recursos para el proceso."],
 ["Cláusula penal", "Tasación anticipada de perjuicios por incumplimiento."],
 ["Cláusulas excepcionales", "Poderes de la entidad: interpretación, modificación y terminación unilaterales, caducidad."],
 ["Comité evaluador", "Grupo que verifica y califica ofertas y recomienda la adjudicación."],
 ["Concurso de méritos", "Modalidad para consultoría; se elige por calidad."],
 ["Contratación directa", "Modalidad sin competencia, solo por causales legales."],
 ["Documento Tipo", "Pliego estándar obligatorio e inalterable en ciertos sectores (Ley 2022 de 2020)."],
 ["Estudios previos", "Documento que justifica la necesidad, el objeto, la modalidad, el valor, los riesgos y las garantías."],
 ["Fraccionamiento", "Dividir una contratación para eludir la modalidad que corresponde. Prohibido."],
 ["Garantía", "Póliza o instrumento que ampara la seriedad, el cumplimiento y otros riesgos."],
 ["Inhabilidad", "Impedimento legal para contratar con el Estado."],
 ["Interventoría", "Seguimiento externo especializado de un contrato; obligatoria en obra licitada."],
 ["Ley de Garantías", "Ley 996 de 2005: restricciones a la contratación antes de elecciones."],
 ["Licitación pública", "Modalidad general, competitiva, con adjudicación en audiencia."],
 ["Liquidación", "Cierre del contrato con balance final de obligaciones y saldos."],
 ["Matriz de riesgos", "Tabla de riesgos previsibles con su valoración, asignación y tratamiento."],
 ["Mínima cuantía", "Modalidad para valores hasta el 10 % de la menor cuantía; gana el menor precio."],
 ["Ordenador del gasto", "Servidor con competencia, por delegación, para comprometer recursos y firmar contratos."],
 ["PAA", "Plan Anual de Adquisiciones."],
 ["Perfeccionamiento", "Momento en que nace el contrato: acuerdo sobre objeto y precio por escrito."],
 ["Pliego de condiciones", "Reglas del proceso: requisitos, factores, cronograma y minuta."],
 ["RP", "Registro presupuestal: compromete los recursos con el contrato."],
 ["RUP", "Registro Único de Proponentes, en la Cámara de Comercio."],
 ["SECOP II", "Plataforma transaccional de compras públicas de Colombia Compra Eficiente."],
 ["Selección abreviada", "Modalidad para menor cuantía, bienes uniformes y otros casos legales."],
 ["SMMLV", "Salario mínimo mensual legal vigente; $ 1.750.905 en 2026."],
 ["Subsanar", "Corregir o completar requisitos que no dan puntaje, dentro del término legal."],
 ["Supervisor", "Servidor de la entidad que vigila la ejecución del contrato."],
 ["Urgencia manifiesta", "Causal de contratación directa para situaciones que exigen acción inmediata (Ley 80, arts. 42-43)."],
]

PLAZOS = [
 ["Publicar documentos en SECOP II", "3 días hábiles desde su expedición"],
 ["Proyecto de pliego — licitación", "Mínimo 10 días hábiles antes de la apertura"],
 ["Proyecto de pliego — selección abreviada y concurso", "Mínimo 5 días hábiles"],
 ["Invitación de mínima cuantía", "Mínimo 1 día hábil"],
 ["Audiencia de riesgos (licitación)", "Dentro de 3 días hábiles desde el inicio del plazo para ofertar"],
 ["Traslado del informe de evaluación — licitación", "5 días hábiles"],
 ["Liquidación bilateral", "Plazo del pliego o contrato; si no, 4 meses"],
 ["Liquidación unilateral", "2 meses siguientes"],
 ["Ley de Garantías 2027 (art. 38 parág.)", "Desde ≈ 30-jun-2027 hasta la elección"],
]
