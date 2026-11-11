#!/usr/bin/env python3
"""Regenera las plantillas de ejemplo (plantillas/*.docx, *.pptx) a partir de ejemplos/*.json."""
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
S = RAIZ / ".claude" / "skills"
TAREAS = [
    (S / "informes-institucionales/scripts/crear_informe.py", "ejemplos/informe-ejemplo.json", "plantillas/informe-supervision.docx"),
    (S / "presentaciones-institucionales/scripts/crear_presentacion.py", "ejemplos/presentacion-ejemplo.json", "plantillas/presentacion-ejemplo.pptx"),
]

for script, entrada, salida in TAREAS:
    subprocess.run([sys.executable, str(script), str(RAIZ / entrada), str(RAIZ / salida)], check=True)
