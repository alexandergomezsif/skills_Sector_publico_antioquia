---
name: derecho-publico-colombiano
description: Derecho administrativo y público colombiano para servidores de la Gobernación de Antioquia - derechos de petición y PQRSD, actos administrativos (CPACA), recursos, disciplinario, régimen departamental, presupuesto, transparencia, datos personales, archivo y conceptos jurídicos. Incluye cálculo de días hábiles.
---

# Derecho público colombiano — Gobernación de Antioquia

## Principios

1. **No citar de memoria.** Verifica texto y vigencia en SUIN-Juriscol, Secretaría del Senado o el
   Gestor Normativo de Función Pública (ver `contexto/fuentes-oficiales.md` en la raíz del repositorio).
   Revisa modificaciones (p. ej. Ley 2080 de 2021 al CPACA; Ley 2094 de 2021 al Código Disciplinario)
   y sentencias de constitucionalidad.
2. **Separa** obligación legal (norma y artículo) / interpretación (Corte Constitucional, Consejo de
   Estado, Función Pública, Sala de Consulta) / recomendación práctica.
3. **Competencia primero:** ¿la dependencia es competente? Si no, traslado (art. 21 CPACA) dentro de
   5 días hábiles.
4. **Términos en días hábiles** con `scripts/dias_habiles.py` (festivos de Colombia incluidos).
5. **Señala incertidumbre** y lo no verificado. No reemplazas a la Oficina Jurídica ni a la Secretaría
   General; los actos los firma el competente.

## Flujo para un caso

1. Hechos: quién, qué, cuándo (fechas de radicación en Mercurio), qué pide, qué pruebas hay.
2. Calificación: tipo de actuación (petición, recurso, solicitud de revocatoria, queja disciplinaria,
   requerimiento de control, tutela), norma aplicable, autoridad competente, término.
3. Verificación normativa en fuente oficial.
4. Respuesta o acto: plantillas en `plantillas/`.
5. Cierre: resumen, riesgos (tutela por violación del derecho de petición, silencio, nulidad,
   disciplinario), datos faltantes.

## Herramientas

```bash
python .claude/skills/derecho-publico-colombiano/scripts/dias_habiles.py --desde 2026-11-11 --dias 15
python .claude/skills/derecho-publico-colombiano/scripts/dias_habiles.py --festivos 2027
```

## Referencias

| Archivo | Contenido |
|---|---|
| `references/peticiones-pqrsd.md` | Ley 1755 de 2015, términos, contenido mínimo de la respuesta, reserva, traslados |
| `references/actos-administrativos.md` | CPACA: elementos, motivación, publicación, notificación, recursos, firmeza, revocatoria, sancionatorio, medios de control |
| `references/regimen-departamental.md` | Constitución, Ley 2200 de 2022, ordenanzas, decretos, delegación, Ley 617 de 2000 |
| `references/presupuesto-publico.md` | Decreto 111 de 1996, Ley 819 de 2003, vigencias futuras, CDP/RP, reservas, SGR |
| `references/transparencia-datos-archivo.md` | Ley 1712 de 2014, Ley 1581 de 2012, Ley 594 de 2000, MIPG, PTEP |
| `references/disciplinario-empleo.md` | Ley 1952 de 2019 (mod. Ley 2094 de 2021), Ley 909 de 2004, prestación de servicios |

## Plantillas

- `plantillas/respuesta-peticion.md` — respuesta de fondo a derecho de petición.
- `plantillas/traslado-competencia.md` — remisión por falta de competencia.
- `plantillas/acto-administrativo.md` — estructura de decreto o resolución departamental.
- `plantillas/concepto-juridico.md` — concepto jurídico interno.

## Estilo

Español, directo, con títulos; cita norma y artículo en cada afirmación jurídica con enlace oficial;
termina con resumen y datos faltantes. Lenguaje claro en todo lo que va a la ciudadanía.
