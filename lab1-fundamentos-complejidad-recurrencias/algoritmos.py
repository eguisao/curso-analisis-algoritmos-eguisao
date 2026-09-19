"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 
 
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0

    for i in range(1, len(lista)):
        j = i

        while j > 0:
            comparaciones += 1

            if lista[j - 1] >= lista[j]:
                break

            lista[j - 1], lista[j] = lista[j], lista[j - 1]
            j -= 1

    return lista, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()

    if len(lista) <= 1:
        return lista, 0

    mitad = len(lista) // 2

    izquierda, comparaciones_izquierda = merge_sort(lista[:mitad])
    derecha, comparaciones_derecha = merge_sort(lista[mitad:])

    resultado = []
    i = 0
    j = 0
    comparaciones = comparaciones_izquierda + comparaciones_derecha

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones