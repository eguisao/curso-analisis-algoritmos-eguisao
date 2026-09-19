"""Experimento de mejor, peor y caso promedio para insertion sort."""

import os
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


def medir_escenario(datos: list[int]) -> tuple[float, int]:
    """Mide el tiempo y las comparaciones de insertion sort.

    Args:
        datos: lista de indices de riesgo que se va a ordenar.

    Returns:
        Una tupla con el tiempo de ejecucion en segundos y
        el numero de comparaciones realizadas.
    """
    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()

    return fin - inicio, comparaciones


def crear_graficas(
    tamanos: list[int],
    tiempos: dict[str, list[float]],
    comparaciones: dict[str, list[int]],
) -> None:
    """Crea y guarda las graficas de la Parte 3.

    Args:
        tamanos: tamaños utilizados en el experimento.
        tiempos: tiempos de ejecucion por escenario.
        comparaciones: comparaciones por escenario.
    """
    os.makedirs("graficas", exist_ok=True)

    plt.figure()
    plt.plot(tamanos, comparaciones["A"], marker="o", label="Escenario A")
    plt.plot(tamanos, comparaciones["B"], marker="o", label="Escenario B")
    plt.plot(tamanos, comparaciones["C"], marker="o", label="Escenario C")
    plt.title("Comparaciones de insertion sort por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    plt.figure()
    plt.plot(tamanos, tiempos["A"], marker="o", label="Escenario A")
    plt.plot(tamanos, tiempos["B"], marker="o", label="Escenario B")
    plt.plot(tamanos, tiempos["C"], marker="o", label="Escenario C")
    plt.title("Tiempo de ejecución de insertion sort por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


def main() -> None:
    """Ejecuta las mediciones y genera las graficas."""
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos = {
        "A": [],
        "B": [],
        "C": [],
    }

    comparaciones = {
        "A": [],
        "B": [],
        "C": [],
    }

    for n in tamanos:
        datos_a = generar_aleatorio(n, 42)
        datos_b = generar_casi_ordenado(n, 42)
        datos_c = generar_inverso(n)

        tiempo_a, comparaciones_a = medir_escenario(datos_a)
        tiempo_b, comparaciones_b = medir_escenario(datos_b)
        tiempo_c, comparaciones_c = medir_escenario(datos_c)

        tiempos["A"].append(tiempo_a)
        tiempos["B"].append(tiempo_b)
        tiempos["C"].append(tiempo_c)

        comparaciones["A"].append(comparaciones_a)
        comparaciones["B"].append(comparaciones_b)
        comparaciones["C"].append(comparaciones_c)

        print(f"\nTamaño: {n}")
        print(
            f"Escenario A - Tiempo: {tiempo_a:.6f} s | "
            f"Comparaciones: {comparaciones_a}"
        )
        print(
            f"Escenario B - Tiempo: {tiempo_b:.6f} s | "
            f"Comparaciones: {comparaciones_b}"
        )
        print(
            f"Escenario C - Tiempo: {tiempo_c:.6f} s | "
            f"Comparaciones: {comparaciones_c}"
        )

    crear_graficas(tamanos, tiempos, comparaciones)

    print("\nGraficas generadas correctamente.")
    print(" - graficas/parte3_comparaciones.png")
    print(" - graficas/parte3_tiempo.png")


if __name__ == "__main__":
    main()