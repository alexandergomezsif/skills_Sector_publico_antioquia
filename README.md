# Claude para la Gobernación de Antioquia

Repositorio de contexto, *skills* y plantillas para que Claude asista a servidores públicos y
contratistas de la Gobernación de Antioquia en informes, presentaciones, contratación estatal,
derecho público y análisis de datos, respetando el Manual de Identidad Visual y la normativa vigente.

> **Corte normativo: noviembre de 2026.** El contenido no sustituye a la Oficina Jurídica, la Dirección
> Contractual ni al supervisor. Todo producto es un borrador que revisa y firma el servidor competente.

## Qué incluye

```
CLAUDE.md                         Reglas de trabajo, datos clave y alertas normativas (se lee al iniciar)
contexto/                         Estructura, Plan de Desarrollo, valores 2026, fuentes, glosario, mantenimiento
.claude/skills/
  marca-gobernacion/              Colores, tipografía, escudo, austeridad, Ley 2345 (tokens JSON/CSS)
  informes-institucionales/       Estructuras de informe, lenguaje claro, generador .docx con membrete
  presentaciones-institucionales/ Guion por mensajes y generador .pptx 16:9 con gráficos nativos
  contratacion-estatal/           Marco normativo, modalidades, ciclo, supervisión, novedades 2026,
                                  Ley de Garantías, documentos tipo, 7 plantillas, calculadora de cuantías
  derecho-publico-colombiano/     Peticiones, CPACA, régimen departamental, presupuesto, transparencia,
                                  disciplinario, 4 plantillas, calculadora de días hábiles con festivos
  analisis-datos-excel/           Perfilador de calidad, ejecución presupuestal, tablas resumen
ejemplos/                         JSON de ejemplo, Excel ficticio, solicitudes sugeridas
plantillas/                       Informe y presentación de ejemplo generados por los scripts
scripts/                          Empaquetar skills (.zip) y regenerar plantillas
```

## Cómo usarlo

### Opción A — Claude Code (recomendada para equipos técnicos)

```bash
git clone <url-del-repositorio> && cd gobernacion-antioquia-claude
pip install -r requirements.txt
claude
```

Claude Code lee `CLAUDE.md` y carga las skills de `.claude/skills/` automáticamente. Trabaje dentro de
la carpeta y ponga sus archivos de insumo en `datos/` (excluida de Git).

### Opción B — Claude en la web o la app de escritorio

1. Genere los paquetes: `python scripts/empaquetar_skills.py` → carpeta `dist/` con un .zip por skill,
   más `contexto-gobernacion-antioquia.zip` (lleva `CLAUDE.md` y `contexto/`).
2. Suba cada .zip como skill personalizada (requiere plan con ejecución de código habilitada). Según el
   centro de ayuda de Claude, se suben en **Customize > Skills** con la opción de cargar un ZIP; en planes
   Team y Enterprise, un propietario puede aprovisionarlas para toda la organización. Ver
   [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
3. Opcional: cree un **Proyecto** y pegue el contenido de `CLAUDE.md` en sus instrucciones.

### Escudo oficial

El repositorio incluye el PNG oficial del portal antioquia.gov.co en resolución de pantalla (157 × 70 px),
que usan los generadores de Word y PowerPoint. Para impresión, pida a la Dirección de Comunicaciones la
versión en alta resolución y guárdela como `.claude/skills/marca-gobernacion/assets/escudo/escudo-color.png`
(ver `LEEME.md` allí); los scripts la preferirán automáticamente.

## Herramientas incluidas

| Script | Para qué | Ejemplo |
|---|---|---|
| `crear_informe.py` | JSON → Word con membrete, Arial 12, tablas, KPIs, alertas, firmas | `python .claude/skills/informes-institucionales/scripts/crear_informe.py ejemplos/informe-ejemplo.json salida.docx` |
| `crear_presentacion.py` | JSON → PowerPoint 16:9 con marca y gráficos editables | `python .claude/skills/presentaciones-institucionales/scripts/crear_presentacion.py ejemplos/presentacion-ejemplo.json salida.pptx` |
| `calcular_cuantias.py` | Menor/mínima cuantía, Ley de Garantías, límite de adiciones del 50 % en SMMLV | `--anio 2026 --presupuesto-smmlv 5000000` |
| `dias_habiles.py` | Vencimientos en días hábiles con festivos colombianos | `--desde 2026-11-11 --dias 15` |
| `perfilar_excel.py` | Diagnóstico de calidad de un Excel antes de analizarlo | `ejemplos/ejecucion-ficticia.xlsx` |
| `ejecucion_presupuestal.py` | Ejecución por dependencia/rubro con Excel de fórmulas vivas | `--agrupar Dependencia` |
| `tabla_resumen.py` | Tabla dinámica de cualquier base (p. ej. exporte SECOP II) | `--agrupar Modalidad --sumar Valor --moneda` |

## Puntos que deben confirmarse con la Gobernación

Marcados como **[POR VERIFICAR]** en los archivos. Los principales:

1. Cuantías oficiales 2026 publicadas por la entidad (el repositorio las calcula suponiendo presupuesto
   ≥ 1.200.000 SMMLV).
2. Delegaciones contractuales posteriores al Decreto 2025070000089 de 2025.
3. Dependencias internas exactas del Decreto Ordenanzal 2024070003913 de 2024.
4. Plantilla oficial de presentaciones y escudo en alta resolución para impresión (Dirección de Comunicaciones).
5. Número de la ordenanza del estatuto orgánico de presupuesto departamental.
6. Fallo de fondo del Consejo de Estado sobre el salario mínimo 2026 y control de constitucionalidad
   del Decreto Legislativo 1420 de 2026.
7. Fecha exacta de entrada en vigencia de la compra pública sostenible (Decreto 0997, art. 14) para
   departamentos de categoría especial.

## Mantenimiento

Ver `contexto/mantenimiento.md`. Cambios por *pull request* con la fuente oficial enlazada y registro en
`CHANGELOG.md`.

## Seguridad y datos

- No suba al repositorio bases con datos personales, información clasificada o reservada.
- Antes de compartir datos con Claude, use solo las columnas necesarias y anonimice cuando sea posible
  (Ley 1581 de 2012, Ley 1712 de 2014) y siga las políticas de seguridad de la información de la entidad.
