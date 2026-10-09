
"""Pruebas para los algoritmos de subarreglo maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def verificar_caso(valores: list[float]) -> None:
    """Comprueba que ambos algoritmos encuentren la misma suma."""
    resultado_fuerza = subarreglo_fuerza_bruta(valores)
    resultado_divide = subarreglo_maximo(
        valores, 0, len(valores) - 1
    )

    assert resultado_fuerza[2] == resultado_divide[2], (
        f"Resultados diferentes para {valores}: "
        f"{resultado_fuerza} != {resultado_divide}"
    )


def main() -> None:
    """Ejecuta los casos obligatorios y las pruebas aleatorias."""
    ejemplo = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(ejemplo)[2] == 17
    assert subarreglo_maximo(ejemplo, 0, len(ejemplo) - 1)[2] == 17
    verificar_caso(ejemplo)

    verificar_caso([7])
    verificar_caso([-8, -3, -10])
    verificar_caso([2, 4, 1, 5])
    verificar_caso([-5, 10, -2, 3, -20])
    assert subarreglo_maximo(
        [-5, 10, -2, 3, -20], 0, 4
    )[2] == 11

    generador = random.Random(42)

    for _ in range(20):
        cantidad = generador.randint(1, 30)
        valores = [
            generador.randint(-20, 20)
            for _ in range(cantidad)
        ]
        verificar_caso(valores)

    print("Todas las pruebas fueron superadas.")
    print("Casos especiales y 20 pruebas aleatorias verificados.")


if __name__ == "__main__":
    main()
