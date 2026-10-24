# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Esneider Guisao Ospina · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `5cf44bd`

Muy buen trabajo: el código es correcto y el informe está ordenado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 22 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **89 / 100** |
| **Nota (0–5)** | **4.45** |

## 1. Corrección conceptual (16 / 20)
**Lo que hizo bien:**
- En la pregunta 4 compara con el máximo de un arreglo, explica que combinar cuesta `Θ(1)` y concluye que dividir no mejora el orden `Θ(n)`.
- En la pregunta 5 recomienda divide y vencerás y declara que su cifra es una estimación, sin usar una regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 5 el cálculo del factor tiene un error: pasar de 8000 a 1.000.000 con `n log n` da un factor cercano a 192, no 166. Por eso los 4,6 segundos deberían ser unos 5,4 segundos.
- Para fuerza bruta dice "varias horas" sin dar la cifra; con su factor de 15.625 saldrían unas 15 horas. Dar el número hace la recomendación más convincente.
- En la pregunta 3 afirma que desde 50 elementos gana divide y vencerás, pero no se alcanza a ver en la gráfica ni muestra los valores de esos tamaños en una tabla.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando los dos subproblemas y el recorrido lineal del caso cruzado.
- Aplica el método maestro (`a=2`, `b=2`, `n^(log₂2) = n`), identifica el caso 2 y llega a `Θ(n log n)`.
- Justifica el `Θ(n²)` de la fuerza bruta con la suma `1+2+...+n`.

**Lo que puede mejorar:**
- Podría decir explícitamente por qué se cumple la condición del caso 2 (`f(n)` crece igual que `n^(log_b a)`) y no solo mostrar la igualdad.

## 3. Corrección de la implementación (22 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta, no modifican la lista y `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta.
- `pruebas.py` cubre todos los casos pedidos y 20 listas aleatorias.
- `subarreglo.py` tiene type hints y docstrings en el estilo pedido.

**Lo que puede mejorar:**
- En `medicion.py`, `medir_tiempo` no tiene type hint en el parámetro `funcion` ni en el retorno de lo que ejecuta, y su docstring no sigue el estilo Google (sin Args ni Returns).
- Esa misma función recibe `valores` pero no lo usa, y guarda un `resultado` que tampoco usa.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños.
- Los valores que cita (alrededor de 0,8 s y 3,4 s para fuerza bruta en 4000 y 8000) coinciden con la gráfica.
- Calcula el factor al duplicar de 4000 a 8000 (4,24 y 2,11) y lo compara con lo esperado para `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Para el factor de `n log n` podría decir cuánto da exactamente al duplicar (un poco más de 2) y comparar con su 2,11.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada, el informe lleva el orden pedido, incluye la gráfica visible y enlaza el código de cada parte.
- Tiene instrucciones de reproducción y varios commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas soluciones coinciden con listas aleatorias y la medición corre completa y genera la gráfica.

## Para el próximo laboratorio
- Revise las cuentas de sus estimaciones antes de entregar y dé cifras concretas (horas, segundos).
- Agregue una tabla con los tiempos medidos para respaldar lo que dice de los tamaños pequeños.
- Ponga type hints y docstring completo en todas las funciones, también en las de apoyo.
