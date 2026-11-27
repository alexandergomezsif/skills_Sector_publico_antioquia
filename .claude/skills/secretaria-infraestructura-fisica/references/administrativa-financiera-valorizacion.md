# Gestión administrativa y financiera de la SIF y contribución de valorización

## 1. Dirección Administrativa y Financiera (art. 236 Decreto Ordenanzal 2024070003913)

| Función | En la práctica |
|---|---|
| Recursos humanos, técnicos, físicos y financieros de la SIF | Planta (incluye empleos temporales creados en 2025 para fortalecer la SIF), contratistas de apoyo, bienes |
| Gestión administrativa y documental de procesos y contratos | Expedientes en Mercurio, TRD, SECOP II |
| Informes administrativos, financieros y presupuestales a entes de control | Contraloría General de Antioquia, CGR (SGR), Procuraduría |
| Presupuesto: elaboración, programación y ejecución | Anteproyecto, CDP, RP, PAC, traslados, reservas, vigencias futuras; soportes para contratación |
| Facturación y cartera | Facturación de valorización y otros instrumentos; **cobro persuasivo**; traslado del **coactivo** a la Tesorería (Secretaría de Hacienda) |

Base presupuestal: Decreto 111 de 1996 (Estatuto Orgánico de Presupuesto) y el estatuto orgánico
departamental; ordenanza anual de presupuesto (p. ej. Ordenanza 51 del 16-dic-2024 para 2025); decretos de
modificación (ej. Decreto 2025070002484). Ver `derecho-publico-colombiano/references/presupuesto-publico.md`.

### Indicadores financieros útiles para la SIF

| Indicador | Fórmula |
|---|---|
| Ejecución presupuestal (compromisos) | RP / apropiación definitiva × 100 |
| Ejecución de obligaciones | obligaciones / compromisos × 100 |
| Ejecución de pagos | pagos / obligaciones × 100 |
| Reservas constituidas | compromisos sin obligar al 31-dic |
| Avance físico vs. financiero por contrato | % obra ejecutada (interventoría) vs. % pagado |
| Cartera de valorización | saldo por cobrar por proyecto y edad de la mora |

Use la skill `analisis-datos-excel` (`ejecucion_presupuestal.py`) para los cálculos.

## 2. Contribución de valorización — Departamento de Antioquia

### Marco

| Norma | Contenido |
|---|---|
| Decreto Legislativo 1604 de 1966 | Contribución de valorización (adoptado como legislación permanente por la Ley 48 de 1968); su art. 9 se cita en la gestión de paz y salvos **[POR VERIFICAR texto]** |
| Decreto 1222 de 1986 (Código de Régimen Departamental) | Valorización departamental |
| Ley 1682 de 2013 | Citada por la SIF como fundamento complementario (art. 12) **[POR VERIFICAR contenido aplicable]** |
| **Ordenanza 46 del 29-dic-2022** | **Estatuto de la contribución de valorización** del Departamento (art. 49: resoluciones modificadoras de la distribución; art. 70: balance) [V] |
| **Ordenanza 22 del 16-ago-2024** | Modifica y adiciona la Ordenanza 46: precisa elementos esenciales (sujeto activo: el Departamento; solidaridad), adopta **beneficio local o directo y beneficio general** como sistemas [V] |
| Ordenanza 57 de 2016 | Estatuto anterior; sigue citándose para proyectos decretados en su vigencia (cobro coactivo por mora de 3 cuotas mensuales, 1 semestral o 1 anual) [V] |
| Decreto 2023070003577 de 2023 | Cartera irrecuperable y saneamiento [V por cita] |
| Decreto 2025070004084 de 2025 | Comité Técnico de Sostenibilidad (saneamiento contable) [V por cita] |

### Etapas (según el estatuto y la práctica de la SIF)

1. **Factibilidad del proyecto por valorización** (Dirección de Instrumentos de Financiación): beneficio,
   capacidad de pago, zona de influencia, censo y socialización.
2. **Ordenanza** de la Asamblea que decreta la obra por el sistema de valorización.
3. **Resolución distribuidora** (contribución por predio) y notificación; recursos.
4. **Resoluciones modificadoras** (art. 49 Ord. 46/2022): ajustes por cambios de área, propietario o
   error.
5. **Recaudo**: contado o cuotas; **facturación y cobro persuasivo** (Dirección Administrativa y
   Financiera).
6. **Cobro coactivo** por mora: competencia de la **Tesorería General — Secretaría de Hacienda** [V].
7. **Paz y salvo** y **autorizaciones de registro** a las ORIP (Oficinas de Registro) para escrituras de
   predios gravados; inscripción del gravamen en el folio.
8. **Balance** del proyecto (art. 70) ante la Asamblea; devoluciones si hay excedentes o la obra no se
   ejecuta (ej.: Loma Hermosa, San Jerónimo, en devolución de dineros).

### Proyectos de valorización vigentes (informe de la Dirección de Instrumentos de Financiación, ene. 2026)

| Proyecto | Subregión | Estado |
|---|---|---|
| Limón – Anorí (2014) | Nordeste | En construcción, novedades de cobro |
| Puerto Nare – Puerto Triunfo (2018) | Magdalena Medio | En construcción, novedades de cobro |
| Puro Cuero – Puente Chapinero (2018) | Oriente | En construcción, novedades de cobro |
| Carabanchel – La María | Oriente | En construcción, novedades de cobro |
| Líbano – Puente Iglesias / Camino de la Virgen (Támesis) (Ord. 62 de 2017) | Suroeste | En construcción, novedades de cobro |
| Loma Hermosa (San Jerónimo) | Occidente | Devolución de dineros |

Otros datos del mismo informe: balance parcial elaborado (37 obras financiadas); 35 comunicaciones de
cobro persuasivo; 13 expedientes trasladados a Hacienda para coactivo; propuesta de **saneamiento de 30
proyectos con cartera de ≈ $3.882 millones (2.008 contribuyentes)**; estudio de **14 corredores viales**
(10 subgrupos) para nueva valorización por beneficio general; gestión manual de paz y salvos (se prepara
un software).

### Reglas de reporte de gravámenes de valorización en estudios de títulos y paz y salvos

(Criterios del aplicativo Automatización VUR, definidos por el usuario para la Dirección Administrativa y
Financiera.)

- Registrar **toda** anotación de valorización, pagada o no: quién gravó, si se canceló y quiénes
  intervinieron. Conclusión: **"VALORIZADA Y CANCELADA"** o **"VALORIZADA"**.
- La valorización **municipal** no corresponde a la Gobernación, pero se anota.
- La valorización **INVIAS** sí compete a la Gobernación (otro tipo de paz y salvo).
- Folio **no activo** → no se genera paz y salvo.
- Las afectaciones de inenajenabilidad por valorización no definen por sí solas el paz y salvo: el
  profesional decide.
- Identificar el **propietario actual** (puede no coincidir con el gravado).

## Fuentes

- Página de la Dirección Administrativa y Financiera (antioquia.gov.co/articulos/direccion-administrativa-y-financiera)
- Gaceta Departamental 23.853 (Ordenanza 46 de 2022) y 24.630 (Ordenanza 22 de 2024)
- Informes de gestión de la Dirección de Instrumentos de Financiación (2025 y 2026)
- Avisos de notificación de valorización publicados por la SIF (2025-2026)
