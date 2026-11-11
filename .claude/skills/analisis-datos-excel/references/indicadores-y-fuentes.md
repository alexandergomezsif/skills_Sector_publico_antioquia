# Indicadores, fuentes y errores frecuentes

## Indicadores de gestión frecuentes

| Ámbito | Indicador | Fórmula | Nota |
|---|---|---|---|
| Presupuesto | % compromisos | Compromisos / Apropiación definitiva | Lo que más se reporta como "ejecución" |
| Presupuesto | % obligaciones | Obligaciones / Apropiación definitiva | Refleja bienes/servicios recibidos |
| Presupuesto | % pagos | Pagos / Apropiación definitiva | Ejecución de caja |
| Presupuesto | Rezago | Compromisos − Obligaciones | Reserva potencial al cierre |
| Plan de desarrollo | Avance de meta | Logro acumulado / Meta (cuatrienio o vigencia) | Respetar el tipo de indicador: acumulable, mantenimiento, reducción |
| Plan de desarrollo | Avance ponderado del programa | Σ (avance indicador × peso) | Pesos definidos por Planeación |
| Contratación | Participación por modalidad | Valor modalidad / Valor total | Señal de alerta si contratación directa es alta |
| Contratación | Pluralidad | Promedio de oferentes por proceso competitivo | Baja pluralidad → revisar requisitos |
| Contratación | Ahorro | (Presupuesto oficial − Valor adjudicado) / Presupuesto oficial | |
| Contratación | Adiciones | Σ adiciones / Valor inicial | Límite legal 50 % por contrato (en SMMLV) |
| Contratación | Avance físico vs. financiero | % físico − % financiero | Negativo grande = pagos adelantados a la ejecución |
| PQRSD | Oportunidad | Respondidas en término / Total vencidas en el periodo | Calcular términos con días hábiles |
| Talento humano | Provisionalidad | Empleos en provisionalidad / Empleos de carrera | |

### Tipos de indicador de meta (para no sumar mal)

- **Acumulable:** el logro de cada año se suma (ej. km de vías intervenidas).
- **Mantenimiento:** se mantiene un nivel cada año (ej. 100 % de municipios asistidos) → no sumar; usar el del año.
- **Reducción:** la meta es bajar (ej. tasa de mortalidad) → avance = (línea base − valor actual) / (línea base − meta).
- **Capacidad / stock:** valor a una fecha (ej. cobertura).

## Fuentes de datos públicas

| Fuente | Contenido |
|---|---|
| datos.gov.co — SECOP II Contratos/Procesos | Exporte de contratos por entidad (filtrar "Gobernación de Antioquia" y NIT 890900286-0 [verificar]) |
| SECOP II — búsqueda pública | Documentos de cada proceso |
| TerriData (DNP) | Indicadores territoriales por municipio y departamento |
| CHIP / FUT (Contaduría) | Ejecución presupuestal y contable reportada |
| Portal de Transparencia Económica / SGR (GESPROY) | Regalías |
| DANE | Población (proyecciones), pobreza, censos |
| SIEE / Mapa Regalías | Proyectos de inversión |
| Anuario Estadístico de Antioquia (DAP) | Estadísticas departamentales |

## Errores frecuentes en exportes institucionales

1. Títulos y fechas en las primeras filas → la tabla real empieza más abajo.
2. Filas de **subtotal y total** mezcladas con el detalle → doble conteo.
3. Cifras en **miles o millones** sin decirlo en la celda.
4. Números como texto con `$`, puntos de miles o espacios.
5. Celdas combinadas que dejan vacíos en columnas de agrupación (rellenar hacia abajo con criterio).
6. Nombres de dependencias con variaciones ("Sec. Educación", "SECRETARIA DE EDUCACION") → normalizar
   con una tabla de equivalencias explícita (estructura vigente desde 2025: ver `contexto/gobernacion-antioquia.md`).
7. Vigencias mezcladas (reservas de años anteriores con presupuesto de la vigencia).
8. Fechas como texto en formatos distintos (dd/mm/aaaa vs. mm/dd/aaaa).
9. Filtros activos u hojas ocultas en el archivo original.
10. Duplicados por contratos con varias modificaciones (una fila por modificación).

## Pruebas de razonabilidad

- Pagos ≤ Obligaciones ≤ Compromisos ≤ CDP ≤ Apropiación definitiva (por rubro). Reportar excepciones.
- Fecha de inicio ≤ fecha de terminación; contratos con plazo negativo o de más de 10 años: revisar.
- Valores negativos: ¿reversiones, reducciones o error?
- Concentración: un registro que pese más del 50 % del total merece verificación.
