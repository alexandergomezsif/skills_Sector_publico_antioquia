# Curso de contratación estatal — instalación y administración

Versión 2.1 (nov. 2026). Desarrollado por: **Alexander Gómez Avendaño**. Página estática (`index.html`) publicada en GitHub Pages + registro de
calificaciones en una hoja de Google mediante Apps Script.

## 1. Crear el registro en Google Sheets (una sola vez, 10 minutos)

1. Cree una hoja de cálculo nueva en Google Drive, por ejemplo "Registro curso contratación".
   Recomendación: use una cuenta institucional, no personal, porque guarda cédulas (Ley 1581).
2. Menú **Extensiones → Apps Script**. Borre el contenido de `Código.gs` y pegue el de
   `apps-script/Codigo.gs`. Guarde.
3. En el editor, seleccione la función **`configurar`** y pulse **Ejecutar**. Acepte los permisos.
   Se crean las hojas **Registros** y **Resumen**.
4. **Configuración del proyecto** (engranaje) → **Propiedades del script** → agregar:
   `CLAVE_COORDINADOR` = una clave larga (mínimo 16 caracteres) que solo conozca la coordinación.
5. **Implementar → Nueva implementación → Tipo: Aplicación web**.
   - Ejecutar como: **Yo**.
   - Quién tiene acceso: **Cualquier persona** (necesario para que la página pueda enviar registros).
   - Copie la **URL de la aplicación web** (termina en `/exec`).

## 2. Conectar la página

Opción A (recomendada): reconstruir la página con la URL incluida:

```bash
python build.py "https://script.google.com/macros/s/XXXX/exec"
```

Opción B: abra el **Panel de la coordinación** (al final de la página), pegue la URL y cargue los
resultados una vez; la URL queda guardada en ese navegador. Los participantes necesitan la opción A.

## 3. Publicar en GitHub Pages

1. Suba `index.html` a la carpeta `curso/` del repositorio (rama `main`).
2. En GitHub: **Settings → Pages → Source: Deploy from a branch → main / (root)**.
3. La dirección del curso queda así:
   `https://alexandergomezsif.github.io/skills_Sector_publico_antioquia/curso/`

## 4. Cómo se califica

**Índice de apropiación** = 20 % práctica de módulos + 30 % taller de casos + 50 % mejor evaluación final.

| Nivel | Requisitos |
|---|---|
| Avanzado | Índice ≥ 90, evaluación final ≥ 90 %, cada etapa ≥ 7 de 8, módulos y taller completos |
| Competente | Índice ≥ 80, evaluación final ≥ 80 %, cada etapa ≥ 6 de 8, módulos y taller completos |
| En desarrollo | Índice ≥ 60 o no cumple algún requisito de Competente |
| Inicial | Índice < 60 |

- Práctica: primera respuesta de las 103 preguntas de los 15 módulos.
- Taller: primera respuesta de las 32 preguntas de 14 casos + las 9 filas del cuadro comparativo de modalidades + la actividad de ordenar la licitación (42 puntos en total).
- Evaluación final: 40 preguntas al azar, 8 por etapa (Bases, Planeación, Selección, Celebración y
  ejecución, Cierre y temas especiales); se habilita al completar módulos y taller; máximo 3 intentos
  en 24 horas; cuenta el mejor.
- Constancia con **código de verificación** para niveles Competente y Avanzado. Verificación:
  `URL_DEL_SCRIPT?accion=verificar&codigo=CODIGO` (responde nivel, índice y últimos 4 dígitos de la cédula).

**Alcance:** el nivel mide la apropiación del contenido del curso. No acredita idoneidad legal ni
reemplaza la evaluación de competencias laborales o del desempeño (Talento Humano).

## 5. Limitaciones que debe conocer

| Limitación | Consecuencia | Mitigación |
|---|---|---|
| Ingreso solo con cédula, sin contraseña | Alguien podría presentar el curso con la cédula de otro | Uso formativo; si se requiere evidencia oficial, evaluación final presencial o con verificación adicional |
| El avance se guarda en el navegador de cada persona | Si cambia de equipo o borra datos del navegador, empieza de nuevo (el registro conserva su mejor resultado) | Pedir que usen siempre el mismo equipo y navegador |
| La URL del script es pública | Alguien podría enviar registros falsos | El script valida y limpia los datos; revise registros atípicos en la hoja **Registros** |
| Datos personales (cédula, nombre, resultados) | Tratamiento sujeto a la Ley 1581 de 2012 | Autorización expresa al ingresar; hoja en cuenta institucional con acceso restringido; validar con la dependencia responsable de protección de datos |

## 6. Actualizar contenido

El contenido vive en `contenido.py` (módulos, glosario, plazos) y `contenido2.py` (preguntas
adicionales, casos, actividad de orden). Después de editar: `python build.py "URL_DEL_SCRIPT"`.
Cambie la versión en `build.py` cuando cambie el contenido evaluado.
