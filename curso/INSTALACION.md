# Curso de contratación estatal — instalación y administración

Versión 3.0, piloto (nov. 2026). Desarrollado por: **Alexander Gómez Avendaño**.

## Estado actual (27-nov-2026)

- Registro en Google Sheets **instalado** en la cuenta del autor: hoja "Curso Contratación Estatal - Registro de
  participantes", proyecto de Apps Script "Registro Curso Contratacion Estatal", implementación de app web con acceso
  "Cualquiera".
- La URL del script está en `endpoint.txt`; `build.py` la usa por defecto.
- La clave del panel de coordinación la generó el propio script (`generarClaveCoordinador`). Consúltela en
  Apps Script > Configuración del proyecto > Propiedades del script > `CLAVE_COORDINADOR`. No la publique.
- Curso en línea: https://alexandergomezsif.github.io/skills_Sector_publico_antioquia/curso/
- **Inscripción con aprobación de la coordinación** (implementación versión 4, 27-nov-2026):
  1. La persona escribe cédula, nombre, correo, dependencia y vinculación. Queda **pendiente** en la pestaña Inscritos.
  2. Al correo de la cuenta dueña del script llega "Inscripción al curso: [nombre]" con los botones **Aprobar** y
     **Rechazar**. Cada botón abre la página del curso (`#/coordinacion/...`), que muestra los datos y pide confirmar.
     No se usa una página del propio script porque Google la bloquea ("No se pudo abrir el archivo") cuando el
     navegador tiene varias cuentas de Google abiertas. Para reenviar avisos pendientes: ejecute
     `reenviarAvisosPendientes` en el editor. Los enlaces llevan
     una firma HMAC (`SECRETO_FIRMA` en Propiedades del script, se crea sola); si se alteran, no funcionan.
  3. Al aprobar, la persona recibe el correo de bienvenida con el botón **Entrar al curso**: un enlace personal
     (`#/acceso/<cédula>/<token>`) que abre el curso ya identificado. No hay códigos que copiar.
  4. Si cambia de equipo, vuelve a escribir cédula y correo y le llega de nuevo su enlace (sin nueva aprobación).
  5. Para que los avisos lleguen a otro correo: Propiedades del script > `CORREO_COORDINADOR`.
  - Cupo: unos 100 correos al día (Gmail gratuito); cada inscripción usa 2. Los eventos sin token válido se rechazan.
  - Rechazar a alguien ya aprobado le retira el acceso; su avance registrado se conserva.
  - Nota técnica: Google reserva el parámetro `c` en las direcciones `/exec`; por eso el enlace usa `ced`.
- Si cambia el código del script: Implementar > Administrar implementaciones > editar (lápiz) > Versión: Nueva versión >
  Implementar. La dirección no cambia.
- **Consola de administración** (`admin.html`, implementación versión 6): https://alexandergomezsif.github.io/skills_Sector_publico_antioquia/curso/admin.html
  Entra con la clave de coordinación (Propiedades del script › `CLAVE_COORDINADOR`); la clave viaja solo en el cuerpo
  del POST y se borra al cerrar la pestaña. Funciones: aprobar o rechazar pendientes, ver inscritos y avance, reenviar
  el enlace de entrada, retirar acceso, descargar CSV e invitar por correo (máx. 50 por envío; pestaña
  **Invitaciones** en la hoja). Tras 20 claves erradas en una hora se bloquea el acceso durante una hora.
  El panel de coordinación ya no está en la página de los estudiantes.
- Pendiente recomendado: pasar la hoja a una cuenta institucional de la Gobernación (Ley 1581 de 2012).
 Página estática (`index.html`) publicada en GitHub Pages + registro de
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
