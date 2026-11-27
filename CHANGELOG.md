# Registro de cambios

## [1.8.0] — 2026-11-27

Curso de contratación estatal: menú del aula ampliado solo con lo que se usa.
- **Programa del curso**: propósito, público, contenido por etapa con tiempos, cómo se avanza, cómo se califica y
  preguntas frecuentes (ingreso desde otro equipo, correo que no llega, repetir la evaluación, a quién preguntar).
- **Material por módulo**: memoria en PDF de cada módulo (`curso/memorias/modulo-NN.pdf`), normas con enlace al
  Gestor Normativo de Función Pública (enlaces verificados el 27-nov-2026) y guías de Colombia Compra Eficiente;
  acceso directo desde cada lección.
- Se descartaron foro, participantes, calendario, anuncios e insignias por no aportar a un curso individual a ritmo propio.

## [1.7.0] — 2026-11-27

Curso de contratación estatal: **inscripción con aprobación de la coordinación** (versión piloto, en pruebas).
- La persona se inscribe con cédula y correo; la coordinación recibe un correo con botones Aprobar y Rechazar
  (enlaces firmados con HMAC y página de confirmación).
- Al aprobar, la persona recibe la bienvenida con un enlace personal de entrada; se elimina el código de 6 dígitos.
- Pestaña Inscritos con estados pendiente, aprobado y rechazado; panel de coordinación con aprobados y pendientes.
- Funciones internas del script marcadas como privadas (`_`) para que no se puedan invocar desde fuera.

## [1.6.0] — 2026-11-27

Curso de contratación estatal 3.0: **aula virtual**.
- Cada módulo en su propia página (`#/modulo/mX`), con menú lateral de contenido, candados, avance y migas de pan;
  en celular el menú se abre como panel lateral.
- Secuencia obligatoria: un módulo se aprueba al leer la lección hasta el final y obtener al menos 70 % en su
  evaluación; si no lo alcanza presenta un refuerzo (habilita el avance, no cambia la nota del primer intento).
  El taller se habilita con los 15 módulos aprobados y la evaluación final con el taller completo.
- Portada con "continuar donde quedó", ruta del contrato y tarjetas de módulo con su estado; notas por módulo en
  "Mi calificación"; aviso antes de abandonar una evaluación final en curso.
- Registro en Google Sheets conectado (`curso/endpoint.txt`); clave de coordinación generada por el script.

## [1.5.0] — 2026-11-26

Curso de contratación estatal, versión 2.1, tras contrastarlo con el material de un diplomado externo
(usado solo como lista de temas; redacción propia y normas verificadas en fuentes oficiales).
- Nuevo módulo **"Quién no puede contratar: inhabilidades, nulidad y responsabilidades"**: Ley 80 arts. 8-10,
  44-48, 50-58; Ley 1474 arts. 3, 4 y 90 (texto vigente tras la Ley 1955 de 2019 y la Ley 2195 de 2022);
  conflicto de interés (CPACA art. 11); responsabilidad fiscal, disciplinaria (Ley 1952 de 2019), penal y civil.
- Módulos ampliados: control ciudadano y veedurías (marco normativo); consorcios, uniones temporales,
  competencia para contratar y regímenes especiales (actores); clases, suficiencia, vigencia y efectividad de
  las garantías según el Decreto 1082 de 2015 (garantías); poderes excepcionales, art. 14 a 19 de la Ley 80
  (supervisión y modificaciones).
- Taller: 4 casos nuevos (exservidor, unión temporal, cálculo de pólizas, contrato nulo) y **cuadro
  comparativo de modalidades** interactivo; 17 preguntas nuevas en los módulos (103 en total).
- Claves de respuesta estables por identificador de módulo (`m15-q0`); textos con el número de módulos
  calculado; memorias en PDF actualizadas (52 páginas) con el cuadro comparativo como anexo.

## [1.4.0] — 2026-11-26

- Nuevo **curso de contratación estatal** en `curso/`: 14 módulos, 86 preguntas, taller de 10 casos,
  evaluación final de 40 preguntas con opciones barajadas, ingreso por cédula sin contraseña,
  autorización de datos (Ley 1581), índice de apropiación (20 % práctica + 30 % casos + 50 % final),
  niveles con requisitos por etapa, constancia con código de verificación y panel del coordinador.
- Registro en Google Sheets con Apps Script (`curso/apps-script/Codigo.gs`): bloqueo concurrente,
  saneamiento contra inyección de fórmulas, resumen por persona con el mejor resultado, clave de coordinador.
- Memorias del curso en PDF (40 páginas) generadas desde la misma fuente (`curso/memorias.py`).

## [1.3.0] — 2026-11-25

- Nueva skill **`secretaria-infraestructura-fisica`**: estructura y funciones oficiales de la SIF
  (Decreto Ordenanzal 2024070003913, páginas de cada dirección), equivalencias con la estructura de 2020,
  flujo entre dependencias; estructuración de proyectos (MGA, BPIN, SGR, maduración, fuentes, Plan Vial,
  APP); gestión predial (Leyes 9/1989, 388/1997, 1682/2013, 1742/2014, 1882/2018; Res. IGAC 620/2008,
  898/2014, 1044/2014, 316/2015); gestión social y ambiental (Decreto 1076: licencia vs. PAGA, permisos,
  consulta previa); asuntos legales; administrativa y financiera y **valorización** (Ordenanzas 46/2022 y
  22/2024, proyectos vigentes, cobro, paz y salvo); programas y metas 2024-2027; dirección y coordinación.
  Plantillas: lista de maduración y ficha predial.
- `contratacion-estatal`: nueva referencia `contratacion-obra-infraestructura.md` (Documentos Tipo de
  transporte vigentes, interventoría, anticipo y fiducia, garantías, actas de obra, APU/AIU, alertas) y
  script **`consultar_secop.py`** (SECOP II datos abiertos).
- `ingenieria-vial-obras`: el lector de códigos reconoce rutas con letra (`25BAN06`).
- CLAUDE.md (alerta 7 y ruta por dependencia), README, glosario, fuentes, mantenimiento y ejemplos.

## [1.2.0] — 2026-11-25

- Nueva skill **`ingenieria-vial-obras`** (Secretaría de Infraestructura Física):
  - Normativa técnica verificada a nov. 2026: Ley 1228 (fajas de retiro), Ley 1682, Especificaciones
    Generales INVIAS 2022 (Res. 4561 y 2451 de 2022), manuales de diseño geométrico, drenaje, cimentaciones,
    mantenimiento y pavimentos, Guía de placa huella (Res. 4401 de 2017), CCP-14 (Res. 108 de 2015),
    SIPUCOL 2.0 (Res. 20263040023605 de 2026), Manual de Señalización 2024, contención vehicular 2022-2024,
    Plan de cambio climático del sector transporte 2026.
  - Malla vial **R10** (ArcGIS, Circular 10): capas, campos, dominios, códigos de vía, calidad de datos y
    consultas REST; script `consultar_red_vial.py` (buscar, municipio, resumen, conteo, GeoJSON).
  - Puentes: inspección, daños, protocolo post-sismo, paso de maquinaria pesada.
  - Mantenimiento, emergencias viales, puntos críticos, estructura del Excel de frentes activos,
    maquinaria amarilla, tarifas de referencia 2026 y lecciones del contrato de maquinaria.
  - Pavimentos, placa huella, drenaje, taludes, control de calidad.
  - Plantillas: informe de visita técnica, ficha de emergencia vial, informe semanal de frentes.
  - Script `costo_frentes.py` (equipos × días × tarifa, Excel con fórmulas).
- `CLAUDE.md`, glosario, fuentes oficiales, mantenimiento y ejemplos actualizados.

## [1.1.0] — 2026-11-11

- Escudo oficial en resolución de pantalla (157 × 70 px) incluido y usado por los generadores de Word y
  PowerPoint como respaldo.
- `marca-gobernacion`: sección de aplicativos y herramientas internas con las convenciones del aplicativo
  de consulta de valorización en VUR (Secretaría de Infraestructura).

## [1.0.0] — 2026-11-11

Versión inicial.

- `CLAUDE.md` con reglas de trabajo, datos institucionales y alertas normativas vigentes a nov. 2026.
- Contexto: estructura (Decreto Ordenanzal 2024070003913), Plan de Desarrollo (Ordenanza 11 de 2024),
  valores 2026, fuentes oficiales, glosario, mantenimiento.
- Skills: marca-gobernacion, informes-institucionales, presentaciones-institucionales,
  contratacion-estatal, derecho-publico-colombiano, analisis-datos-excel.
- Normativa 2026 incorporada: Decreto 0997 (compra pública sostenible, RUP, anticorrupción), Decreto 287,
  Decretos 1171, 1261, 1348 y Decreto Legislativo 1420 (emergencia por el sismo del 10-ago-2026),
  Documentos Tipo 2026, Ley de Garantías para elecciones territoriales de 2027.
- Scripts: crear_informe.py, crear_presentacion.py, calcular_cuantias.py, dias_habiles.py,
  perfilar_excel.py, ejecucion_presupuestal.py, tabla_resumen.py, empaquetar_skills.py.
