"""Validación experimental de insertion sort y merge sort."""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def medir_tiempo(algoritmo, datos: list[int]) -> float:
    """Mide el tiempo de ejecución de un algoritmo de ordenamiento.

    Args:
        algoritmo: función de ordenamiento que se desea medir.
        datos: lista de datos que será ordenada.

    Returns:
        Tiempo de ejecución en segundos.
    """
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()

    return fin - inicio


def main() -> None:
    """Ejecuta la comparación experimental de los dos algoritmos."""
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_insertion = []
    tiempos_merge = []

    for n in tamanos:
        datos = generar_aleatorio(n)

        tiempo_insertion = medir_tiempo(insertion_sort, datos)
        tiempo_merge = medir_tiempo(merge_sort, datos)

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

        print(
            f"{n}: "
            f"insertion_sort = {tiempo_insertion:.6f}s, "
            f"merge_sort = {tiempo_merge:.6f}s"
        )

    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanos,
        tiempos_insertion,
        marker="o",
        label="Insertion sort",
    )

    plt.plot(
        tamanos,
        tiempos_merge,
        marker="o",
        label="Merge sort",
    )

    plt.title("Comparación de tiempo de ejecución")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    plt.savefig("graficas/parte4_tiempo.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()