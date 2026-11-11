---
name: analisis-datos-excel
description: Analiza tablas Excel/CSV con cifras de la Gobernación de Antioquia (ejecución presupuestal, contratos SECOP, metas del plan, inventarios, indicadores) con código reproducible, formato numérico colombiano y control de calidad. Úsala siempre que haya que leer, limpiar, sumar, comparar o graficar datos de una hoja de cálculo.
---

# Análisis de datos en Excel

## Regla de oro

**Ningún número se calcula "a ojo".** Toda cifra sale de código ejecutado sobre el archivo, y cada
resultado lleva: archivo, hoja, fecha de corte, filtros aplicados y unidad.

## Flujo

1. **Perfilar** antes de analizar:
   ```bash
   python .claude/skills/analisis-datos-excel/scripts/perfilar_excel.py archivo.xlsx
   ```
   Revisa: fila de encabezado real (los reportes de SAP, Mercurio o SECOP traen títulos arriba), hojas
   ocultas, celdas combinadas, filas de total/subtotal, números guardados como texto, unidades
   (pesos, miles, millones), duplicados, columnas casi vacías, errores #REF!/#N/A.
2. **Confirmar el sentido** con el usuario solo si hay ambigüedad que cambie el resultado (p. ej. si
   "Valor" incluye adiciones, si la base trae vigencias anteriores, qué fecha de corte usar).
3. **Limpiar** con pandas (`scripts/utils_co.py`: `leer_tabla`, `a_numero`, `normalizar_nombre`).
   Documenta cada transformación (filas excluidas y por qué).
4. **Calcular**:
   - Ejecución presupuestal: `scripts/ejecucion_presupuestal.py archivo.xlsx --agrupar "Dependencia"`
     (Excel con fórmulas vivas + tabla Markdown).
   - Resúmenes tipo tabla dinámica: `scripts/tabla_resumen.py archivo.xlsx --agrupar "Modalidad" --sumar "Valor" --moneda`.
   - Otros análisis: pandas ad hoc, guardando el script en el directorio de trabajo para que sea reproducible.
5. **Validar**: los totales del análisis cuadran con el total del archivo fuente (si existe) o con el
   reporte oficial; los porcentajes están entre 0 y 100 % salvo explicación; los conteos coinciden.
6. **Comunicar**: hallazgo principal en una frase, tabla corta, gráfico si ayuda (colores de la marca:
   `#018D38`, `#3561AB`, `#F28E18`, `#8B4A97`, `#B0942B`), limitaciones de los datos. Para informes o
   presentaciones, pasar los resultados a las skills correspondientes.

## Cuando el entregable es un Excel

- Usa fórmulas de Excel para totales y porcentajes (que el usuario pueda auditar), no valores pegados.
- Encabezado verde oscuro `#0B5640` con texto blanco, Arial, primera fila inmovilizada, formato
  `#,##0` para pesos y `0.0%` para porcentajes; una hoja "Notas" con fuente, corte y supuestos.
- Si la xlsx skill está disponible en el entorno, síguela para el formato y la verificación de fórmulas.

## Formato numérico colombiano

- Pesos: `$ 1.234.567` (miles con punto, decimales con coma). En tablas resumen: millones con un
  decimal y unidad en el encabezado: "Valor (millones de $)".
- Porcentajes: `64,8 %`. Puntos porcentuales (p. p.) para diferencias entre porcentajes.
- Fechas: `30 de septiembre de 2026` en texto; `30/09/2026` en tablas.
- `a_numero()` interpreta `$ 1.234.567,89`, `1,234,567.89`, `(1.500)` y `12,5 %`, y no convierte códigos
  presupuestales como `2.3.1.02`. Cifras como `1.234` se leen como mil doscientos treinta y cuatro.

## Referencias

- `references/indicadores-y-fuentes.md` — indicadores de gestión pública, fuentes de datos (SECOP II
  en datos.gov.co, TerriData, FUT/CHIP, SIEE), errores frecuentes y pruebas de razonabilidad.

## Datos personales

Antes de analizar bases con personas (beneficiarios, contratistas, estudiantes, pacientes), usa solo las
columnas necesarias; no muestres cédulas ni nombres en resultados agregados; datos de menores y de salud
son sensibles (Ley 1581 de 2012).
