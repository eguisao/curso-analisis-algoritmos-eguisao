
"""Pruebas de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_casos_basicos() -> None:
    """Verifica busquedas exitosas e infructuosas."""
    lista = ListaEnlazada()
    tabla = TablaHash(7)

    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")

    tabla.insertar(1000000010, "en bodega")
    tabla.insertar(1000000024, "en reparto")

    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(1000000024) == "en reparto"
    assert lista.buscar(9999999999) is None

    assert tabla.buscar(1000000010) == "en bodega"
    assert tabla.buscar(1000000024) == "en reparto"
    assert tabla.buscar(9999999999) is None


def probar_colisiones() -> None:
    """Verifica la colision de tres guias en la misma casilla."""
    tabla = TablaHash(7)

    tabla.insertar(10, "en bodega")
    tabla.insertar(24, "en reparto")
    tabla.insertar(17, "entregado")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3

    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en reparto"
    assert tabla.buscar(17) == "entregado"

    assert tabla.casillas[3].tamano == 3
    assert tabla.tamano == 3
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias() -> None:
    """Compara ambas estructuras en veinte colecciones aleatorias."""
    azar = random.Random(42)

    for _ in range(20):
        cantidad = azar.randint(1, 100)
        guias = azar.sample(range(10**9, 10**10), cantidad)

        lista = ListaEnlazada()
        tabla = TablaHash(101)
        estados = []

        for guia in guias:
            estado = azar.choice(
                ["en bodega", "en reparto", "entregado"]
            )
            estados.append((guia, estado))
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia, estado in estados:
            assert lista.buscar(guia) == estado
            assert tabla.buscar(guia) == estado

        for _ in range(20):
            inexistente = azar.randint(10**9, 10**10 - 1)

            while inexistente in guias:
                inexistente = azar.randint(10**9, 10**10 - 1)

            assert lista.buscar(inexistente) is None
            assert tabla.buscar(inexistente) is None


def main() -> None:
    """Ejecuta todas las pruebas del laboratorio."""
    probar_casos_basicos()
    probar_colisiones()
    probar_colecciones_aleatorias()

    print("Pruebas basicas superadas.")
    print("Colisiones y factor de carga verificados.")
    print("20 colecciones aleatorias verificadas.")
    print("Todas las pruebas fueron superadas.")


if __name__ == "__main__":
    main()
