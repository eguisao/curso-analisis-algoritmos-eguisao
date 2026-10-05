# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Esneider Guisao Ospina · **Laboratorio:** Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `2b95f4d`

Muy buen trabajo: el laboratorio está completo y los resultados son sólidos.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 20 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **80 / 100** |
| **Nota (0–5)** | **4.00** |

## 1. Corrección conceptual (20 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue a tiempo, y nombra la ventana de cuatro horas como lo que se incumple.
- En la Parte 2 identifica dos perjuicios (el paciente y el operador del centro de contacto), dice quién asume el costo y explica por qué el orden de la lista es una obligación adicional.

**Lo que puede mejorar:**
- Explique con más fuerza por qué un servidor del doble de rápido no basta: el trabajo del algoritmo crece mucho más rápido que la velocidad que se gana.
- El segundo ejemplo (mensajes de WhatsApp) es correcto pero muy breve; le faltó detallar mejor qué se procesa y por qué es inviable.
- En la dimensión ambiental no relaciona el tiempo con energía de forma concreta (por ejemplo, horas de servidor por año).

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define los tres casos sobre entradas del mismo tamaño n, justifica que usaría el peor caso y deja escrita su predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con árbol de recursión, nivel por nivel, hasta `Θ(n log n)`.
- El cálculo línea a línea de insertion sort (mejor y peor caso) está claro, con la tabla de complejidades.

**Lo que puede mejorar:**
- La explicación del caso promedio de insertion sort quedó vaga; falta mostrar por qué en promedio se hace cerca de la mitad del trabajo del peor caso.
- El árbol de recursión está dibujado solo con los primeros niveles y sin el costo escrito al lado de cada nivel.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- Ambos algoritmos ordenan bien, no cambian la lista original, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`. Merge sort tiene su propia mezcla recursiva.
- Los generadores producen valores distintos, del tamaño pedido y con semilla reproducible.

**Lo que puede mejorar:**
- Hay varios detalles de estilo: líneas en blanco con espacios, falta de dos líneas en blanco entre funciones y archivos sin salto de línea al final.
- Los docstrings no dejan línea en blanco antes de `Returns` y la función `medir_tiempo` no tiene tipo en el parámetro `algoritmo`.
- `generar_casi_ordenado` falla si se le pide una lista vacía (n = 0).

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, leyenda y curvas en los mismos ejes.
- La Parte 3.2 identifica con datos el mejor caso (B), el peor (C) y el promedio (A), y lo contrasta con su predicción.
- El concepto técnico (4.3) recomienda merge sort, estima 38 horas para insertion sort y unos 11 segundos para merge sort, declarando que son estimaciones, y responde a la propuesta del servidor con un dato medido.

**Lo que puede mejorar:**
- La sección 4.2 termina sin una conclusión clara: falta decir cuál algoritmo es mejor para Tamiza, describir la curva de merge sort y contrastar con las complejidades de 4.1.
- No comenta que con tamaños pequeños las curvas casi se juntan ni lo explica.
- Cada medición se hizo una sola vez; repetirla y promediar daría curvas más confiables.
- En 4.3 no discute la estabilidad ni el costo de mantenimiento (sí la memoria y el riesgo del escenario B).

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta y los archivos siguen exactamente la estructura pedida; las gráficas se ven en el informe y cada parte enlaza su código.
- Hay varios commits descriptivos que muestran el avance.

**Lo que puede mejorar:**
- Las instrucciones para reproducir tienen una frase cortada y solo sirven para Windows; agregue también cómo hacerlo en Linux/macOS.
- Los encabezados de la Parte 4 cambian de nivel sin orden claro.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien en mis pruebas, ambos scripts corren sin errores y generan las tres gráficas.

## Para el próximo laboratorio
- Cierre cada análisis de gráfica con una conclusión explícita y compárela con la teoría.
- Repita las mediciones varias veces y grafique el promedio.
- Revise el estilo del código (PEP 8) antes de entregar y ponga tipos en todos los parámetros.
- Dé números concretos en los argumentos (por ejemplo, consumo de energía estimado).
