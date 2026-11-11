#!/usr/bin/env python3
"""
Empaqueta cada skill de .claude/skills/ como .zip para subirla a Claude (claude.ai / app de escritorio),
más una skill adicional "contexto-gobernacion-antioquia" que lleva CLAUDE.md y la carpeta contexto/
(en la app no se lee CLAUDE.md automáticamente).

Uso:
    python scripts/empaquetar_skills.py            # crea dist/*.zip
"""
import shutil
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = RAIZ / ".claude" / "skills"
DIST = RAIZ / "dist"

SKILL_CONTEXTO = """---
name: contexto-gobernacion-antioquia
description: Contexto institucional y reglas de trabajo para asistir a servidores de la Gobernación de Antioquia (estructura, Plan de Desarrollo 2024-2027, normas departamentales, valores 2026, fuentes oficiales, alertas normativas). Úsala en cualquier tarea de la Gobernación.
---

# Contexto Gobernación de Antioquia

Lee `CLAUDE.md` (reglas de trabajo, datos clave y alertas vigentes) al empezar cualquier tarea para la
Gobernación de Antioquia. Consulta según necesidad:

- `contexto/gobernacion-antioquia.md` — naturaleza jurídica, Plan de Desarrollo, estructura, sistemas.
- `contexto/valores-referencia.md` — SMMLV, UVT, cuantías, fechas electorales.
- `contexto/fuentes-oficiales.md` — dónde verificar normas y jurisprudencia.
- `contexto/glosario.md` — términos de presupuesto, contratación y gestión.
- `contexto/mantenimiento.md` — qué actualizar y cuándo.

Las demás skills (marca-gobernacion, informes-institucionales, presentaciones-institucionales,
contratacion-estatal, derecho-publico-colombiano, analisis-datos-excel) se complementan con esta.
"""

IGNORAR = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def zip_dir(origen: Path, destino: Path):
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(origen.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                z.write(f, Path(origen.name) / f.relative_to(origen))


def main():
    DIST.mkdir(exist_ok=True)
    for skill in sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").exists()):
        destino = DIST / f"{skill.name}.zip"
        zip_dir(skill, destino)
        print("✓", destino.relative_to(RAIZ))

    tmp = DIST / "_tmp" / "contexto-gobernacion-antioquia"
    if tmp.parent.exists():
        shutil.rmtree(tmp.parent)
    tmp.mkdir(parents=True)
    (tmp / "SKILL.md").write_text(SKILL_CONTEXTO, encoding="utf-8")
    shutil.copy(RAIZ / "CLAUDE.md", tmp / "CLAUDE.md")
    shutil.copytree(RAIZ / "contexto", tmp / "contexto", ignore=IGNORAR)
    destino = DIST / "contexto-gobernacion-antioquia.zip"
    zip_dir(tmp, destino)
    shutil.rmtree(tmp.parent)
    print("✓", destino.relative_to(RAIZ))


if __name__ == "__main__":
    main()
