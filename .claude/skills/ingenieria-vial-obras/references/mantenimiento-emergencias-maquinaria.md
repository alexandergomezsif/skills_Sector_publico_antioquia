# Mantenimiento vial, emergencias, puntos críticos y maquinaria amarilla

Incluye lo aprendido en el apoyo a la supervisión del contrato de administración de maquinaria amarilla
de la Gobernación (Secretaría de Infraestructura Física, 2026) y en el aplicativo "Sistema de Gestión del
Contrato" (https://alexandergomezsif.github.io/GestionMaquinariaGobernacion/).

## 1. Tipos de intervención (terminología para estudios previos e informes)

| Intervención | Qué incluye | Ejemplos | Requiere diseño |
|---|---|---|---|
| **Mantenimiento rutinario** | Actividades continuas de conservación, sin cambiar la estructura | Rocería, limpieza de cunetas y alcantarillas, bacheo menor, remoción de derrumbes menores, reconformación de afirmado | No (sí plan de actividades) |
| **Mantenimiento periódico** | Actividades programadas cada varios años | Reposición de afirmado, sellos, recapeos delgados, reposición de señalización | Diseño simple / especificaciones |
| **Rehabilitación** | Recuperar la capacidad estructural original | Reconstrucción de base y carpeta, refuerzo de pavimento | Sí |
| **Mejoramiento** | Elevar especificaciones: ancho, pendiente, superficie | Pavimentación de vía en afirmado, placa huella, rectificación de curvas | Sí (geométrico, pavimentos, drenaje) |
| **Construcción** | Vía o estructura nueva | Variantes, puentes nuevos | Sí, completo, con licencias y predial |
| **Atención de emergencia** | Restablecer la transitabilidad tras un evento (derrumbe, pérdida de banca, creciente) | Remoción de derrumbes, banca provisional, pasos alternos, puente temporal | Diagnóstico; las obras definitivas requieren diseño |
| **Atención de punto crítico** | Intervención preventiva o correctiva en sitios con falla recurrente o riesgo | Conformación y compactación de calzada, obras de drenaje, manejo de aguas, estabilización | Según magnitud |

El Manual de Mantenimiento de Carreteras (INVIAS, Res. 4046 de 2018) define actividades y frecuencias
para la red nacional; úselo como referencia de alcance y unidades de medida.

## 2. Frentes activos (modelo operativo de la SIF)

La SIF despliega **frentes** de maquinaria y personal técnico en dos líneas:

1. **Emergencias viales** — restablecer el paso (derrumbes, pérdidas de banca, cierres).
2. **Atención a puntos críticos** — conformación, compactación y recuperación de tramos deteriorados.

Cada frente tiene: subregión, consecutivo (CTVO), municipio, vía (nombre + código), fecha de inicio,
fin estimado, días, equipos asignados (tipo + serie/placa + propietario), ingeniero responsable,
inspector, estado de la vía, actividad, longitud de la vía, kilómetro de atención y avance.

### 2.1 Estructura del Excel semanal "FRENTES ACTIVOS SEMANAL"

- Una hoja por semana (p. ej. `07_Septiembre`, `5_Octubre`) y una hoja `Listas` con equipos y tarifas.
- Bloques: **FRENTES EMERGENCIA** y **ATENCIÓN A PUNTOS CRÍTICOS**, cada uno con encabezado
  `SUBREGION | CTVO | MUNICIPIO | VIA (CODIGO) | FECHA INICIO | FIN ESTIMADO | DIAS | EQUIPO | SERIE | OBSERVACION`.
- Matriz de equipos por propietario a la derecha: **Equipos GOB** (propios de la Gobernación),
  **Equipos RENTAN** (contrato interadministrativo) y **Equipos ALQUILADOS**, con un `1` en la columna
  del tipo de equipo.
- La columna OBSERVACIÓN lleva pares etiqueta/valor en filas sucesivas: `Ingeniero:`, `Estado via:`,
  `Avance:`, `Actividad:`, `Longitud via (km):`, `Inspector`, `Km de atencion:`.
- **Avance** se escribe como texto: `Km atendidos 3/4_75%`, `m3 removidos_%` (plantilla sin diligenciar),
  `- 70 %`. Solo un porcentaje explícito es avance; textos de plantilla y abscisas (`8+300`) no lo son
  (regla implementada en el aplicativo, `F.parseAvanceNum`).
- **Estado vía** típico: Habilitada, Habilitada con paso restringido, Vía con declaratoria de cierre,
  Cierre total.

Al analizar estos archivos: perfilar primero (skill `analisis-datos-excel`), normalizar tipos de equipo
(`VQ SC`, `VQ Senc` y `VQ SENC` son la misma volqueta sencilla), separar frentes de emergencia y de
puntos críticos y no publicar nombres de personas.

### 2.2 Indicadores útiles para el informe semanal

| Indicador | Fórmula |
|---|---|
| Frentes activos | Conteo de frentes con fecha fin ≥ fecha de corte |
| Equipos en frente por propietario | Conteo por GOB / RENTAN / ALQUILADO |
| Días-máquina de la semana | Σ equipos × días trabajados en la semana |
| Costo estimado de alquiler | Σ días-máquina × valor día (solo equipos alquilados o con tarifa) |
| Avance físico | km atendidos / km programados (o m³ removidos / m³ estimados) |
| Variación semanal | avance actual − avance de la semana anterior (el aplicativo la calcula) |
| Equipos varados | Conteo con observación "varada"/"varado" o fuera de servicio |

## 3. Maquinaria amarilla — tipos y uso

| Código | Equipo | Uso típico en vías |
|---|---|---|
| MT | Motoniveladora (tipo 120K o similar) | Conformación de calzada y cunetas, perfilado de afirmado |
| VB 7T / VB 10T | Vibrocompactador de 7 o 10 t | Compactación de afirmado, subbase y rellenos |
| RT | Retroexcavadora sobre llanta ("pajarita") | Cargue, limpieza de cunetas y alcantarillas, excavaciones menores |
| EXC 8T / 13T / 20T / 30T | Excavadora sobre oruga (6-8 t, 130, 210, ≥ 30 t) | Remoción de derrumbes, excavación, cargue, conformación de taludes |
| BULLD | Bulldozer (D5K o similar) | Remoción de grandes volúmenes, apertura de banca |
| CARG. FR | Cargador frontal (tipo 930) | Cargue de material |
| MINIC | Minicargador (tipo Bobcat) | Trabajos menores, limpieza |
| VQ SENC | Volqueta sencilla 7 m³ | Transporte de material y escombros |
| VQ DT | Volqueta doble troque 14 m³ | Transporte de mayor volumen |
| CARROT | Carrotanque / irrigador | Humectación para compactación, control de polvo |
| COMP | Compresor con martillo | Demolición, roca |
| Cama baja | Tractocamión con remolque cama baja | Traslado de maquinaria entre frentes |

Conformación típica de un frente de puntos críticos: MT + VB + RT + 2 volquetas (conformación y
compactación). De emergencia por derrumbe: excavadora o bulldozer + volquetas, retroexcavadora de apoyo.

### 3.1 Tarifas de referencia 2026

`assets/tarifas-maquinaria-2026.json` reproduce la hoja `Listas` del Excel de frentes (oct. 2026): valor
hora y valor día (**día = 8 horas**, verificado: 289.615,06 × 8 = 2.316.920,48). Son tarifas del contrato
de alquiler vigente en esa fecha: **verifíquelas contra el contrato y sus modificaciones** antes de usarlas
en un acta o una cuenta. Para presupuestos nuevos, use el análisis del sector (skill `contratacion-estatal`).

## 4. Gestión del mantenimiento del parque de maquinaria (lecciones del contrato, 2026)

Hallazgos de la reunión técnica de agosto de 2026 con el taller del contrato, útiles como riesgos y
recomendaciones en informes de supervisión:

1. **Repuestos solo por dealer autorizado** → tiempos largos de entrega e inmovilización. Riesgo para la
   disponibilidad; evaluar en la estructuración del siguiente contrato alternativas con garantía de
   calidad (repuestos homologados, talleres certificados) **[decisión del ordenador del gasto]**.
2. **Parque antiguo** con referencias descontinuadas → planear compra anticipada y evaluar reposición.
3. **Demoras de talleres autorizados** en diagnóstico y reparación → pactar tiempos máximos e
   indicadores de disponibilidad en el contrato.
4. **Mantenimiento preventivo profundo entre contratos** → aprovechar el periodo sin operación para
   alistar los equipos antes del siguiente contrato.
5. **Bitácoras diarias incompletas** (obligación contractual) → capacitación y verificación semanal; la
   bitácora es la base de horas, fallas y trazabilidad.
6. **Equipos en mal estado estructural** → peritaje técnico antes de decidir reparación o **baja del
   activo**; el aprovechamiento de partes de un equipo dado de baja exige que la baja sea técnica,
   administrativa y jurídicamente procedente.
7. **Equipos de otras entidades** (p. ej. del DAGRAN) → definir por escrito si continúan en el contrato
   o se devuelven, para programar operación y mantenimiento.

### Indicadores de mantenimiento

| Indicador | Fórmula |
|---|---|
| Disponibilidad mecánica | horas disponibles / horas programadas × 100 |
| Utilización | horas trabajadas / horas disponibles × 100 |
| MTBF (tiempo medio entre fallas) | horas de operación / número de fallas |
| MTTR (tiempo medio de reparación) | horas de reparación / número de reparaciones |
| Cumplimiento del plan preventivo | preventivos ejecutados / programados × 100 |

## 5. Emergencias viales — secuencia técnica

1. **Reporte** (municipio, inspector, comunidad, Policía de Carreteras) con ubicación (vía, abscisa,
   coordenada) y fotos.
2. **Visita de diagnóstico**: tipo de evento (derrumbe, pérdida de banca, socavación, colapso de
   alcantarilla, falla de puente), volumen estimado, riesgo residual, afectación (cierre total/parcial).
3. **Medidas inmediatas**: señalización de emergencia, cierre o paso regulado, aviso a tránsito y
   comunidad.
4. **Asignación de frente** (equipos, ingeniero, inspector) y **orden de traslado** de maquinaria.
5. **Ejecución** con registro diario (bitácora, fotos, volúmenes, km atendidos).
6. **Habilitación** y acta o informe de cierre del frente con estado final y obras definitivas
   recomendadas (drenaje, estabilización, muros), que van a un proyecto con diseño.
7. **Soporte para la emergencia**: si se invoca urgencia manifiesta o el régimen del Decreto Legislativo
   1420 de 2026, el diagnóstico técnico es la prueba de la conexidad (skill `contratacion-estatal`).

Volúmenes: m³ en banco (medido en sitio) ≠ m³ suelto (en volqueta). Indique siempre cuál reporta; el
factor de abundamiento depende del material y se toma del estudio o de la práctica de la interventoría
**[no inventar el factor]**.
