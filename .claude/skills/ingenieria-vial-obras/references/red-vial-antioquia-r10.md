# Malla vial de Antioquia — servicio ArcGIS "R10" (Circular 10)

Inspeccionado directamente en el servicio el **25-nov-2026**. Es la fuente que usa el aplicativo de
Gestión del Contrato de maquinaria (módulo de frentes y mapa) para ubicar los frentes por código de vía.

## 1. Servicio

| Atributo | Valor |
|---|---|
| URL | `https://services5.arcgis.com/K90UQIB09TmTjUL8/arcgis/rest/services/R10/FeatureServer` |
| Descripción | Red vial reportada en la Circular 10 del Departamento de Antioquia, en tres capas por clasificación |
| Sistema de referencia | **EPSG:3116** (MAGNA-SIRGAS / Colombia Bogotá zone), metros. Pida `outSR=4326` para WGS84 |
| Máximo por consulta | 2.000 registros (paginar con `resultOffset`) |
| Acceso | Público, sin token (consulta) |
| Última edición de datos | capa 2: ≈ 25-sep-2026; capa 3: ≈ 28-oct-2026 |

| Capa | Nombre | Geometría | Tramos (25-nov-2026) |
|---|---|---|---|
| 1 | Red vial primaria | Polilínea | 76 |
| 2 | Red vial secundaria | Polilínea | 169 |
| 3 | Red vial terciaria | Polilínea | 4.492 |

Los conteos cambian cuando la SIF edita el servicio: consulte con `consultar_red_vial.py conteo` antes
de citarlos. **No hay longitudes totales oficiales en este archivo**: calcúlelas con el script
(`resumen`) y cite la fecha de consulta.

## 2. Campos

| Campo | Tipo | Contenido | Observación |
|---|---|---|---|
| OBJECTID | OID | Identificador interno | No usar como código de vía |
| TIPO_VIA | entero/texto | Funcionalidad: 1 primaria, 2 secundaria, 3 terciaria | En capa 2 llega como texto `"2"` |
| SUBREGION | texto (4) | SR01…SR09 (ver dominio) | Vacío en muchos registros de capas 1 y 2 |
| MUNICIPIO | texto (5) | Código DANE (05001 Medellín … 05895 Zaragoza; 125 municipios) | Vacío en capa 2 |
| NOMBRE_VIA | texto | "Origen - Destino" | Espacios dobles y mayúsculas irregulares |
| CODIGO_VIA | texto | Código de la vía (ver §4) | Vacío (`" "`) en capa 1 (concesiones) |
| COMPETENTE | texto (2) | Entidad a cargo (dominio) | Capa 1: **texto libre** (p. ej. "ANI - …", "INVIAS - …") |
| ORDEN | entero | 1, 2, 3 | Terciaria trae `0` (sin asignar) |
| CONCESION | texto | Concesión responsable | Relevante en primaria (Autopistas 4G, Túnel del Toyo) |
| TRAMO_VIA, RUTA_VIA | texto | Tramo y ruta nacional | Mayormente vacíos |
| INICIO, FIN | texto | Puntos extremos | Pueden traer espacios iniciales |
| CENTRO_POBLADO | texto | Veredas o corregimientos servidos | Solo capa 3 |
| L_ODOMETRO | doble | Longitud medida con odómetro, **km** | |
| L_GPS | doble | Longitud medida con GPS, **km** | Capa 1: `0` en muchos tramos (relleno) |
| ANCHO_VIA | doble | Ancho de calzada, **m** | Capa 1: `1` (relleno) |
| SUPERFICIE / TIPOSUPERFICIE | texto / entero | Tipo de superficie (dominio) | Capa 3 texto `"02"`; capa 2 entero, `0` = sin dato |
| ESTADO / ESTADO_SUPERFICIE | texto / entero | Estado de la superficie (dominio) | Ídem |
| FUENTEINFO | texto (2) | Quién levantó el dato (dominio) | |
| PRODUCTO_PRINCIPAL | texto | Producto agrícola principal que moviliza | Útil para priorización |
| OBSERVACIONES | texto | Notas ("Vía nueva reportada por el Municipio") | Solo capa 3 |
| CIRCULAR | texto | "CIRCULAR 10" | Solo capa 3 |
| Shape__Length | doble | Longitud geométrica en **metros** (EPSG:3116) | Sirve para contrastar con L_GPS |

## 3. Dominios (decodificados por el script)

- **SUBREGION:** SR01 Valle de Aburrá · SR02 Bajo Cauca · SR03 Magdalena Medio · SR04 Nordeste · SR05 Norte · SR06 Occidente · SR07 Oriente · SR08 Suroeste · SR09 Urabá
- **COMPETENTE:** 01 Departamento de Antioquia · 02 Municipio · 03 ANI · 04 INVIAS · 05 Concesión
- **SUPERFICIE:** 01 Tierra · 02 Afirmado · 03 Pavimento asfáltico · 04 Tratamiento superficial · 05 Pavimento rígido · 06 Placa huella · 07 Pavimento articulado · 08 Otro · 09 Rieles · 10 Pavimento
- **ESTADO:** 01 Bueno · 02 Regular · 03 Malo · 04 Pésimo · 05 Intransitable · 98 Otro · 99 Sin información
- **FUENTEINFO:** 01 SIF · 02 Municipio · 03 PVSP · 04 INVIAS · 05 ANI · 06 Ministerio de Transporte · 07 Ortofoto - SIF
- **ORDEN:** 1 Primer orden · 2 Segundo orden · 3 Tercer orden

El servicio publica dos erratas en los nombres de dominio ("Angencia", "Tratamienot"); el script las
corrige al mostrar.

## 4. Códigos de vía

| Patrón | Ejemplo | Lectura |
|---|---|---|
| `05xxxVTnn` | `05282VT28` | Terciaria: código DANE del municipio (05282 = Fredonia) + **VT** + consecutivo |
| `rrANnn` | `25AN02` | Secundaria departamental derivada de la ruta nacional `rr` (25), consecutivo `nn` |
| `rrANnn-r` / `-r-s` | `25AN01-2-1` | Ramal y sub-ramal del tramo `25AN01` |
| `rrAN` + letra | `25ANF` | Tramo especial (variante o paso; p. ej. "Paso por Caldas") |
| vacío | — | Red primaria concesionada o nacional; buscar por nombre |

La lectura de los códigos secundarios es una **inferencia** a partir de los datos (patrón consistente en
el servicio); confírmela con el inventario oficial antes de usarla en un acto administrativo.

En el Excel semanal de frentes activos el código aparece en la columna `VIA (CODIGO)` junto al nombre
(p. ej. "Jonas\n05282VT28"); el aplicativo toma la última palabra con dígitos como código.

## 5. Calidad de datos — qué reportar siempre

1. **Competencia en la capa 1** es texto libre y a veces numérica ("3"): normalizar antes de agrupar.
2. **Longitudes de relleno** (`L_GPS = 0`, `ANCHO_VIA = 1`) en capa 1: usar `Shape__Length` / 1000 y
   decirlo.
3. **Vacíos** en SUBREGION y MUNICIPIO (capa 2): asignar por cruce espacial con límites municipales
   (IGAC/DANE) si se necesita el dato; no inventarlo.
4. **Diferencia L_GPS vs. geometría** > 10 %: señalar el tramo como "longitud por verificar en campo".
5. **Estado de superficie** es un dato de inventario, no de inspección reciente: no lo use para afirmar
   el estado actual de una vía; para eso están los boletines de la SIF y las visitas.

## 6. Consultas REST útiles (navegador o `curl`)

```
# Conteo
.../FeatureServer/3/query?where=1%3D1&returnCountOnly=true&f=json

# Vías de un municipio (atributos)
.../FeatureServer/3/query?where=MUNICIPIO%3D'05282'&outFields=*&returnGeometry=false&f=json

# Buscar por código o nombre (GeoJSON en WGS84 para un mapa)
.../FeatureServer/2/query?where=CODIGO_VIA%20LIKE%20'%2525AN02%25'&outFields=*&outSR=4326&f=geojson

# Estadística: km por subregión (si el servicio lo permite)
.../FeatureServer/3/query?where=1%3D1&groupByFieldsForStatistics=SUBREGION
   &outStatistics=[{"statisticType":"sum","onStatisticField":"L_GPS","outStatisticFieldName":"km"}]&f=json
```

En web (MapLibre/Leaflet) el aplicativo de maquinaria carga cada capa con
`/{capa}/query?where=1=1&outFields=*&f=geojson` y busca con `NOMBRE_VIA LIKE '%x%' OR CODIGO_VIA LIKE '%x%'`.
Para muchas vías, agrupe las condiciones en lotes de ≈ 15 para no exceder el largo de URL.

## 7. Uso en informes

- Cite: "Fuente: malla vial R10 — Circular 10, Gobernación de Antioquia (ArcGIS Online), consulta del
  AAAA-MM-DD."
- Para un frente: código, nombre, orden, competencia, longitud (L_GPS), superficie y estado de inventario,
  y la abscisa del punto atendido (dato de campo, no del servicio).
- Si la vía **no es departamental** (COMPETENTE = Municipio, INVIAS, ANI o concesión), advierta que la
  intervención del Departamento requiere convenio, solicitud de apoyo o declaratoria de emergencia que
  lo justifique (ver `contratacion-estatal` y `derecho-publico-colombiano`).
