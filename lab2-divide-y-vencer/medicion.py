
"""Mide y grafica los tiempos de ambos algoritmos."""

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_tiempo(funcion, valores: list[int]) -> float:
    """Mide la mediana de tres ejecuciones de una funcion."""
    tiempos = []

    for _ in range(3):
        inicio = time.perf_counter()
        resultado = funcion()
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return statistics.median(tiempos)


def main() -> None:
    """Mide los algoritmos y guarda la grafica comparativa."""
    tamanos = [10, 50, 100, 500, 1000, 4000, 8000]
    generador = random.Random(42)

    tiempos_fuerza = []
    tiempos_divide = []

    for n in tamanos:
        valores = [
            generador.randint(-100, 100)
            for _ in range(n)
        ]

        resultado_fuerza = subarreglo_fuerza_bruta(valores)
        resultado_divide = subarreglo_maximo(
            valores, 0, len(valores) - 1
        )

        assert resultado_fuerza[2] == resultado_divide[2], (
            f"Las sumas no coinciden para n={n}"
        )

        tiempo_fuerza = medir_tiempo(
            lambda: subarreglo_fuerza_bruta(valores), valores
        )
        tiempo_divide = medir_tiempo(
            lambda: subarreglo_maximo(
                valores, 0, len(valores) - 1
            ),
            valores,
        )

        tiempos_fuerza.append(tiempo_fuerza)
        tiempos_divide.append(tiempo_divide)

        print(
            f"n={n:>5} | Fuerza bruta: {tiempo_fuerza:.6f} s "
            f"| Divide y venceras: {tiempo_divide:.6f} s"
        )

    carpeta_graficas = Path(__file__).parent / "graficas"
    carpeta_graficas.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(
        tamanos, tiempos_fuerza, marker="o",
        label="Fuerza bruta O(n²)"
    )
    plt.plot(
        tamanos, tiempos_divide, marker="o",
        label="Divide y vencerás O(n log n)"
    )

    plt.title("Tiempo de ejecución según tamaño del arreglo")
    plt.xlabel("Tamaño del arreglo (n elementos)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    ruta_grafica = carpeta_graficas / "tiempo_vs_n.png"
    plt.savefig(ruta_grafica, dpi=150)
    plt.close()

    print(f"\nGrafica guardada en: {ruta_grafica}")


if __name__ == "__main__":
    main()
