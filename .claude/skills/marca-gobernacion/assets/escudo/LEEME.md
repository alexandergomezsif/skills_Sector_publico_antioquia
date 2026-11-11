# Archivos oficiales del escudo

Esta carpeta está vacía a propósito. Coloque aquí **solo** los archivos oficiales entregados por la
Dirección de Comunicaciones (publicidadymarca@antioquia.gov.co) o descargados de
https://antioquia.gov.co/imagen-de-marca.

Nombres esperados por los scripts (PNG con fondo transparente, ≥ 600 px de ancho):

| Archivo | Uso |
|---|---|
| `escudo-color-pantalla.png` | **Incluido.** PNG oficial del portal antioquia.gov.co sin margen, 157 × 70 px (mínimo de pantalla del manual: 150 × 67). Tomado del aplicativo VUR de la Secretaría de Infraestructura. Sirve para pantalla y presentaciones; para impresión pida la versión en alta resolución |
| `escudo-color.png` | Versión principal a color con "GOBERNACIÓN DE ANTIOQUIA / República de Colombia" |
| `escudo-blanco.png` | Versión invertida para fondos oscuros (requiere autorización) |
| `escudo-<secretaria>.png` | Versión de membrete con el nombre de la dependencia (opcional) |

Los scripts usan `escudo-color.png` si existe y, si no, `escudo-color-pantalla.png`. Si ninguno existe, `crear_informe.py` y `crear_presentacion.py` ponen un marcador rotulado
"ESCUDO OFICIAL" para que nadie publique una pieza sin el emblema correcto.

No suba al repositorio versiones redibujadas, recortadas o modificadas.
