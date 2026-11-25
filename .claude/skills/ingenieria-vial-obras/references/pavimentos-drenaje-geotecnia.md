# Pavimentos, superficies de rodadura, drenaje y geotecnia

Criterios técnicos generales para orientar conceptos, revisiones y alcances. Los valores numéricos de
diseño (espesores, módulos, coeficientes, caudales) salen del manual aplicable y de los ensayos del
proyecto, nunca de este archivo.

## 1. Estructura de un pavimento (de abajo hacia arriba)

| Capa | Función | Control típico |
|---|---|---|
| Subrasante (terreno natural o mejorado) | Soporte | CBR, clasificación, humedad; mejoramiento si es deficiente |
| Subbase granular | Distribuir cargas, drenar, evitar contaminación | Granulometría, desgaste, compactación (densidad en campo) |
| Base granular o estabilizada | Capa estructural principal en flexibles | Ídem + CBR del material |
| Capa de rodadura | Superficie: mezcla asfáltica, tratamiento superficial, losa de concreto, adoquín, placa huella | Espesor, densidad, resistencia, lisura |

**Flexible**: capas granulares + asfalto (diseño por ejes equivalentes y módulo de subrasante).
**Rígido**: losas de concreto (diseño por fatiga y erosión; juntas y pasadores).
**Articulado**: adoquines sobre cama de arena y base.

## 2. Selección de superficie en vías terciarias y secundarias

| Alternativa | Cuándo conviene | Riesgos | Norma |
|---|---|---|---|
| Afirmado (material granular) | Tránsito bajo, pendientes moderadas, recursos limitados | Pérdida de material con lluvia, mantenimiento frecuente; requiere bombeo y cunetas | Esp. Generales cap. 300 |
| **Placa huella** | Pendientes fuertes donde el afirmado se pierde, tránsito bajo, zonas rurales | Mala ejecución de riostras y juntas, drenaje deficiente, cuneta insuficiente | Guía MinTransporte Res. 4401 de 2017 |
| Tratamiento superficial (simple/doble) | Tránsito bajo-medio, buena base, clima que permita riego | Desprendimiento si la base es mala | Esp. cap. 400 |
| Pavimento asfáltico | Tránsito medio-alto, corredores secundarios | Costo; requiere base buena y drenaje | Manuales de pavimentos asfálticos (1999 y 2007) |
| Pavimento rígido | Tránsito pesado, zonas con humedad alta, pendientes | Costo inicial; juntas | Manual de pavimentos de concreto |

Criterio de decisión práctico: **pendiente + tránsito + disponibilidad de materiales + capacidad de
mantenimiento del responsable** (municipio vs. Departamento). La competencia de la vía (R10) define
quién la mantendrá después.

### Placa huella — puntos de control (Guía de 2017)

Dos franjas (huellas) de concreto para las ruedas, zona central en concreto ciclópeo o piedra pegada,
riostras transversales, cunetas laterales y bordillos. Revise en obra: subrasante compactada y drenada,
dimensiones de huellas y riostras según diseño, acero de refuerzo, juntas, curado del concreto,
resistencia (cilindros), pendiente transversal, cunetas y descoles terminados antes de abrir al tránsito.

## 3. Drenaje vial (Manual de Drenaje para Carreteras, Res. 024 de 2011)

| Obra | Función | Falla típica |
|---|---|---|
| Bombeo / pendiente transversal | Sacar el agua de la calzada | Calzada plana o con baches → encharcamiento |
| Cunetas (en V, trapezoidales, revestidas) | Llevar el agua longitudinalmente | Colmatación, erosión del fondo, sección insuficiente |
| Alcantarillas (tubo o cajón) | Cruce de aguas bajo la vía | Obstrucción, socavación a la salida, diámetro insuficiente |
| Encoles y descoles | Entrada y salida de alcantarillas | Descole sin protección → erosión que avanza hacia la banca |
| Zanjas de coronación | Interceptar agua arriba del talud | Ausencia o falta de mantenimiento → deslizamientos |
| Subdrenes / filtros | Abatir el nivel freático | Colmatación del geotextil o del material filtrante |
| Bateas / vados | Cruce a nivel de quebradas pequeñas | Socavación, arrastre en crecientes |

Regla de campo: **la mayoría de las pérdidas de banca y fallas de afirmado en Antioquia tienen origen en
agua mal manejada**. Todo informe de punto crítico debe describir el drenaje existente y su estado.

## 4. Taludes y estabilización

Tipos de falla: caída de rocas, deslizamiento traslacional o rotacional, flujo de lodos o detritos,
reptación, socavación de pata por quebrada, pérdida de banca por erosión del lleno.

Medidas (de menor a mayor complejidad): manejo de aguas superficiales (zanjas, cunetas, descoles) ·
perfilado y descapote del talud · revegetalización y bioingeniería · trinchos · gaviones · muros de
concreto o tierra armada · pantallas ancladas y pilotes · drenes horizontales. El Manual de Estabilidad
de Taludes del INVIAS está en adopción **[POR VERIFICAR]**; mientras tanto, el diseño lo soporta el
estudio geotécnico del proyecto.

Toda obra de contención o estabilización requiere **estudio geotécnico y diseño firmado**. En emergencia
se permiten medidas provisionales (remoción, perfilado, drenaje, gaviones de emergencia) que deben
quedar documentadas como provisionales.

## 5. Control de calidad en obra (qué pedir al contratista o a la interventoría)

| Actividad | Evidencia mínima |
|---|---|
| Rellenos, subbase, base, afirmado | Granulometría, límites, desgaste, CBR del material; densidad en campo por capa (frecuencia de la especificación) |
| Concretos (placa huella, obras de arte, losas) | Diseño de mezcla, asentamiento, cilindros a 7 y 28 días, curado |
| Acero de refuerzo | Certificado del fabricante, verificación de diámetros, traslapos y recubrimientos |
| Mezclas asfálticas | Diseño, temperatura de colocación, densidad, espesor (núcleos), contenido de asfalto |
| Obras de drenaje | Cotas, pendiente, dimensiones, protección de descoles |
| Señalización | Conformidad con el Manual de Señalización 2024, retrorreflectividad |
| Todas | Bitácora de obra, registro fotográfico georreferenciado, cantidades medidas y firmadas |

## 6. Cálculos frecuentes (con código, mostrando fórmula y unidades)

- **Volumen de material de afirmado**: V (m³ compactos) = longitud (m) × ancho (m) × espesor (m).
  Convertir a m³ sueltos para transporte solo con un factor del estudio o del laboratorio.
- **Viajes de volqueta**: viajes = V suelto / capacidad útil de la volqueta (7 m³ sencilla, 14 m³
  doble troque según la hoja de tarifas).
- **Concreto de placa huella**: por metro lineal = (área de huellas + riostras + bordillos) × espesor del
  diseño. No usar espesores "típicos": tomar los del diseño aprobado.
- **Rendimientos de maquinaria**: dependen de equipo, material, distancia y operador; tomarlos de la
  bitácora del contrato (horas y cantidades reales), no de valores genéricos.
