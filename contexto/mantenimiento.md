# Mantenimiento del repositorio

El repositorio solo es útil si está al día. Responsable sugerido: un enlace de la Secretaría General
(Dirección Contractual) y uno de la Dirección de Comunicaciones.

## Cada enero

- [ ] SMMLV y auxilio de transporte → `contexto/valores-referencia.md`, `CLAUDE.md` §3, `calcular_cuantias.py` (constante `SMMLV_POR_ANIO`).
- [ ] UVT → mismos archivos.
- [ ] Presupuesto aprobado (ordenanza) y cuantías oficiales publicadas por la Gobernación.
- [ ] Festivos: el script `dias_habiles.py` los calcula (Ley 51 de 1983); verificar si una ley nueva agregó alguno.
- [ ] Categoría del departamento.

## Con cada cambio normativo

- [ ] Nuevo decreto que modifique el Decreto 1082 de 2015 → `contratacion-estatal/references/marco-normativo.md` y `novedades-2026.md`.
- [ ] Nuevas versiones de Documentos Tipo → `contratacion-estatal/references/documentos-tipo.md`.
- [ ] Circular de CCE sobre Ley de Garantías → `contratacion-estatal/references/ley-garantias.md`.
- [ ] Reforma al manual de contratación departamental o a delegaciones → `contexto/gobernacion-antioquia.md`.
- [ ] Fin o prórroga del régimen de emergencia del terremoto (Decreto 1420 de 2026) → `novedades-2026.md`.

## Infraestructura vial (cada semestre)

- [ ] Versión vigente de las Especificaciones Generales de Construcción, manuales INVIAS y Manual de Señalización → `ingenieria-vial-obras/references/normativa-tecnica-vial.md`.
- [ ] Estado de los proyectos normativos marcados [POR VERIFICAR] (SINC v5, CCP-14 Sección 13, Manual de Estabilidad de Taludes, categorización 2026).
- [ ] Estructura y conteos del servicio R10 (`consultar_red_vial.py conteo`; si cambian los campos, actualizar el script y `red-vial-antioquia-r10.md`).
- [ ] Estructura de la SIF y funciones por dependencia (si cambia el decreto de estructura) → `secretaria-infraestructura-fisica/references/estructura-y-funciones-sif.md`.
- [ ] Versiones de Documentos Tipo de infraestructura de transporte → `contratacion-estatal/references/contratacion-obra-infraestructura.md`.
- [ ] Metas y programas de la SIF (informes de gestión y SECOP II) → `secretaria-infraestructura-fisica/references/proyectos-infraestructura-sif.md`.
- [ ] Estatuto de valorización y proyectos vigentes → `administrativa-financiera-valorizacion.md`.
- [ ] Campos del conjunto SECOP II jbjy-vk9h (si cambian, actualizar `consultar_secop.py`).
- [ ] Tarifas de maquinaria del contrato vigente → `ingenieria-vial-obras/assets/tarifas-maquinaria-2026.json` (renombrar con el año).

## Con cada versión del Manual de Identidad Visual

- [ ] Colores, tipografía y reglas → `marca-gobernacion/SKILL.md`, `assets/marca.json`.
- [ ] Reemplazar archivos del escudo en `marca-gobernacion/assets/escudo/` (solo los entregados por la Dirección de Comunicaciones).
- [ ] Regenerar plantillas: `python scripts/regenerar_plantillas.py` (ver README).

## Al cambiar de administración (2028)

- [ ] Nuevo Plan de Desarrollo (ordenanza) → `contexto/gobernacion-antioquia.md`.
- [ ] Nueva estructura administrativa si la hay.
- [ ] Revisar que no queden referencias al plan anterior en plantillas.

## Control de cambios

Toda modificación por *pull request*, con la fuente oficial enlazada en la descripción.
Registrar en `CHANGELOG.md`.
