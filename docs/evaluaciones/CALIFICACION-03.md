# Retroalimentación — Lab 03 Estructuras de datos

**Estudiante:** Esneider Guisao Ospina · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `a056396`

Buen trabajo: entregó todo completo, el código funciona y su informe se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **96 / 100** |
| **Nota (0–5)** | **4.80** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque sobren casillas, usando el ejemplo de las guías 10, 24 y 17 con m = 7.
- Justifica por qué la tabla hash no sirve para rangos y recomienda un árbol equilibrado para ellos.
- Estima la altura del árbol degenerado (unas 400.000) frente a la del equilibrado (cerca de 19) y declara sus estimaciones a 5.000.000 de envíos como estimaciones.

**Lo que puede mejorar (y cómo corregirlo):**
- La comparación entre encadenamiento y direccionamiento abierto es corta: no deja claro qué pasa con el costo cuando la tabla se llena en el direccionamiento abierto.
  → *Cómo corregirlo:* piense qué ocurre con el espacio disponible y con el número de intentos al buscar cuando α se acerca a 1, y escríbalo para cada método.
- En el árbol degenerado da la altura, pero no cuenta cuántas comparaciones costaría insertar todas las guías una a una.
  → *Cómo corregirlo:* piense cuántas comparaciones necesita la guía número k al insertarse en una cadena y súmelas para las 400.000.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista para una guía inexistente y el `Θ(1 + α)` de la tabla.
- Nombra el supuesto de distribución uniforme y explica que, si todo cae en una casilla, la tabla se degrada a `Θ(n)`.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las dos estructuras buscan bien, tanto guías que existen como las que no; la colisión con m = 7 y `factor_carga` (3/7) funcionan.
- La tabla reutiliza `ListaEnlazada` sin `dict`, `set` ni `hash()`, y `buscar` usa un ciclo `while`.
- Las pruebas comparan lista y tabla en 20 colecciones aleatorias y todas pasan.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de `n` con las dos curvas en los mismos ejes y la segunda cuatro valores de α.
- Calcula el factor de crecimiento de la lista (cerca de 4,12 al pasar de 5.000 a 20.000) y lo contrasta con `Θ(n)`; los valores del informe coinciden con lo que muestran las gráficas.

**Lo que puede mejorar (y cómo corregirlo):**
- Para la segunda gráfica no calcula cuánto se multiplicó el tiempo al crecer α; solo dice que la tendencia "concuerda".
  → *Cómo corregirlo:* tome dos valores de α, divida los tiempos medidos y compare ese cociente con lo que predice `Θ(1 + α)`.
- La estimación a 5.000.000 usa una proporción simple para la lista sin explicar con más detalle la forma de la curva.
  → *Cómo corregirlo:* apóyese en el factor de crecimiento que calculó en la pregunta 2 para justificar por qué la curva es una recta.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada, con todos los archivos del entregable.
- El `README.md` tiene su nombre, instrucciones de reproducción, el orden pedido, las gráficas visibles y enlaces al código de cada parte.
- Hay cuatro commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, y `medicion.py` corre sin errores y genera las dos gráficas.
