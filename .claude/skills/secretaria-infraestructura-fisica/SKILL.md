---
name: secretaria-infraestructura-fisica
description: Funcionamiento de la Secretaría de Infraestructura Física de la Gobernación de Antioquia (SIF) - estructura y funciones oficiales de cada dependencia, estructuración de proyectos (MGA, BPIN, SGR, maduración), gestión predial (Ley 1682, avalúos IGAC, expropiación), gestión social y ambiental (licencias, PAGA, permisos), asuntos legales, proyectos y metas del Plan Vial, administración y finanzas, valorización (Ordenanza 46 de 2022), gestión contractual de obra e interventoría y coordinación del Despacho. Úsala para cualquier tarea de una dependencia de la SIF.
---

# Secretaría de Infraestructura Física (SIF) — Gobernación de Antioquia

Mapa de trabajo para servidores y contratistas de la SIF. Primero ubica la dependencia responsable;
luego aplica la referencia del área y, si hace falta, las skills técnicas, contractuales y jurídicas.

## 1. Ubica la dependencia (Decreto Ordenanzal 2024070003913 de 2024)

| Si la tarea trata de… | Dependencia | Referencia |
|---|---|---|
| Prioridades, Plan Vial, inventario vial, MGA/BPIN, estudios y diseños, proyectos SGR | Dirección de Estructuración de Proyectos | `references/estructuracion-proyectos.md` |
| Valorización, nuevos instrumentos de financiación, ordenanzas de obras | Dirección de Instrumentos de Financiación | `references/administrativa-financiera-valorizacion.md` §2 |
| APP y proyectos estratégicos | Subsecretaría de Planeación, Proyectos Estratégicos y APPs | `references/estructuracion-proyectos.md` §5 |
| Obras viales, mantenimiento de la red, supervisión de obra, contratos con Rentan, emergencias | Dirección de Desarrollo Físico | skill `ingenieria-vial-obras` + `references/proyectos-infraestructura-sif.md` |
| Red terciaria, placa huella, convenios con municipios, FNC y JAC; equipamientos y espacio público | Dirección de Infraestructura y Apoyo Territorial | `references/proyectos-infraestructura-sif.md` + `references/asuntos-legales-sif.md` §3 |
| Predios, avalúos, expropiación, saneamiento | Dirección de Gestión Social, Ambiental y Predial | `references/gestion-predial.md` |
| Licencias y permisos ambientales, PAGA, socialización, reasentamiento, consulta previa | Dirección de Gestión Social, Ambiental y Predial | `references/gestion-social-ambiental.md` |
| Conceptos, revisión contractual, sancionatorios, liquidaciones, PQRSD, control, defensa | Dirección de Asuntos Legales | `references/asuntos-legales-sif.md` + skills `contratacion-estatal` y `derecho-publico-colombiano` |
| Presupuesto, CDP/RP, informes financieros, facturación y cartera, cobro persuasivo | Dirección Administrativa y Financiera | `references/administrativa-financiera-valorizacion.md` §1 |
| Comités, tablero de metas, Asamblea, Consejo de Gobierno, riesgos del proceso | Despacho y subsecretarías | `references/direccion-coordinacion-sif.md` |
| Cualquier proceso de obra, interventoría o consultoría | Dependencia técnica + Asuntos Legales | `contratacion-estatal/references/contratacion-obra-infraestructura.md` |

Estructura completa, funciones oficiales y flujo entre dependencias: `references/estructura-y-funciones-sif.md`.

## 2. Reglas de esta skill

1. **Cita la función del decreto de estructura** cuando un documento asigne responsabilidades a una
   dependencia; no inventes competencias. Si un acto antiguo usa nombres de la estructura de 2020
   (Proyectos Especiales, Director Operativo predial), tradúcelos con la tabla de equivalencias.
2. **Cifras de metas, contratos y valores** con fuente y fecha (informe de gestión, SECOP II, boletín).
   Para datos actuales consulta SECOP II con `contratacion-estatal/scripts/consultar_secop.py`.
3. **Competencia sobre la vía** antes de cualquier proyecto: malla R10 (`ingenieria-vial-obras`).
4. **Predios y valorización** tocan datos personales (propietarios, matrículas, deudas): úsalos solo en
   documentos internos; en informes públicos agrega por proyecto o municipio.
5. **Neutralidad (Ley 2345 de 2023)**: describe obras, metas y cifras; no atribuyas logros a personas ni
   uses lemas de gobierno.
6. Los conceptos, actos y estudios son **borradores** para revisión de la dependencia competente.

## 3. Herramientas

```bash
# SECOP II (contratos del Departamento; filtro de infraestructura por objeto)
python .claude/skills/contratacion-estatal/scripts/consultar_secop.py resumen --infra --desde 2026-01-01
python .claude/skills/contratacion-estatal/scripts/consultar_secop.py buscar "pavimentacion" --tipo Obra --desde 2025-01-01 --salida pav.xlsx

# Malla vial R10 y costos de maquinaria
python .claude/skills/ingenieria-vial-obras/scripts/consultar_red_vial.py buscar "25AN01"
python .claude/skills/ingenieria-vial-obras/scripts/costo_frentes.py --listar
```

## 4. Plantillas

- `plantillas/lista-maduracion-proyecto.md` — chequeo antes de radicar un proceso de obra o interventoría.
- `plantillas/ficha-predial.md` — ficha por predio para la gestión predial (uso interno).
- Además: `ingenieria-vial-obras/plantillas/*` (visita técnica, emergencia, frentes) y
  `contratacion-estatal/plantillas/*` (estudios previos, matriz de riesgos, liquidación, incumplimiento).

## 5. Fuentes base

antioquia.gov.co (páginas de la SIF y de cada dirección; Gaceta Departamental; informes de gestión Ley
951 de 2005, 2023-2026); colombiacompra.gov.co (Documentos Tipo y relatoría); datos.gov.co (SECOP II);
Función Pública (leyes 1682, 1742, 1882); IGAC (resoluciones de avalúos); MinAmbiente (Decreto 1076).
