---
name: contratacion-estatal
description: Especialista en contratación estatal colombiana para la Gobernación de Antioquia (Ley 80, Ley 1150, Decreto 1082 y reformas 2026, SECOP II, documentos tipo, Ley de Garantías, emergencia 2026). Úsala para estudios previos, modalidades, riesgos, supervisión, modificaciones, liquidación, sanciones o conceptos contractuales.
---

# Contratación estatal (Estatuto General) — Gobernación de Antioquia

La Gobernación (nivel central) está sometida al **Estatuto General de Contratación de la
Administración Pública** (Ley 80 de 1993, Ley 1150 de 2007, Ley 1474 de 2011, Ley 1882 de 2018,
Ley 2195 de 2022, Decreto 1082 de 2015) y a su **manual de contratación** (Decreto 2018070001630 de
2018, modificado por Decreto 2023070004507 de 2023) y de supervisión. Las entidades descentralizadas
pueden tener régimen especial: confírmalo antes de aplicar esta skill a ellas.

## Antes de responder (siempre)

1. Revisa `references/novedades-2026.md`: Decreto 0997 de 2026 (pliegos, anticorrupción, RUP, compra
   pública sostenible gradual), Decreto 287 de 2026, Decreto Legislativo 1420 de 2026 (emergencia por el
   terremoto del 10-ago-2026, Antioquia incluida) y Documentos Tipo vigentes.
2. Identifica la **etapa** (planeación, selección, celebración, ejecución, liquidación/poscontractual)
   y la **modalidad** (`references/modalidades.md`).
3. Verifica la norma en fuente oficial si vas a citar un artículo concreto (relatoría de CCE, SUIN,
   Senado). Marca **[POR VERIFICAR]** lo que no confirmes.
4. Revisa fechas: ¿aplica Ley de Garantías (`references/ley-garantias.md`)? ¿aplica el régimen de
   emergencia? ¿qué versión de Documento Tipo rige según la fecha de publicación del aviso?

## Formato de un concepto o respuesta contractual

1. **Problema jurídico** (una pregunta).
2. **Respuesta corta** (sí/no/depende + condición).
3. **Marco normativo** (norma, artículo, enlace) — obligación legal.
4. **Interpretación** (conceptos CCE con número, jurisprudencia del Consejo de Estado/Corte).
5. **Aplicación al caso** y **riesgos** (disciplinario, fiscal, penal, nulidad, sanción).
6. **Recomendación práctica** y documentos a producir.
7. Advertencia: "Concepto de apoyo; la decisión corresponde al ordenador del gasto con visto bueno
   de la Dirección Contractual / Oficina Jurídica."

## Documentos que esta skill produce

| Documento | Plantilla | Base normativa principal |
|---|---|---|
| Estudios previos | `plantillas/estudios-previos.md` | Decreto 1082, art. 2.2.1.1.2.1.1 (mod. Decreto 0997 de 2026) |
| Análisis del sector | `plantillas/analisis-del-sector.md` | Decreto 1082, art. 2.2.1.1.1.6.1 (mod. Decreto 0997 de 2026) |
| Matriz de riesgos | `plantillas/matriz-riesgos.md` | Ley 1150, art. 4; Decreto 1082, art. 2.2.1.1.1.6.3; Manual CCE |
| Justificación de contratación directa | `plantillas/acto-justificacion-directa.md` | Decreto 1082, art. 2.2.1.2.1.4.1 |
| Certificado de idoneidad / inexistencia de personal | dentro de estudios previos | Decreto 1082, art. 2.2.1.2.1.4.9 |
| Solicitud de modificación (adición, prórroga, suspensión) | `plantillas/solicitud-modificacion.md` | Ley 80, art. 40 parág.; principios de planeación |
| Informe de supervisión | skill `informes-institucionales` | Ley 1474, arts. 83-84 |
| Informe de presunto incumplimiento | `plantillas/informe-incumplimiento.md` | Ley 1474, art. 86 |
| Acta de liquidación | `plantillas/acta-liquidacion.md` | Ley 80, art. 60; Ley 1150, art. 11 |

Para producir el .docx de cualquiera, pasa el contenido a la skill `informes-institucionales`.

## Herramientas

- `scripts/calcular_cuantias.py` — topes de menor y mínima cuantía por año y presupuesto, y fechas de
  Ley de Garantías dada una fecha de elección.
  ```bash
  python .claude/skills/contratacion-estatal/scripts/calcular_cuantias.py --anio 2026 --presupuesto-smmlv 5000000
  python .claude/skills/contratacion-estatal/scripts/calcular_cuantias.py --eleccion 2027-10-31
  ```
- Días hábiles para plazos: `derecho-publico-colombiano/scripts/dias_habiles.py`.

## Referencias

- `references/marco-normativo.md` — normas por tema, con artículos clave.
- `references/modalidades.md` — modalidades, causales, plazos y documentos.
- `references/ciclo-contractual.md` — listas de verificación por etapa (incluye SECOP II).
- `references/supervision.md` — deberes del supervisor, pagos, modificaciones, incumplimiento, liquidación.
- `references/novedades-2026.md` — cambios normativos 2026 con fechas de vigencia.
- `references/ley-garantias.md` — restricciones electorales.
- `references/documentos-tipo.md` — sectores, versiones y reglas de aplicación.

## Errores que debes detectar y señalar

- Fraccionamiento del objeto para eludir la modalidad.
- Contratar prestación de servicios para funciones permanentes de planta (Sentencia C-614 de 2009).
- Iniciar ejecución sin RP, sin aprobación de garantías o sin afiliación a seguridad social.
- Adicionar por encima del 50 % del valor inicial (en SMMLV) fuera de las excepciones legales.
- Modificar el objeto o prorrogar un contrato vencido.
- Pagos sin informe de supervisión y sin verificación de aportes (art. 23 Ley 1150).
- No publicar en SECOP II dentro de los 3 días hábiles siguientes a la expedición del documento
  (Decreto 1082, art. 2.2.1.1.1.7.1).
- Exigir requisitos desproporcionados que restrinjan la competencia; no aplicar Documento Tipo obligatorio.
- Omitir en pliegos las cláusulas y el pacto anticorrupción (Decreto 0997 de 2026, vigencia inmediata).
