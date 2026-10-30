# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Esneider Guisao Ospina · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `b5c90dd`

Muy buen trabajo: el informe es completo, ordenado y se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **88 / 100** |
| **Nota (0–5)** | **4.40** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue con claridad que el orden correcto no basta: el proceso también debe terminar en la ventana de cuatro horas, y nombra los tres cierres incompletos como evidencia.
- Explica que un servidor el doble de rápido no cambia el crecimiento cuadrático del trabajo.
- En la Parte 2 identifica dos perjuicios concretos (el paciente y el operador del centro de contacto) y dice quién asume el costo en cada uno.
- Discute bien que el orden de la lista decide a quién se llama primero, y que por eso el resultado debe ser correcto además de rápido.

**Lo que puede mejorar (y cómo corregirlo):**
- El segundo ejemplo (campaña de 100.000 mensajes) no deja claro qué parte del proceso se vuelve inviable ni por qué el algoritmo es el culpable del tiempo.
  → *Cómo corregirlo:* indique qué operación concreta crece con la cantidad de datos y qué recurso o plazo se incumple al crecer.
- La relación entre tiempo de ejecución y energía se queda en lo general.
  → *Cómo corregirlo:* conecte el tiempo diario del proceso con su repetición cada madrugada durante años, usando un orden de magnitud que usted justifique.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio sobre entradas del mismo tamaño n, justifica usar el peor caso para decidir la entrada a producción y deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve paso a paso con el árbol de recursión (costo por nivel, número de niveles y costo total).
- Calcula insertion sort línea a línea para el mejor y el peor caso, y presenta la tabla de complejidades.

**Lo que puede mejorar (y cómo corregirlo):**
- El caso promedio de insertion sort se justifica con palabras, sin un conteo propio.
  → *Cómo corregirlo:* piense cuántos pares de elementos están fuera de orden en promedio en una lista aleatoria y cuántos desplazamientos implica eso.
- En la tabla del peor caso, la línea del `while` no cuenta la comprobación que termina cada ciclo.
  → *Cómo corregirlo:* revise cuántas veces se evalúa esa condición por cada iteración del ciclo externo.

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien listas de varios tamaños, no alteran la lista recibida y cuentan solo comparaciones entre elementos.
- `merge_sort` tiene su propia mezcla recursiva y no se usa `sorted()` ni `sort()`.
- Los generadores producen listas con valores distintos, del tamaño pedido y con semilla reproducible. El escenario B queda con el 98 % ordenado y el 2 % al final.
- Hay *type hints* y *docstrings* con `Args` y `Returns`.

**Lo que puede mejorar (y cómo corregirlo):**
- Las funciones `main` de `parte3_casos.py` y `parte4_complejidad.py` tienen *docstring* de una línea, sin las secciones del estilo Google.
  → *Cómo corregirlo:* agregue la sección `Returns:` (por ejemplo, "Ninguno.") para que todas las funciones sigan el mismo formato.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con evidencia el mejor caso (B), el peor (C) y el promedio (A), y lo contrasta con su predicción.
- Concluye que `merge_sort` es el mejor para Tamiza describiendo lo que hace cada curva, y explica por qué en tamaños pequeños las curvas se parecen.
- El concepto técnico recomienda una sola implementación, extrapola a 1.200.000 registros declarándolo como estimación, responde a la compra del servidor con un dato medido y discute memoria y mantenimiento.

**Lo que puede mejorar (y cómo corregirlo):**
- La tabla de la Parte 4.2 dice que con n = 6400 `insertion_sort` tardó 3.90 s y `merge_sort` 0.036 s, pero la gráfica `parte4_tiempo.png` muestra cerca de 3.4 s y cerca de 0.03 s. Además, la Parte 4.3 usa los valores de la gráfica, así que el informe se contradice.
  → *Cómo corregirlo:* regenere la tabla y la gráfica con la misma corrida y use esos mismos números en 4.2 y 4.3.
- No explica por qué el escenario B, siendo casi ordenado, aún hace cientos de miles de comparaciones con n = 6400.
  → *Cómo corregirlo:* piense qué le pasa a cada uno de los registros nuevos del final cuando entra al tramo ya ordenado.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Sigue la estructura de carpetas y los nombres de archivo del entregable. Hay informe por partes, gráficas incrustadas con ruta relativa que resuelve, instrucciones de reproducción y enlaces al código en cada parte práctica.
- Hay más de cinco commits descriptivos sobre el laboratorio.

**Lo que puede mejorar (y cómo corregirlo):**
- En la raíz del repositorio hay un archivo vacío llamado `git` que no pertenece al entregable.
  → *Cómo corregirlo:* elimínelo con `git rm git`.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan correctamente, los generadores producen los lotes pedidos y los scripts corren hasta el final generando las gráficas.
