---
name: presentaciones-institucionales
description: Crea presentaciones de la Gobernación de Antioquia (comités, Asamblea, rendición de cuentas, socializaciones, consejos de gobierno) con guion de mensajes y .pptx 16:9 con la marca. Úsala para cualquier presentación o diapositivas.
---

# Presentaciones institucionales

## Flujo

1. **Propósito y audiencia.** ¿Qué decisión o comprensión debe salir de la reunión? ¿Quién asiste
   (Gobernador, Asamblea, comunidad, comité técnico)? ¿Cuánto tiempo? Regla: 1 diapositiva ≈ 1-2 minutos.
2. **Guion antes que diseño.** Escribe la lista de diapositivas con un **título-mensaje** cada una (una
   frase completa con la conclusión: "La ejecución llegó al 72 % y va 6 puntos por debajo"). Leídos en
   secuencia, los títulos deben contar la historia completa. Muestra el guion al usuario si la
   presentación es larga o de alto impacto.
3. **Datos.** Toda cifra con fuente y fecha de corte en la diapositiva. Cálculos con la skill
   `analisis-datos-excel`.
4. **Generar.** Escribe el guion en JSON (esquema en el encabezado del script; ejemplo en
   `ejemplos/presentacion-ejemplo.json`) y ejecuta:
   ```bash
   python .claude/skills/presentaciones-institucionales/scripts/crear_presentacion.py guion.json salida.pptx
   ```
   Tipos: `seccion`, `contenido`, `kpis`, `tabla`, `grafico` (columnas, barras, lineas,
   columnas_apiladas — gráficos nativos editables), `dos_columnas`, `cierre`. Todos aceptan `notas`.
5. **Revisar.** Convierte a PDF/imagen y mira cada diapositiva: texto que se sale, tablas de más de
   8 filas (dividir), gráficos ilegibles, escudo presente.

Si la Dirección de Comunicaciones entregó la plantilla oficial .pptx, úsala como base en lugar del
script (copia y llena sus diseños) y conserva estas reglas de contenido.

## Reglas

- Máximo 6 viñetas por diapositiva y 12 palabras por viñeta. Nada de párrafos.
- Un gráfico = un mensaje. Elige: comparación entre categorías → barras/columnas; evolución en el tiempo
  → líneas; composición → columnas apiladas (evitar tortas con más de 3 partes).
- Colores de series en el orden de la marca (verde, azul, naranja, morado, dorado, azul claro).
- Escudo oficial en la esquina inferior derecha; en fondos de color, sobre contenedor blanco.
- Sin eslóganes ni marcas de gobierno, sin fotos del gobernador o funcionarios con fines de promoción
  (Ley 2345 de 2023). En periodo de Ley de Garantías extremar la neutralidad.
- Rendición de cuentas: estructura de MIPG/Manual Único de Rendición de Cuentas — qué se prometió
  (meta del plan), qué se hizo (avance con evidencia), cuánto costó, qué falta, diálogo con la ciudadanía.
- Accesibilidad: contraste AA, tamaño mínimo 14 pt en cuerpo, texto alternativo en imágenes.

## Estructuras sugeridas

| Ocasión | Secuencia |
|---|---|
| Comité directivo / seguimiento | Mensaje clave → KPIs → avance vs. meta → rezagos y causas → acciones → decisiones requeridas |
| Debate de control en la Asamblea | Cuestionario recibido → respuesta por pregunta (dato + soporte) → compromisos |
| Socialización comunitaria | Qué es el proyecto → dónde y cuándo → beneficios → cómo participar → contacto/PQRSD |
| Rendición de cuentas | Contexto → metas del plan → resultados por línea → presupuesto → retos → preguntas |
| Presentación de un proyecto (MGA) | Problema → objetivos → alternativas → costos → indicadores → cronograma → riesgos |
