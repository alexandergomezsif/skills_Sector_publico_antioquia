# Registro de cambios

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
