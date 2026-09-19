# Laboratorio 1 — Fundamentos, complejidad y recurrencias

**Nombre completo:** ESNEIDER GUISAO OSPINA

## 1. Instrucciones para reproducir

Para ejecutar el laboratorio se debe tener Python instalado y activar el entorno virtual del proyecto.

Desde la carpeta `lab1-fundamentos-complejidad-recurrencias`:

```bash
python parte3_casos.py
```

## Parte 1 — Analizar el algoritmo antes de comprar el servidor

- Yo creo que porque el proceso de Tamiza lleve ocho años funcionando no significa que todavía sea adecuado para la cantidad de datos que maneja actualmente. Hace algunos años podía funcionar bien porque seguramente había menos registros, pero ahora tiene que ordenar alrededor de 1,2 millones de registros todas las noches.
- Para mí, hay una diferencia entre que el algoritmo sea correcto y que cumpla con el tiempo que tiene disponible. Es correcto cuando al final los registros quedan ordenados de mayor a menor riesgo, que es lo que necesita Tamiza. Pero eso no es suficiente, porque el proceso también tiene un límite de tiempo, debe terminar entre las 2:00 a. m. y las 6:00 a. m. El problema es que ya ha ocurrido tres veces que no alcanza a terminar antes de las 6:00 a. m. y la lista queda incompleta.
- Por eso, antes de comprar un servidor con el doble de velocidad, primero revisaría el algoritmo. Un servidor más rápido podría hacer que el proceso tarde menos, pero el algoritmo seguiría haciendo el mismo tipo de trabajo. Si para ordenar 1,2 millones de registros necesita realizar demasiadas operaciones, aumentar la velocidad del servidor no solucionaría completamente el problema. Además, si la cantidad de registros sigue creciendo, la situación podría volver a presentarse.
- Un ejemplo diferente sería un sistema que tenga que procesar una campaña de 100.000 mensajes de WhatsApp. Supongamos que el sistema procesa todos los mensajes correctamente, pero tarda cuatro horas y la campaña necesita estar lista en una hora. En ese caso el sistema está dando el resultado esperado, pero no está cumpliendo con el tiempo que necesita el proceso.
- Por eso considero que primero se debería medir cuánto tarda el algoritmo con una cantidad de datos similar a la que maneja Tamiza. Con esa información se podría determinar si realmente es necesario aumentar la capacidad del servidor o si también se debe cambiar el algoritmo.

## Parte 2 — Responsabilidad ambiental y ética de la implementación

- Si yo estuviera a cargo de la parte técnica de Tamiza, no me podría quedar solo en la discusión de si el algoritmo sirve o no. Tendría que pensar en lo que pasa cada madrugada cuando se procesan esos 1,2 millones de registros de pacientes y en el impacto que puede tener el proceso.

- Algo que también tendría en cuenta es el consumo de energía. El proceso se ejecuta durante la noche y, mientras el servidor está trabajando con los datos, está consumiendo energía y recursos. Si el proceso tarda más de lo necesario y esto se repite todas las noches durante años, ese consumo adicional se va acumulando. Por eso, mejorar el algoritmo no sería solamente un tema de hacer que el programa sea más rápido, también evitaría mantener los recursos trabajando durante más tiempo del necesario.

- Lo que más me preocuparía, de todas formas, es lo que puede pasar con los pacientes. Si una noche el proceso falla, se demora demasiado o queda a la mitad, la lista puede quedar incompleta. Puede haber pacientes que no sean incluidos en las llamadas programadas y tengan que esperar más tiempo para ser contactados. En este caso, quien termina asumiendo el costo es el paciente, aunque el problema haya comenzado en el sistema.

- Y si pensamos en lo que ocurre al otro lado, está el operador del centro de contacto. Si llega a las 6:00 a. m. y encuentra una lista incompleta o que no quedó bien organizada, le tocará revisar qué pasó y tratar de trabajar con la información disponible. Esto puede quitarle tiempo y generar confusión durante la jornada. Al final, el operador termina enfrentando un problema que no fue causado por él.

- Hay otra cosa que me parece todavía más importante en este caso. La lista no se ordena solamente para tener los datos organizados. El orden indica qué pacientes se deben contactar primero de acuerdo con su nivel de riesgo. Entonces, no serviría de mucho que el proceso termine antes de las 6:00 a. m. si los registros quedaron en un orden equivocado.

- Por ejemplo, si un paciente tiene un nivel de riesgo mayor y termina después de otro que debería ser contactado más tarde, se estaría cambiando la prioridad de las llamadas. En ese punto ya no sería solamente un problema de que el sistema se demoró, porque el error podría afectar directamente la forma en que se atiende a una persona.

- Por eso, al escoger el algoritmo yo tendría que mirar más que el tiempo de ejecución. También tendría que asegurarme de que el resultado sea correcto y que la lista que recibe el centro de contacto realmente refleje las prioridades de los pacientes. Como el proceso se repite todas las noches, una decisión que parece solamente técnica puede terminar teniendo consecuencias para muchas personas.

## Parte 3 — Mejor, peor y caso promedio: demostración práctica

Código utilizado para esta parte:

- [Experimento de la Parte 3](parte3_casos.py)
- [Algoritmos de ordenamiento](algoritmos.py)
- [Generadores de datos](datos.py)

### 3.1 — Explicación

- Cuando hablamos del mejor, peor y caso promedio de un algoritmo, tenemos que comparar entradas que tengan el mismo tamaño. Por ejemplo, si tenemos una lista de n elementos, podemos mirar cómo se comporta el algoritmo con las diferentes formas en que pueden estar organizados esos mismos n elementos.

- El mejor caso sería cuando el algoritmo tiene que hacer la menor cantidad de trabajo posible con una entrada de tamaño n. En el caso de insertion sort, esto pasa cuando los datos ya están ordenados como los necesitamos. Por eso casi no tiene que hacer movimientos para organizarlos.

- El peor caso sería cuando, con esos mismos n elementos, el algoritmo tiene que hacer la mayor cantidad de trabajo. En insertion sort esto ocurre cuando los datos vienen en el orden contrario al que necesitamos, porque los elementos tienen que ir pasando uno por uno hasta encontrar su posición.

- El caso promedio sería el comportamiento que se obtiene al considerar las diferentes entradas posibles de un mismo tamaño n y sacar un promedio del trabajo que realiza el algoritmo. Para este ejercicio, el escenario que más se acerca a esta situación es el de los datos aleatorios, porque no tienen un orden definido y algunos elementos tendrán que moverse más que otros.

- Para decidir si insertion sort debería utilizarse en producción en Tamiza, yo me fijaría principalmente en el peor caso. Esto se debe a que el proceso solamente tiene cuatro horas para terminar. Si nos basamos únicamente en que normalmente los datos llegan en una situación favorable, podría presentarse una noche en la que los datos estén en un orden más complicado y el proceso no alcance a terminar antes de las 6:00 a. m.

- Antes de realizar las pruebas, mi predicción es que el escenario B será el mejor caso, porque el 98 % de los registros ya está en el orden que necesitamos y solamente hay un pequeño grupo de registros nuevos al final. El escenario C será el peor caso, porque los datos vienen completamente al contrario del orden requerido. Por último, espero que el escenario A se acerque al caso promedio, ya que los registros están organizados aleatoriamente.

- Esta es mi predicción antes de hacer las mediciones. Después de ejecutar las pruebas en python, compararé los resultados para comprobar si los tres escenarios realmente se comportan como esperaba.

### 3.2 — Resultados del experimento

- Para realizar las pruebas utilicé los tres escenarios con los tamaños de entrada de 100, 200, 400, 800, 1600, 3200 y 6400 registros. El tiempo se midió solamente durante la ejecución de `insertion_sort`, utilizando `time.perf_counter()`. Los datos se generaron antes de iniciar el cronómetro para no incluir ese tiempo en la medición.

- Los resultados muestran una diferencia clara entre los tres escenarios. En todos los tamaños probados, el escenario B fue el que necesitó menos comparaciones y menos tiempo. Por ejemplo, con 6400 registros realizó 414738 comparaciones y tardó aproximadamente 0.138 segundos.

- El escenario C fue el que presentó el mayor número de comparaciones y el mayor tiempo de ejecución. Con 6400 registros realizó 20476800 comparaciones y tardó aproximadamente 6.587 segundos. Esto coincide con lo esperado para el caso en el que los datos llegan completamente en el orden contrario al que necesita el algoritmo.

- El escenario A quedó entre los otros dos. Para 6400 registros realizó 10276753 comparaciones y tardó aproximadamente 3.884 segundos. Por su comportamiento con datos aleatorios, es el escenario que se aproxima al caso promedio.

- Por lo tanto, los resultados de la prueba coinciden con mi predicción de la sección 3.1: el escenario B corresponde al mejor caso, el escenario C al peor caso y el escenario A se aproxima al caso promedio.

### Comparaciones por escenario

![Comparaciones de insertion sort por escenario](graficas/parte3_comparaciones.png)

### Tiempo de ejecución por escenario

![Tiempo de ejecución de insertion sort por escenario](graficas/parte3_tiempo.png)

# Parte 4 — Complejidad de merge sort e insertion sort: cálculo y validación

### 4.1 — Cálculo teórico

#### Complejidad de merge sort

Para merge sort, el algoritmo divide la lista en dos partes aproximadamente iguales y aplica el mismo procedimiento a cada una. Después de ordenar las dos partes, las combina en una sola lista ordenada.

Por esta razón, la recurrencia es:

\[
T(n) = 2T(n/2) + \Theta(n)
\]

Cada término representa una parte del trabajo:

- `2T(n/2)`: representa el costo de resolver los dos subproblemas, cada uno con aproximadamente la mitad de los elementos.
- `\Theta(n)`: corresponde al proceso de combinar las dos partes ordenadas. Para hacerlo hay que recorrer los elementos de ambas partes y construir nuevamente la lista ordenada.

#### Cálculo manual de insertion sort

Para realizar el cálculo manual voy a utilizar la misma implementación de `insertion_sort` utilizada en el experimento:

```python
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
```

#### Mejor caso

El mejor caso ocurre cuando los datos ya están ordenados en el mismo sentido en que los necesita Tamiza, es decir, de mayor riesgo a menor riesgo.

En este caso, el algoritmo entra una sola vez al ciclo `while` para cada posición. La comparación realizada por el `if` permite detener inmediatamente el proceso porque los elementos ya están en el orden correcto.

| Línea | Veces que se ejecuta |
| --- | ---: |
| `lista = datos.copy()` | 1 |
| `comparaciones = 0` | 1 |
| `for i in range(1, len(lista))` | `n - 1` |
| `j = i` | `n - 1` |
| `while j > 0` | `n - 1` |
| `comparaciones += 1` | `n - 1` |
| `if lista[j - 1] >= lista[j]` | `n - 1` |
| `break` | `n - 1` |
| Intercambio | 0 |
| `j -= 1` | 0 |
| `return lista, comparaciones` | 1 |

En el mejor caso, el ciclo externo se ejecuta `n - 1` veces y en cada iteración se realiza una sola comparación entre elementos. Por lo tanto, el crecimiento del trabajo es proporcional a `n`.

La complejidad temporal del mejor caso es:

\[
\boxed{T(n)=\Theta(n)}
\]

Aunque en la tabla `lista = datos.copy()` aparece como una sola ejecución de la instrucción, la copia internamente debe recorrer los elementos de la lista. Esto también tiene un costo lineal. Por lo tanto, el resultado general del mejor caso sigue siendo `\Theta(n)`.

##### Peor caso

El peor caso ocurre cuando los datos están completamente en el orden contrario al que necesita Tamiza. Por ejemplo, para una lista de 10 elementos:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

En este caso, los elementos deben desplazarse prácticamente hasta el extremo contrario de la lista para quedar ordenados de mayor a menor.

La cantidad de veces que se ejecutan las instrucciones que dependen del ciclo `while` aumenta en cada iteración del ciclo externo:

| Línea | Veces que se ejecuta |
| --- | ---: |
| `lista = datos.copy()` | 1 |
| `comparaciones = 0` | 1 |
| `for i in range(1, len(lista))` | `n - 1` |
| `j = i` | `n - 1` |
| `while j > 0` | \(\frac{n(n-1)}{2}\) |
| `comparaciones += 1` | \(\frac{n(n-1)}{2}\) |
| `if lista[j - 1] >= lista[j]` | \(\frac{n(n-1)}{2}\) |
| Intercambio | \(\frac{n(n-1)}{2}\) |
| `j -= 1` | \(\frac{n(n-1)}{2}\) |
| `break` | 0 |
| `return lista, comparaciones` | 1 |

Para entender de dónde sale esta cantidad, se puede observar el número de comparaciones realizadas en cada iteración:

```text
i = 1  → 1 comparación
i = 2  → 2 comparaciones
i = 3  → 3 comparaciones
...
i = n-1 → n-1 comparaciones
```

Por lo tanto, la cantidad total de comparaciones es:

\[
1+2+3+\cdots +(n-1)
\]

La suma de los primeros `n - 1` números enteros positivos es:

\[
\frac{n(n-1)}{2}
\]

Por ejemplo, si:

\[
n=5
\]

entonces:

\[
1+2+3+4=10
\]

y utilizando la fórmula:

\[
\frac{5(5-1)}{2}
=
\frac{5(4)}{2}
=
10
\]

Por lo tanto, el número de comparaciones en el peor caso es:

\[
\frac{n(n-1)}{2}
\]

Desarrollando la expresión:

\[
\frac{n(n-1)}{2}
=
\frac{n^2-n}{2}
\]

o también:

\[
\frac{1}{2}n^2-\frac{1}{2}n
\]

El término que domina el crecimiento cuando `n` aumenta es:

\[
n^2
\]

Por lo tanto, la complejidad temporal del peor caso es:

\[
\boxed{T(n)=\Theta(n^2)}
\]

##### Caso promedio

El caso promedio representa el comportamiento del algoritmo cuando se consideran diferentes arreglos posibles de los datos para un mismo tamaño `n`. En el experimento de Tamiza, este comportamiento se aproxima utilizando datos generados aleatoriamente.

En una entrada aleatoria, algunos elementos pueden encontrarse cerca de la posición que les corresponde, mientras que otros pueden necesitar varios desplazamientos. Por esta razón, el trabajo realizado se encuentra entre el comportamiento del mejor y del peor caso.

En promedio, un elemento debe desplazarse aproximadamente una cantidad intermedia de las posiciones que podría recorrer. Por esta razón, el número de desplazamientos y comparaciones crece proporcionalmente al número de pares de elementos que pueden encontrarse en un orden que requiera desplazamiento.

La suma:

\[
1+2+3+\cdots +(n-1)
\]

representa el crecimiento máximo utilizado anteriormente para el peor caso. En el caso promedio no se debe interpretar esta suma como el número exacto de comparaciones que siempre se realizan, sino como una referencia para observar el orden de crecimiento. En una entrada aleatoria se realizan, en promedio, menos desplazamientos que en el peor caso, pero el crecimiento continúa siendo cuadrático.

La suma completa del peor caso es:

\[
\frac{n(n-1)}{2}
=
\frac{n^2-n}{2}
\]

y su término dominante es `n²`. En el caso promedio, aunque la cantidad exacta de operaciones sea menor que en el peor caso, sigue creciendo proporcionalmente a `n²`.

Por lo tanto, la complejidad temporal del caso promedio es:

\[
\boxed{T(n)=\Theta(n^2)}
\]

Los datos aleatorios utilizados en el experimento permiten aproximar este comportamiento, pero una ejecución concreta no representa por sí sola todos los posibles arreglos de entrada para un determinado tamaño `n`.

#### Tabla de complejidades esperadas

| Algoritmo | Mejor caso | Caso promedio | Peor caso |
| --- | --- | --- | --- |
| Insertion sort | \(\Theta(n)\) | \(\Theta(n^2)\) | \(\Theta(n^2)\) |
| Merge sort | \(\Theta(n\log n)\) | \(\Theta(n\log n)\) | \(\Theta(n\log n)\) |

La diferencia principal entre los dos algoritmos está en la forma en que aumenta el trabajo cuando crece el número de registros.

Para `insertion sort`, el mejor caso es lineal porque cuando los datos ya están ordenados solamente necesita realizar una comparación por posición. Sin embargo, cuando los elementos necesitan muchos desplazamientos, el número de operaciones crece de forma cuadrática.

En `merge sort`, el proceso de división y combinación mantiene una estructura similar independientemente de cómo estén organizados inicialmente los datos. Por esta razón, su complejidad se mantiene en `\Theta(n log n)` para los tres casos.

#### Resolución mediante árbol de recursión

Para resolver la recurrencia de `merge sort` voy a utilizar el método del árbol de recursión.

Partimos de la recurrencia:

\[
T(n)=2T(n/2)+cn
\]

donde `cn` representa el costo de combinar las dos partes ordenadas.

La primera división genera dos problemas de tamaño `n/2`:

```text
                         T(n)
                       /      \
                  T(n/2)      T(n/2)
                  /    \      /    \
             T(n/4) T(n/4) T(n/4) T(n/4)
                 ...
```

El costo de combinación en cada nivel puede analizarse de la siguiente manera.

En el nivel 0 se encuentra el problema original:

\[
cn
\]

En el nivel 1 existen dos subproblemas de tamaño `n/2`. El costo total de ese nivel es:

\[
2\left(c\frac{n}{2}\right)
\]

Simplificando:

\[
2\left(c\frac{n}{2}\right)=cn
\]

En el nivel 2 existen cuatro subproblemas de tamaño `n/4`:

\[
4\left(c\frac{n}{4}\right)=cn
\]

Por lo tanto, en cada nivel el costo total de combinación sigue siendo:

\[
cn
\]

En un nivel general `k`, existen:

\[
2^k
\]

subproblemas y cada uno tiene tamaño:

\[
\frac{n}{2^k}
\]

El costo total del nivel `k` es:

\[
2^k\left(c\frac{n}{2^k}\right)
\]

Simplificando:

\[
2^k\left(c\frac{n}{2^k}\right)=cn
\]

Por lo tanto, cada nivel del árbol aporta un costo de `cn`.

El proceso de división termina cuando cada subproblema tiene tamaño 1. Para encontrar ese nivel se plantea:

\[
\frac{n}{2^k}=1
\]

Multiplicando por `2^k`:

\[
n=2^k
\]

Aplicando logaritmo en base 2:

\[
k=\log_2 n
\]

Esto significa que el proceso de división llega al caso base después de `log₂(n)` niveles de división.

Como cada nivel tiene un costo de:

\[
cn
\]

y existen aproximadamente:

\[
\log_2 n
\]

niveles de combinación, el costo total de esas combinaciones es:

\[
cn\log_2 n
\]

Además, en el último nivel existen aproximadamente `n` subproblemas de tamaño 1, por lo que el costo de las hojas es:

\[
\Theta(n)
\]

Por lo tanto, la recurrencia completa queda:

\[
T(n)=cn\log_2 n+\Theta(n)
\]

El término dominante cuando `n` aumenta es:

\[
n\log_2 n
\]

Por lo tanto:

\[
\boxed{T(n)=\Theta(n\log n)}
\]

Así, la complejidad temporal de `merge sort` es:

\[
\boxed{\Theta(n\log n)}
\]
