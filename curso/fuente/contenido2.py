"""Ampliación: preguntas adicionales por módulo, taller de casos y actividad de orden.
Fuente: referencias verificadas del repositorio (contratacion-estatal, secretaria-infraestructura-fisica)."""
from contenido import Q

EXTRA = {
"m1": [
 Q("Las empresas industriales y comerciales del Estado con régimen especial…", ["No tienen ninguna regla", "Aplican derecho privado, pero deben respetar los principios de la función pública", "Siempre licitan"], 1, "Ley 1150, art. 13: los regímenes especiales aplican los principios de la función administrativa y de la gestión fiscal."),
 Q("¿Quién puede responder fiscalmente por un contrato mal ejecutado?", ["Solo el contratista", "Servidores, contratistas, supervisores e interventores que causen daño al patrimonio", "Nadie, si el contrato se liquidó"], 1, "La responsabilidad alcanza a todos los que gestionan recursos públicos."),
 Q("Contratar \"a dedo\" una obra pequeña sin proceso vulnera principalmente…", ["La selección objetiva y la transparencia", "El equilibrio económico", "La autonomía territorial"], 0, "Aun lo pequeño se contrata por la modalidad que corresponda (por ejemplo, mínima cuantía)."),
],
"m2": [
 Q("La Ley 2022 de 2020 se refiere a…", ["Documentos Tipo obligatorios", "La Ley de Garantías", "Las APP"], 0, "Hizo obligatorios los Documentos Tipo y dio competencia a Colombia Compra Eficiente."),
 Q("¿Qué norma reglamenta paso a paso cada modalidad de selección?", ["La Constitución", "El Decreto 1082 de 2015", "La Ley 996 de 2005"], 1, "El Decreto 1082 de 2015 (Parte 2, Título 1), modificado en 2026 por los Decretos 287 y 0997."),
 Q("Desde 2026, antes de firmar, además de los antecedentes nacionales se deben consultar…", ["Las redes sociales del contratista", "Las listas restrictivas internacionales, dejando constancia", "El historial crediticio"], 1, "Decreto 0997 de 2026; aparecer en una lista no inhabilita automáticamente: se analiza caso a caso."),
],
"m3": [
 Q("¿Qué plataforma usa la Gobernación para radicados y gestión documental?", ["SECOP II", "Mercurio", "SIGEP"], 1, "Mercurio es el sistema de gestión documental de la Gobernación."),
 Q("La Tienda Virtual del Estado sirve para…", ["Comprar por Acuerdo Marco de Precios", "Publicar el PAA", "Registrar proponentes"], 0, "Allí se emiten órdenes de compra de Acuerdos Marco e instrumentos de agregación de demanda."),
 Q("¿Puede el supervisor delegar su función en un contratista de apoyo?", ["Sí, por escrito", "No; puede apoyarse en él, pero la supervisión no se delega", "Sí, si el contrato es pequeño"], 1, "El apoyo a la supervisión es posible; la responsabilidad sigue en el supervisor designado."),
],
"m4": [
 Q("El análisis del sector debe ser…", ["Igual para todos los procesos", "Proporcional al valor, tipo y riesgo del proceso", "Opcional en licitaciones"], 1, "Decreto 1082, art. 2.2.1.1.1.6.1: proporcional al proceso."),
 Q("Si el plazo de un contrato pasa al año siguiente, el soporte presupuestal requiere…", ["Vigencias futuras autorizadas", "Solo un RP", "Un acta de inicio anticipada"], 0, "Sin vigencias futuras no se pueden comprometer recursos de años siguientes."),
 Q("¿Cuál NO es contenido mínimo del estudio previo?", ["La necesidad", "La modalidad y su justificación", "El nombre del contratista que se va a elegir"], 2, "El estudio previo no anticipa ganador: eso violaría la selección objetiva."),
],
"m5": [
 Q("¿Qué capacidad se mide con indicadores como liquidez y endeudamiento?", ["Jurídica", "Financiera", "De experiencia"], 1, "Son indicadores de capacidad financiera, verificados en el RUP."),
 Q("¿Se puede mejorar el precio de la oferta después del cierre?", ["Sí, como subsanación", "No; lo que da puntaje no se mejora después del cierre", "Solo en mínima cuantía"], 1, "Subsanar no permite mejorar la oferta."),
 Q("La matriz de riesgos se sustenta legalmente en…", ["Ley 1150, art. 4", "Ley 996, art. 38", "Ley 1712, art. 9"], 0, "El art. 4 de la Ley 1150 exige estimar, tipificar y asignar riesgos previsibles."),
],
"m6": [
 Q("La subasta inversa se usa para…", ["Consultoría", "Bienes y servicios de características técnicas uniformes", "Obra pública mayor"], 1, "Es una forma de selección abreviada por menor precio."),
 Q("¿Qué certificado exige un contrato de prestación de servicios profesionales?", ["De inexistencia o insuficiencia de personal de planta", "De paz y salvo de valorización", "De disponibilidad de predios"], 0, "Lo expide Talento Humano."),
 Q("Un contrato con el municipio de Fredonia para mejorar una vía terciaria se celebra por…", ["Licitación", "Contratación directa (convenio interadministrativo)", "Concurso de méritos"], 1, "Ley 1150, art. 2, num. 4, lit. c; ojo con la Ley de Garantías desde ≈ 30-jun-2027."),
],
"m7": [
 Q("¿Qué pasa si en una licitación nadie se presenta?", ["Se adjudica al que la entidad prefiera", "Se declara desierta por acto motivado", "Se prorroga indefinidamente"], 1, "La declaratoria de desierta es motivada; luego puede seguirse una selección abreviada en las condiciones de la norma."),
 Q("Una oferta con un precio sospechosamente bajo…", ["Se rechaza de plano", "Se le pide explicación antes de decidir", "Gana automáticamente"], 1, "Decreto 1082, art. 2.2.1.1.2.2.4: oferta artificialmente baja."),
 Q("¿En cuántos días hábiles se publican los documentos del proceso en SECOP II?", ["3 días hábiles desde su expedición", "30 días", "Al final del contrato"], 0, "Decreto 1082, art. 2.2.1.1.1.7.1."),
],
"m8": [
 Q("Si un sector no tiene Documento Tipo, la entidad…", ["No puede contratar", "Aplica el Decreto 1082 y las guías de CCE, con requisitos proporcionales y justificados", "Copia el de otro sector"], 1, "Sin documento tipo se justifica cada habilitante y factor en el estudio previo."),
 Q("¿Qué matriz del Documento Tipo dice si la actividad está cubierta?", ["Matriz 1 – Experiencia", "Matriz de riesgos", "Matriz de cumplimiento"], 0, "La Matriz 1 define la experiencia exigible por actividad."),
 Q("Los Documentos Tipo de infraestructura social son obligatorios desde…", ["El 16 de febrero de 2026", "2020", "No son obligatorios"], 0, "Resoluciones 539, 540, 952 y 953 de 2025."),
],
"m9": [
 Q("El amparo que cubre los daños a terceros en una obra es…", ["Responsabilidad civil extracontractual", "Seriedad de la oferta", "Calidad del servicio"], 0, "Obligatorio en obra."),
 Q("¿Quién aprueba la garantía del contratista?", ["La aseguradora", "La entidad", "El interventor"], 1, "La aprobación de la garantía es un requisito de ejecución a cargo de la entidad."),
 Q("La obligación de usar la marca institucional debe ir en…", ["Los contratos y convenios", "Solo en la publicidad", "Ningún documento"], 0, "Manual de Identidad Visual, Ley 2345 de 2023 y Ordenanza 7 de 2021."),
],
"m10": [
 Q("Un contrato suspendido requiere para continuar…", ["Acta de reinicio y ajuste de garantías", "Nada", "Un nuevo proceso"], 0, "La suspensión se cierra con acta de reinicio."),
 Q("La cesión de un contrato exige…", ["Autorización previa escrita y cesionario con iguales o mejores condiciones", "Solo aviso por correo", "Que el contrato esté vencido"], 0, "Sin autorización la cesión no es válida."),
 Q("Avance financiero 80 % y avance físico 40 %: ¿qué indica?", ["Todo va bien", "Pagos adelantados a la ejecución: alerta de supervisión", "Que hay que adicionar"], 1, "Es una señal de alerta clásica."),
],
"m11": [
 Q("La multa busca…", ["Castigar después de liquidar", "Apremiar el cumplimiento durante la ejecución", "Terminar el contrato"], 1, "La multa es conminatoria."),
 Q("La decisión del procedimiento del art. 86 se notifica…", ["Por correo a los 30 días", "En la misma audiencia, con recurso de reposición", "Solo a la aseguradora"], 1, "Se notifica en audiencia y la reposición se resuelve en ella."),
 Q("Si el contratista se pone al día durante el procedimiento…", ["Se impone la sanción igual", "La entidad puede dar por terminado el procedimiento", "Se declara la caducidad"], 1, "El art. 86 permite terminar el procedimiento si cesa el incumplimiento."),
],
"m12": [
 Q("En la liquidación se libera…", ["El saldo no ejecutado del RP", "La garantía de estabilidad", "El RUP"], 0, "El balance financiero libera recursos comprometidos y no usados."),
 Q("Al liquidar una obra, la garantía de estabilidad…", ["Se cancela", "Debe estar vigente por el plazo exigido desde el recibo", "No aplica"], 1, "Mínimo 5 años desde el recibo a satisfacción."),
 Q("Los convenios interadministrativos…", ["No se liquidan", "También se liquidan y se reintegran los saldos no ejecutados", "Se archivan sin trámite"], 1, "Ejemplo: la SIF liquidó 61 convenios con municipios en 2025."),
],
"m13": [
 Q("¿Qué es el AIU?", ["Administración, imprevistos y utilidad del presupuesto de obra", "Acta de inicio unificada", "Un tipo de garantía"], 0, "Se presenta desagregado en el presupuesto oficial."),
 Q("Un mejoramiento de vía existente generalmente…", ["Requiere licencia ambiental siempre", "No requiere licencia ambiental: usa PAGA y los permisos de recursos naturales", "No requiere nada"], 1, "Decreto 1076 de 2015 (listado del Decreto 769 de 2014)."),
 Q("Si la vía es de competencia municipal según la malla vial, el Departamento interviene normalmente mediante…", ["Contrato de obra directo sin más", "Convenio o cofinanciación con el municipio", "Una adición a cualquier contrato"], 1, "La competencia sobre la vía define el instrumento."),
],
"m14": [
 Q("Para Antioquia, la compra pública sostenible del Decreto 0997 empieza aproximadamente en…", ["Agosto de 2026", "Mayo de 2027", "2030"], 1, "9 meses desde la publicación para departamentos de categoría especial (calcular con el texto oficial)."),
 Q("El Decreto Legislativo 1420 de 2026 ¿suspende la publicación en SECOP II?", ["Sí", "No; todo se publica en los términos ordinarios", "Solo en obras"], 1, "La publicidad y el control fiscal se mantienen."),
 Q("Durante la Ley de Garantías de 2027, las licitaciones…", ["Se suspenden", "Continúan: los procesos competitivos no se suspenden", "Se convierten en directas"], 1, "La restricción del art. 38 recae sobre convenios interadministrativos y nómina."),
],
}

# Taller de casos aplicados: cada caso con su situación y 2-3 decisiones
CASOS = [
{"id": "c1", "area": "plan", "t": "La necesidad que no estaba en el PAA",
 "s": "En marzo, la Dirección de Desarrollo Físico detecta que necesita un estudio de suelos para un puente. La necesidad no está en el Plan Anual de Adquisiciones y no hay CDP.",
 "q": [
  Q("¿Qué hace primero?", ["Contrata y luego actualiza el PAA", "Actualiza el PAA y solicita el CDP antes de abrir el proceso", "Usa el CDP de otro proyecto"], 1, "La planeación exige la necesidad en el PAA y la disponibilidad presupuestal previa."),
  Q("El estudio de suelos, por su naturaleza, es…", ["Consultoría", "Suministro", "Obra"], 0, "Estudios técnicos son consultoría (Ley 80, art. 32, num. 2)."),
  Q("Si vale $ 150 millones (2026), la modalidad es…", ["Concurso de méritos", "Mínima cuantía", "Licitación"], 1, "$ 150.000.000 ≤ $ 175.090.500: mínima cuantía aplica a cualquier objeto."),
 ]},
{"id": "c2", "area": "sel", "t": "El requisito de más",
 "s": "Para una licitación de pavimentación con Documento Tipo de transporte v4, un ingeniero propone exigir 15 años de experiencia del proponente \"para asegurar calidad\".",
 "q": [
  Q("¿Se puede?", ["Sí, si se justifica", "No: el Documento Tipo es inalterable en habilitantes y factores", "Solo con autorización del Gobernador"], 1, "Ley 2022 de 2020."),
  Q("¿Dónde se verifica la experiencia exigible para pavimentación?", ["Matriz 1 – Experiencia del Documento Tipo", "En el RUT", "En la matriz de riesgos"], 0, "La Matriz 1 define la experiencia por actividad."),
 ]},
{"id": "c3", "area": "sel", "t": "El proponente que olvidó un documento",
 "s": "En una selección abreviada, un proponente no adjuntó el certificado de su revisor fiscal sobre pagos de seguridad social. El documento no da puntaje.",
 "q": [
  Q("¿Qué hace el comité evaluador?", ["Lo rechaza", "Le pide subsanar dentro del término legal", "Le resta puntos"], 1, "Lo que no da puntaje es subsanable hasta el traslado del informe de evaluación."),
  Q("Si el proponente aprovecha y envía también un menor precio…", ["Se acepta", "No se acepta: no se puede mejorar la oferta", "Se promedia"], 1, "Subsanar no es mejorar."),
 ]},
{"id": "c4", "area": "ejec", "t": "El contrato que vence mañana",
 "s": "Un contrato de interventoría vence mañana y la obra vigilada tiene una prórroga aprobada de dos meses.",
 "q": [
  Q("¿Qué debe hacer hoy el supervisor?", ["Esperar a que venza y luego prorrogar", "Tramitar hoy la prórroga de la interventoría, con garantías ampliadas", "Nada: la interventoría sigue sola"], 1, "Un contrato vencido no se puede prorrogar."),
  Q("¿Qué regla especial tiene la interventoría?", ["Puede prorrogarse por el mismo plazo del contrato vigilado, con ajuste de valor", "No se puede prorrogar", "Se prorroga sin documento"], 0, "Ley 1474, art. 85."),
 ]},
{"id": "c5", "area": "ejec", "t": "La obra que nadie pidió",
 "s": "Durante una obra vial el contratista construyó, por instrucción verbal del supervisor, 80 m de cuneta no previstos. Ahora pide el pago.",
 "q": [
  Q("¿Fue correcto?", ["Sí, si era necesario", "No: el supervisor no puede autorizar trabajos no pactados", "Sí, porque es poca obra"], 1, "Se requería acta de precios no previstos y modificación con soporte presupuestal antes de ejecutar."),
  Q("¿Qué riesgo se genera?", ["Ninguno", "Hallazgo fiscal y disciplinario, y una posible reclamación del contratista", "Solo un retraso"], 1, "Obra ejecutada sin respaldo contractual ni presupuestal."),
 ]},
{"id": "c6", "area": "ejec", "t": "El contratista que no avanza",
 "s": "Un contratista de obra lleva tres meses con 20 % de avance frente a 60 % programado. La interventoría ha requerido por escrito tres veces.",
 "q": [
  Q("¿Qué documento inicia el procedimiento sancionatorio?", ["Un correo al contratista", "El informe de la interventoría con hechos, obligaciones, pruebas y tasación", "Un trino"], 1, "Ley 1474, art. 86."),
  Q("¿A quién se cita a la audiencia?", ["Al contratista y a su aseguradora", "Solo al contratista", "A la Contraloría"], 0, "El garante también es citado."),
  Q("Si el incumplimiento paraliza la obra de manera grave, la medida más fuerte es…", ["La multa", "La caducidad", "Una adición"], 1, "La caducidad termina el contrato y genera inhabilidad."),
 ]},
{"id": "c7", "area": "cierre", "t": "La liquidación olvidada",
 "s": "Un contrato de obra terminó hace 5 meses. No se ha liquidado y el pliego no fijó plazo de liquidación.",
 "q": [
  Q("¿Qué plazo bilateral ya venció?", ["Los 4 meses de la Ley 1150", "Ninguno", "El de 10 años"], 0, "Sin plazo pactado, la bilateral es de 4 meses desde la terminación."),
  Q("¿Qué puede hacer ahora la entidad?", ["Nada", "Liquidar unilateralmente dentro de los 2 meses siguientes, o de mutuo acuerdo hasta el vencimiento del término para demandar", "Esperar 10 años"], 1, "Ley 1150, art. 11."),
 ]},
{"id": "c8", "area": "cierre", "t": "La urgencia que no era del sismo",
 "s": "Una dependencia quiere usar la urgencia manifiesta del Decreto Legislativo 1420 de 2026 para contratar la remodelación de una oficina en Medellín que no sufrió daños.",
 "q": [
  Q("¿Procede?", ["Sí, el decreto aplica a todo", "No: solo aplica a contratos directa y específicamente conexos con el sismo", "Sí, si es barata"], 1, "Exige conexidad concreta."),
  Q("¿Qué debe quedar en el expediente cuando sí procede?", ["La prueba de la conexidad: municipio, daño, reporte", "Nada", "Solo la factura"], 0, "Y el envío a la Contraloría del art. 43 de la Ley 80."),
 ]},
{"id": "c9", "area": "bases", "t": "El contratista con funciones permanentes",
 "s": "Una persona lleva cuatro años con contratos sucesivos de prestación de servicios, cumple horario y recibe órdenes como un funcionario de planta.",
 "q": [
  Q("¿Qué riesgo existe?", ["Ninguno", "Contrato realidad: subordinación y funciones permanentes", "Que se venza el RUP"], 1, "La prestación de servicios no puede usarse para funciones permanentes (C-614 de 2009, C-171 de 2012)."),
  Q("¿Qué certificado debe soportar cada contrato?", ["Inexistencia o insuficiencia de personal de planta", "Paz y salvo de valorización", "Certificado de tradición"], 0, "Lo expide Talento Humano."),
 ]},
{"id": "c10", "area": "plan", "t": "La vía sin predios",
 "s": "La Secretaría de Infraestructura quiere abrir la licitación de un mejoramiento vial. Los diseños están listos, pero faltan 12 predios por adquirir y el permiso de ocupación de cauce de un puente.",
 "q": [
  Q("¿Qué principio está en juego?", ["Maduración del proyecto (Ley 1474, art. 87)", "Publicidad", "Autonomía"], 0, "Abrir sin predios ni permisos genera suspensiones y reclamaciones."),
  Q("Si decide abrir de todas formas, ¿qué es indispensable?", ["Nada", "Tipificar y asignar el riesgo predial y ambiental en la matriz, con cronograma realista", "Pedir al contratista que compre los predios"], 1, "La adquisición predial es responsabilidad del Estado (Ley 1682, art. 20)."),
  Q("Si un propietario no acepta la oferta de compra en 30 días hábiles…", ["Se abandona el proyecto", "Es obligatorio iniciar la expropiación", "Se cambia el trazado sin estudios"], 1, "Ley 1682, art. 25, modificado por la Ley 1742 de 2014."),
 ]},
]

ORDEN_LICITACION = [
 "Aviso de convocatoria",
 "Publicación del proyecto de pliego (≥ 10 días hábiles)",
 "Acto de apertura y pliego definitivo",
 "Audiencia de asignación de riesgos y aclaraciones",
 "Cierre y apertura de ofertas",
 "Informe de evaluación y traslado (5 días hábiles)",
 "Audiencia de adjudicación",
]
