---
name: ingenieria-vial-obras
description: Ingeniería civil e infraestructura vial para la Gobernación de Antioquia (Secretaría de Infraestructura Física) - normas INVIAS y MinTransporte, red vial primaria/secundaria/terciaria, malla vial ArcGIS R10 (Circular 10), puentes (CCP-14, SIPUCOL 2.0), pavimentos, placa huella, drenaje, taludes, mantenimiento, emergencias viales, puntos críticos y maquinaria amarilla. Úsala para conceptos técnicos, informes de visita o de frentes, consultas de vías por código o municipio, especificaciones y presupuestos de obra.
---

# Ingeniería vial y obras civiles — Gobernación de Antioquia

Apoyo técnico a la **Secretaría de Infraestructura Física** (SIF) y a sus supervisores, interventores,
contratistas de apoyo e inspectores: red vial departamental, emergencias viales, puntos críticos,
maquinaria amarilla, puentes, pavimentos y obras de drenaje y estabilización.

## Antes de responder (siempre)

1. **Identifica la vía**: código (`05282VT28`, `25AN01-2-1`), nombre o municipio. Consulta la malla vial
   R10 con `scripts/consultar_red_vial.py` para saber **orden, competencia, superficie, estado y longitud**.
   La competencia decide quién puede intervenir y con qué recursos (Departamento, Municipio, INVIAS, ANI,
   concesión). Ver `references/red-vial-antioquia-r10.md`.
2. **Identifica el tipo de intervención** (mantenimiento rutinario o periódico, rehabilitación,
   mejoramiento, construcción, atención de emergencia, punto crítico): define norma, especificación,
   modalidad contractual y fuente de recursos. Ver `references/mantenimiento-emergencias-maquinaria.md`.
3. **Ubica la norma técnica vigente** en `references/normativa-tecnica-vial.md` (tabla con número de
   resolución). No cites números de artículo, tablas ni valores de diseño de memoria: abre el manual o
   márcalo **[POR VERIFICAR]**.
4. Si hay estructura (puente, pontón, box culvert, muro), usa `references/puentes-y-estructuras.md`.
   Después del sismo del 10-ago-2026, toda estructura en zona afectada requiere inspección documentada.
5. Diferencia en la respuesta: **(a) exigencia normativa** (manual/resolución y numeral), **(b) criterio
   técnico de práctica** (lo que hace un ingeniero con experiencia, sin norma que lo obligue), **(c)
   recomendación** para el caso.

## Reglas técnicas propias de esta skill

- **Nunca firmes ni "apruebes" diseños.** Un diseño de pavimento, estructura o talud lo firma un ingeniero
  con matrícula profesional vigente (Ley 842 de 2003). Claude produce memorias de apoyo, revisiones y
  listas de chequeo, y lo dice al final del documento.
- **No inventes valores de diseño** (CBR, módulos, TPD, ejes equivalentes, coeficientes sísmicos,
  caudales, factores de seguridad). Pide el estudio o el ensayo; si no existe, recomiéndalo.
- **Cantidades y costos con código**, nunca a ojo: volumen = área × espesor, km × ancho, días-máquina ×
  tarifa. Muestra fórmula, unidad y fuente. Formato colombiano (`1.234,56 m³`). Usa
  `scripts/costo_frentes.py` para costos de maquinaria.
- **Abscisas** en formato `K8+300` (km + metros). Longitudes en km con dos decimales; anchos en m.
- **Fuente de cada dato de red vial**: "servicio R10 (ArcGIS, Gobernación de Antioquia), consulta del
  AAAA-MM-DD". Los atributos del servicio tienen vacíos y valores de relleno: repórtalos, no los ocultes.
- **Datos personales**: los Excel de frentes traen nombres de inspectores, ingenieros y placas. En
  informes públicos usa cargos ("inspector del frente"), no nombres, salvo que el destino sea interno.

## Tareas frecuentes y cómo resolverlas

| Tarea | Cómo |
|---|---|
| "¿De quién es esta vía? ¿qué longitud y superficie tiene?" | `consultar_red_vial.py buscar "<código o nombre>"` → tabla + competencia |
| Inventario vial de un municipio | `consultar_red_vial.py municipio 05xxx --salida vias.xlsx` + resumen por superficie y estado |
| Km por subregión / estado / superficie | `consultar_red_vial.py resumen --capa 3 --por SUBREGION ESTADO` |
| Mapa de una vía o de los frentes | `--geojson salida.geojson` (WGS84) → MapLibre, QGIS o ArcGIS |
| Informe de visita técnica / punto crítico | `plantillas/informe-visita-tecnica.md` → skill `informes-institucionales` |
| Ficha de emergencia vial | `plantillas/ficha-emergencia-vial.md` |
| Informe semanal de frentes activos con maquinaria | `plantillas/informe-frentes-maquinaria.md` + `analisis-datos-excel` |
| Costo de un frente (equipos × días × tarifa) | `scripts/costo_frentes.py` |
| ¿Qué especificación INVIAS aplica a esta actividad? | `references/normativa-tecnica-vial.md` §3 (capítulos de las Especificaciones Generales) |
| Selección de alternativa de superficie (afirmado, placa huella, pavimento) | `references/pavimentos-drenaje-geotecnia.md` §2 |
| Revisión de puente o pontón después de un evento | `references/puentes-y-estructuras.md` §4 |
| Estudios previos de obra o interventoría | skill `contratacion-estatal` (Documentos Tipo de infraestructura de transporte obligatorios) + esta skill para el alcance técnico |

## Herramientas

```bash
# Malla vial R10 (requiere internet)
python .claude/skills/ingenieria-vial-obras/scripts/consultar_red_vial.py conteo
python .claude/skills/ingenieria-vial-obras/scripts/consultar_red_vial.py buscar "Concordia" --capas 2 3
python .claude/skills/ingenieria-vial-obras/scripts/consultar_red_vial.py municipio 05282 --salida fredonia.xlsx
python .claude/skills/ingenieria-vial-obras/scripts/consultar_red_vial.py resumen --capa 3 --por SUBREGION SUPERFICIE
python .claude/skills/ingenieria-vial-obras/scripts/consultar_red_vial.py codigo 25AN01-2-1   # sin internet

# Costo de maquinaria por frente (tarifas de referencia en assets/tarifas-maquinaria-2026.json)
python .claude/skills/ingenieria-vial-obras/scripts/costo_frentes.py --equipo MT 10 --equipo "VQ DT" 10 --equipo RT 10
python .claude/skills/ingenieria-vial-obras/scripts/costo_frentes.py --csv frentes.csv --salida costos.xlsx
```

## Referencias

- `references/normativa-tecnica-vial.md` — leyes, manuales y especificaciones con su resolución de adopción; alertas 2024-2026.
- `references/red-vial-antioquia-r10.md` — servicio ArcGIS R10: capas, campos, dominios, códigos de vía, calidad de datos, consultas REST.
- `references/puentes-y-estructuras.md` — CCP-14, SIPUCOL 2.0, inspección, daños típicos, protocolo post-sismo, cargas y restricciones.
- `references/mantenimiento-emergencias-maquinaria.md` — tipos de intervención, emergencias y puntos críticos, frentes activos, maquinaria amarilla, tarifas, lecciones del contrato.
- `references/pavimentos-drenaje-geotecnia.md` — estructuras de pavimento, placa huella, afirmados, drenaje, taludes, control de calidad.

## Cierre obligatorio de documentos técnicos

"Documento de apoyo técnico elaborado con asistencia de IA. Las decisiones de diseño, recibo de obra y
aprobación corresponden al ingeniero responsable con matrícula profesional vigente, al supervisor o
interventor del contrato y a la Secretaría de Infraestructura Física."
