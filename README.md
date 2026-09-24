# Resumen de ventas

Script en Python que lee un archivo de ventas en CSV y genera un resumen en texto con:

- El **total vendido por producto** (unidades e importe = cantidad × precio).
- El **producto más vendido**, medido en unidades.

## Requisitos

- Python 3.8 o superior. No necesita librerías externas (solo la biblioteca estándar).

## Formato del CSV de entrada

El archivo debe tener cabecera con las columnas `fecha`, `producto`, `cantidad` y `precio`:

```csv
fecha,producto,cantidad,precio
2026-09-01,Laptop,2,850.00
2026-09-01,Mouse,10,15.50
```

- `cantidad`: número entero de unidades.
- `precio`: precio unitario, usando punto como separador decimal.

El repositorio incluye `ventas.csv` con 20 filas de ejemplo.

## Uso

Desde la carpeta del proyecto:

```bash
python resumen_ventas.py
```

Por defecto lee `ventas.csv` y escribe `resumen.txt`. También puedes indicar otros archivos:

```bash
python resumen_ventas.py mis_ventas.csv mi_resumen.txt
```

Si falta el archivo, falta alguna columna o hay un valor no numérico, el script muestra un mensaje de error indicando el problema.

## Ejemplo de salida

Con el `ventas.csv` de ejemplo se genera este `resumen.txt`:

```
RESUMEN DE VENTAS
==================================================

Producto              Unidades               Total
--------------------------------------------------
Laptop                       8            6,800.00
Monitor                      6            1,320.00
Auriculares                 14              630.00
Mouse                       37              573.50
Webcam                       9              540.00
Teclado                     15              525.00
--------------------------------------------------
TOTAL                       89           10,388.50

Producto más vendido: Mouse (37 unidades)
```

Los productos se ordenan de mayor a menor importe total.
