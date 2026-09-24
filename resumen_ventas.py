"""Genera un resumen de ventas a partir de un archivo CSV.

Lee un CSV con las columnas fecha, producto, cantidad y precio, y escribe
un archivo de texto con el total vendido por producto y el producto más
vendido (por unidades).

Uso:
    python resumen_ventas.py [entrada.csv] [salida.txt]
"""

import csv
import sys
from collections import defaultdict
from decimal import Decimal, InvalidOperation

COLUMNAS = {"fecha", "producto", "cantidad", "precio"}


def leer_ventas(ruta_csv):
    """Devuelve dos diccionarios: unidades e importe total por producto."""
    unidades = defaultdict(int)
    importes = defaultdict(Decimal)

    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        faltantes = COLUMNAS - set(lector.fieldnames or [])
        if faltantes:
            raise ValueError(f"Faltan columnas en el CSV: {', '.join(sorted(faltantes))}")

        for num_linea, fila in enumerate(lector, start=2):
            producto = fila["producto"].strip()
            try:
                cantidad = int(fila["cantidad"])
                precio = Decimal(fila["precio"])
            except (ValueError, InvalidOperation):
                raise ValueError(f"Valor no numérico en la línea {num_linea}: {fila}")
            unidades[producto] += cantidad
            importes[producto] += cantidad * precio

    return unidades, importes


def generar_resumen(unidades, importes):
    """Construye el texto del resumen."""
    if not unidades:
        return "No hay ventas registradas.\n"

    lineas = ["RESUMEN DE VENTAS", "=" * 50, ""]
    lineas.append(f"{'Producto':<20}{'Unidades':>10}{'Total':>20}")
    lineas.append("-" * 50)
    for producto in sorted(importes, key=importes.get, reverse=True):
        lineas.append(f"{producto:<20}{unidades[producto]:>10}{importes[producto]:>20,.2f}")
    lineas.append("-" * 50)
    lineas.append(f"{'TOTAL':<20}{sum(unidades.values()):>10}{sum(importes.values()):>20,.2f}")
    lineas.append("")

    mas_vendido = max(unidades, key=unidades.get)
    lineas.append(
        f"Producto más vendido: {mas_vendido} ({unidades[mas_vendido]} unidades)"
    )
    return "\n".join(lineas) + "\n"


def main():
    entrada = sys.argv[1] if len(sys.argv) > 1 else "ventas.csv"
    salida = sys.argv[2] if len(sys.argv) > 2 else "resumen.txt"

    try:
        unidades, importes = leer_ventas(entrada)
    except FileNotFoundError:
        sys.exit(f"Error: no se encontró el archivo '{entrada}'.")
    except ValueError as e:
        sys.exit(f"Error: {e}")

    resumen = generar_resumen(unidades, importes)
    with open(salida, "w", encoding="utf-8") as f:
        f.write(resumen)

    print(f"Resumen generado en '{salida}'.")


if __name__ == "__main__":
    main()
