
"""Experimentos de rendimiento para lista enlazada y tabla hash."""

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista de guias que no pertenecen a existentes.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in existentes and guia not in inexistentes:
            inexistentes.append(guia)

    return inexistentes


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    guias: list[int],
) -> float:
    """Mide el tiempo medio por busqueda en segundos.

    Args:
        estructura: lista enlazada o tabla hash.
        guias: guias que se van a buscar.

    Returns:
        Tiempo medio por busqueda, en segundos.
    """
    inicio = time.perf_counter()

    for guia in guias:
        resultado = estructura.buscar(guia)
        assert resultado is None

    fin = time.perf_counter()
    return (fin - inicio) / len(guias)


def construir_estructuras(
    guias: list[int], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye la lista y la tabla con las mismas guias.

    Args:
        guias: guias de diez digitos.
        m: numero de casillas de la tabla hash.

    Returns:
        La lista enlazada y la tabla hash construidas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)

    for guia in guias:
        estado = "en reparto"
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    return lista, tabla


def verificar_estructuras(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
) -> None:
    """Comprueba que ambas estructuras devuelvan el mismo estado."""
    for guia in guias[:20]:
        assert lista.buscar(guia) == tabla.buscar(guia)


def experimento_lista_vs_tabla() -> None:
    """Compara tiempos medios para diferentes cantidades de guias."""
    azar = random.Random(42)
    tamanos = [100, 500, 1000, 5000, 20000, 50000]

    tiempos_lista = []
    tiempos_tabla = []
    factores_carga = []

    for n in tamanos:
        guias = azar.sample(range(10**9, 10**10), n)

        # Un primo cercano a n / 2 mantiene alfa cerca de 2.
        m = n // 2
        while any(m % divisor == 0 for divisor in range(2, int(m**0.5) + 1)):
            m += 1

        lista, tabla = construir_estructuras(guias, m)
        verificar_estructuras(lista, tabla, guias)

        inexistentes = generar_guias_inexistentes(
            set(guias), 200, semilla=7 + n
        )

        tiempo_lista = medir_busquedas(lista, inexistentes)
        tiempo_tabla = medir_busquedas(tabla, inexistentes)

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)
        factores_carga.append(tabla.factor_carga())

        print(
            f"n={n:>5} | m={m:>5} | alfa={tabla.factor_carga():.3f} "
            f"| Lista: {tiempo_lista:.8f} s/busqueda "
            f"| Tabla: {tiempo_tabla:.8f} s/busqueda"
        )

    plt.figure(figsize=(10, 6))
    plt.plot(
        tamanos, tiempos_lista, marker="o",
        label="Lista enlazada"
    )
    plt.plot(
        tamanos, tiempos_tabla, marker="o",
        label="Tabla hash"
    )
    plt.title("Tiempo medio de busqueda frente al numero de guias")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(
        Path(__file__).parent / "graficas" / "lista_vs_tabla.png",
        dpi=150,
    )
    plt.close()


def experimento_tiempo_vs_alfa() -> None:
    """Mide el efecto del factor de carga en la tabla hash."""
    azar = random.Random(84)
    n = 20000
    guias = azar.sample(range(10**9, 10**10), n)
    inexistentes = generar_guias_inexistentes(
        set(guias), 200, semilla=91
    )

    factores_objetivo = [0.5, 1, 4, 10]
    factores_medidos = []
    tiempos_tabla = []

    for alfa_objetivo in factores_objetivo:
        m = max(1, round(n / alfa_objetivo))

        tabla = TablaHash(m)
        for guia in guias:
            tabla.insertar(guia, "en reparto")

        lista, tabla_verificacion = construir_estructuras(guias, m)

        verificar_estructuras(
            lista, tabla_verificacion, guias
        )

        tabla = tabla_verificacion

        tiempo = medir_busquedas(tabla, inexistentes)
        alfa = tabla.factor_carga()

        factores_medidos.append(alfa)
        tiempos_tabla.append(tiempo)

        print(
            f"Alfa objetivo={alfa_objetivo:g} | "
            f"Alfa real={alfa:.3f} | "
            f"Tabla: {tiempo:.8f} s/busqueda"
        )

    plt.figure(figsize=(10, 6))
    plt.plot(
        factores_medidos, tiempos_tabla, marker="o",
        label="Tabla hash"
    )
    plt.title("Tiempo medio de busqueda frente al factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(
        Path(__file__).parent / "graficas" / "tiempo_vs_alfa.png",
        dpi=150,
    )
    plt.close()


def main() -> None:
    """Ejecuta los dos experimentos y genera las graficas."""
    experimento_lista_vs_tabla()
    experimento_tiempo_vs_alfa()
    print("Experimentos finalizados. Graficas guardadas en graficas/.")


if __name__ == "__main__":
    main()
