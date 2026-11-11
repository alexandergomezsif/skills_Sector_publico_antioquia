---
name: informes-institucionales
description: Redacta informes de la Gobernación de Antioquia (gestión, supervisión, ejecutivo, empalme, organismos de control, oficios) en lenguaje claro y genera el .docx con membrete. Úsala para cualquier informe o documento escrito de cualquier secretaría.
---

# Informes institucionales

## Flujo

1. **Encargo.** Confirma solo lo que falte: tipo de informe, destinatario, dependencia que firma,
   periodo y fecha de corte, insumos (Excel, actas, SECOP, plan de acción). No pidas lo que ya está en
   los archivos.
2. **Estructura.** Toma la del tipo en `references/tipos-de-informe.md`. Si el destinatario tiene formato
   propio (Contraloría, Procuraduría, Asamblea, DNP), ese formato manda.
3. **Datos.** Toda cifra sale de un insumo verificable. Si hay tablas, usa la skill `analisis-datos-excel`
   y cita archivo, hoja y fecha de corte. Sin insumo: `[COMPLETAR: dato y fuente]`. Nunca inventes.
4. **Redacción.** Aplica `references/lenguaje-claro.md`: conclusión primero, frases ≤ 25 palabras, voz
   activa, sin adjetivos de autoelogio ("exitoso", "histórico"), sin marcas ni eslóganes de gobierno.
5. **Vínculo con el plan.** En informes de gestión, cada logro se ata a línea → componente → programa →
   indicador → meta → avance (Ordenanza 11 de 2024).
6. **Generación del archivo.** Escribe el contenido en JSON y ejecuta:
   ```bash
   python .claude/skills/informes-institucionales/scripts/crear_informe.py contenido.json salida.docx
   ```
   El esquema JSON está documentado al inicio del script y hay un ejemplo en `ejemplos/informe-ejemplo.json`.
   El script aplica Arial 12, márgenes carta, escudo oficial (si existe en `marca-gobernacion/assets/escudo/`),
   encabezado con dependencia, pie con paginación, tablas con estilo de marca y bloque de firmas.
7. **Revisión.** Convierte a PDF y revisa visualmente si el entorno lo permite
   (`soffice --headless --convert-to pdf salida.docx`). Verifica: cifras = fuente, totales cuadran,
   fechas coherentes, sin `[COMPLETAR]` olvidados si el usuario dio los datos.

Si el usuario prefiere otro formato (Google Docs, documento en línea), entrega el mismo contenido allí.

## Reglas de contenido

- Título que diga el hallazgo, no el tema: "La ejecución presupuestal llegó al 78 % a septiembre",
  no "Ejecución presupuestal".
- Resumen ejecutivo de máximo media página al inicio en todo informe de más de 3 páginas.
- Distingue **logro** (resultado medido), **actividad** (lo que se hizo) y **pendiente** (con responsable y fecha).
- Riesgos y alertas con nivel (alto/medio/bajo), causa, efecto y acción propuesta.
- Fechas en formato "15 de octubre de 2026"; montos "$ 1.234.567.890" o "$1.234,6 millones" en tablas
  resumen (indica la unidad en el encabezado de la columna).
- Datos personales: no incluir cédulas, teléfonos ni datos sensibles en informes publicables.
- Cierre de documentos con contenido jurídico o contractual: "Borrador elaborado con apoyo de IA; requiere
  revisión y firma del servidor competente."

## Referencias

- `references/tipos-de-informe.md` — estructuras: gestión, supervisión, ejecutivo, empalme/entrega del
  cargo (Ley 951 de 2005), control interno, respuesta a organismos de control, oficio, acta.
- `references/lenguaje-claro.md` — reglas y lista de reemplazos.
