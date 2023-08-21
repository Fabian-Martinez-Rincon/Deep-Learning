<style>
        body {
            background-color: white;
            color: black;
            transition: background-color 0.5s, color 0.5s; /* Esto añade una suave transición al cambiar los colores */
        }

        body.dark-mode {
            background-color: #1E2021;
            color: white;
            
        }
      body.dark-mode strong ,body.dark-mode h1, body.dark-mode h2, body.dark-mode h3, body.dark-mode h4, body.dark-mode h5, body.dark-mode h6{
            color: white;
        }
      body.dark-mode blockquote{
         filter: invert(1);
      }
        button{
         font-family: 'Roboto', sans-serif;
         font-size: 14px;
         font-weight: bolt;
         background: #1e90FF;
         width: 100px;
         padding: 7px;
         text-align: center;
         text-decoration: none;
         text-transform: uppercase;
         color: #fff;
         border-radius: 6px;
         cursor: pointer;
         box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }
    </style>
<script>
    function toggleDarkMode() {
        const body = document.body;
        if (body.classList.contains('dark-mode')) {
            body.classList.remove('dark-mode');
        } else {
            body.classList.add('dark-mode');
        }
    }
</script>

<div align='center'><h2> 🤖 Deep Learning</h2></div>


<div align='center'>
<button onclick="toggleDarkMode()">Oscuro</button>
<a href='https://github.com/Fabian-Martinez-Rincon/Deep-Learning/tree/main'><button style='background: #ecec00'> ⭐ </button></a>
<a href='https://github.com/Fabian-Martinez-Rincon'><button style='background: #000000'>Github</button></a>

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5
' height="10" width="100%"></div>


- [Practica](/index.html)
- [Polars (alternativa a pandas)](https://www.youtube.com/watch?v=CtkMzCIXOWk)

## 01a_Introduccion

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

"Discreta" y "continua" son términos que se refieren a dos tipos diferentes de variables o conjuntos de datos. Vamos a definir y diferenciar cada uno.

#### Discreta

Una variable discreta es aquella que puede tomar un número finito o un conjunto contable infinito de valores. Estos valores suelen ser resultados específicos y separados, y no pueden ser subdivididos de manera significativa.

<table>
<tr><td>Ejemplos</td><td>Caracteristicas</td></tr>
<tr><td>

- El número de estudiantes en una clase (puedes tener 20, 21, 22 estudiantes, pero no 20.5 estudiantes).
- El número de lanzamientos de una moneda hasta obtener cara.
- La cantidad de libros en una estantería.
</td><td>

- Los valores que puede tomar son contables.
- No tiene sentido hablar de valores "entre" dos valores discretos adyacentes. Por ejemplo, entre 3 y 4 estudiantes, no hay ningún valor válido.
</td></tr>
</table>

#### Continua

Una variable continua es aquella que puede tomar cualquier valor dentro de un rango específico. Estos valores pueden ser subdivididos infinitamente, y hay un número infinito de valores posibles entre dos valores cualesquiera.


<table>
<tr><td>Ejemplos</td><td>Caracteristicas</td></tr>
<tr><td>

- La altura de una persona (puede ser 1.75 metros, 1.751 metros, 1.7512 metros, etc.).
- El tiempo que tarda un corredor en completar una maratón.
- La temperatura de una habitación.
</td><td>

- Los valores que puede tomar son incontables dentro de un rango.
- Siempre hay valores intermedios entre dos valores cualesquiera, sin importar cuán cercanos estén.
</td></tr>
</table>




<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

### Aprendizaje Supervisado

> Video de Regresión Lineal Dot Csv [Link](https://www.youtube.com/watch?v=k964_uNn3l0)

El aprendizaje supervisado es un tipo de aprendizaje automático donde se proporciona un conjunto de datos de entrada junto con las respuestas correctas (etiquetas) con el objetivo de entrenar un modelo que pueda hacer predicciones precisas sobre datos no vistos previamente.

#### Clasificación


En problemas de clasificación, el objetivo es predecir una etiqueta categórica o discreta para una entrada dada. Es decir, se clasifica la entrada en una de varias categorías o clases.

<table><td>


- Determinar si un correo electrónico es spam o no spam.
- Clasificar una imagen en categorías como "gato", "perro" o "pájaro".
- Diagnosticar si un paciente tiene una enfermedad específica o no.

</td><td>



<img src='https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/37c37b79-0381-4afb-b898-d04a698eec25' width='400px'>
</td></table>



#### Regresión

En problemas de regresión, el objetivo es predecir un valor continuo para una entrada dada. A diferencia de la clasificación, donde se predice una etiqueta de clase, en la regresión se predice una cantidad numérica. (Rojo: Los datos reales, Azul: Datos previstos)

<table><td>

- Predecir el precio de una casa basado en sus características (tamaño, ubicación, número de habitaciones, etc.).
- Estimar la temperatura de una ciudad en un día futuro.
- Prever las ventas de un producto en los próximos meses.



</td><td>



<img src='https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/497e06a4-6da7-4950-becd-2483bb48f0aa' width='800px'>
</td></table>


#### Diferencias

<table>
<tr><td>Clasificación</td><td>Regresión</td></tr>
<tr><td>

- Las respuestas (etiquetas) son discretas y pertenecen a un conjunto finito.
- No hay orden inherente entre las clases. Por ejemplo, en una clasificación de animales, "gato" no es mayor ni menor que "perro".
</td><td>

- Las respuestas son valores numéricos continuos.
- Hay un orden inherente en las respuestas. Por ejemplo, un precio de casa de \$300,000 es mayor que uno de \$200,000.
</td></tr>
</table>

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

## Red Neuronal Artificial


> Preguntar sobre los pesos y la funcion de activación
> Video de [Dot csv Parte 1](https://www.youtube.com/watch?v=MRIv2IwFTPg)
> Video de [Dot csv Parte 2](https://www.youtube.com/watch?v=uwbHOpp9xkc)
> Video de [Dot csv Parte 2.5](https://www.youtube.com/watch?v=FVozZVUNOOA)
> Video de [Dot csv Parte 3](https://www.youtube.com/watch?v=eNIqz_noix8)
> Video de [Dot csv Parte 3.5](https://www.youtube.com/watch?v=M5QHwkkHgAA&t=1s)


<table><td>

Una Red Neuronal Artificial (RNA) es un modelo de aprendizaje automático inspirado en la estructura y funcionamiento de las redes neuronales biológicas presentes en el cerebro humano. Estas redes están compuestas por unidades llamadas "neuronas" que están interconectadas y trabajan juntas para producir una salida basada en una serie de entradas.
</td><td>

<img src='https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/ff926135-69ca-4696-8175-75d1ce5980dd' width='3000'>
</td></table>

#### Componentes básicos de una RNA

1. **Neuronas**: Son las unidades básicas de procesamiento en una red neuronal. Cada neurona recibe una serie de entradas, las procesa y produce una salida.

2. **Pesos**: Son valores asociados a las conexiones entre neuronas. Determinan la importancia relativa de cada entrada a una neurona.

3. **Función de Activación**: Es una función matemática aplicada a la salida de una neurona. Introduce no linealidades en la red, permitiendo que la RNA aprenda relaciones más complejas.

4. **Bias**: Es un término adicional que se añade antes de la función de activación para permitir que la neurona se ajuste mejor a los datos.

#### Estructura de una RNA

1. **Capa de Entrada**: Es la primera capa de la red y recibe los datos de entrada.

2. **Capas Ocultas**: Son las capas intermedias entre la entrada y la salida. Pueden ser una o varias, dependiendo de la profundidad de la red.

3. **Capa de Salida**: Es la última capa de la red y produce la salida final, que puede ser una clasificación, una regresión, entre otros.

#### Funcionamiento

1. **Feedforward (Propagación hacia adelante)**: Los datos de entrada se pasan a través de la red, desde la capa de entrada hasta la capa de salida. En cada neurona, se calcula una suma ponderada de las entradas, se añade el bias y se aplica la función de activación para producir la salida.

2. **Backpropagation (Retropropagación)**: Es el algoritmo utilizado para entrenar una RNA. Consiste en calcular el error de la red (diferencia entre la salida predicha y la real) y propagar este error hacia atrás para ajustar los pesos y biases de la red.

3. **Aprendizaje**: Durante el entrenamiento, la RNA ajusta repetidamente sus pesos y biases utilizando un algoritmo de optimización (como el descenso del gradiente) para minimizar el error en las predicciones.



<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

## Redes Neuronales Convolucionales

> Video de Dot Csv: [Redes Neuronales Convolucionales](https://www.youtube.com/watch?v=V8j1oENVz00)

Una Red Neuronal Convolucional es un tipo especializado de red neuronal diseñada específicamente para procesar datos con una estructura similar a una cuadrícula, como imágenes.

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/3eafca50-417f-4487-a85a-67a125350401)

1. **Capas Convolucionales**: Estas capas aplican un conjunto de filtros a la entrada. Cada filtro detecta características específicas, como bordes, texturas o colores. La operación de convolución escanea la imagen con un pequeño "ventana" y aplica una transformación para producir un mapa de características.

2. **Función de Activación**: Después de cada convolución, se aplica una función de activación, como la función ReLU (Rectified Linear Unit), para introducir no linealidades en el modelo. [Mas información](/Documentos/FuncionesDeActivacion.html)

3. **Pooling o Submuestreo**: Estas capas reducen la dimensionalidad espacial (ancho y alto) de los datos, conservando las características más importantes. Una técnica común es el "max pooling", que selecciona el valor máximo de un grupo de valores.

4. **Capas Totalmente Conectadas (FC, Fully Connected)**: Después de varias capas convolucionales y de pooling, las CNNs suelen tener una o más capas totalmente conectadas que procesan la información y producen la salida final, como una clasificación.

5. **Clasificación**: La última capa de una CNN generalmente produce una distribución de probabilidad sobre las clases objetivo, utilizando una función como la función softmax.

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

## Redes Neuronales que generan datos

Las redes neuronales que generan datos son modelos avanzados que se entrenan para producir datos que se asemejen a algunos datos de entrada reales. 
1. **Redes Generativas Adversarias (GANs)**:
   - **Funcionamiento**: Las GANs consisten en dos redes neuronales, el generador y el discriminador, que se entrenan simultáneamente a través de un juego adversario. El generador intenta producir datos que engañen al discriminador, mientras que el discriminador intenta distinguir entre datos reales y datos generados.
   - **Aplicaciones**: Creación de imágenes realistas, mejora de la resolución de imágenes, generación de arte, creación de modelos 3D, entre otros.

2. **Modelos Autoregresivos**:
   - **Funcionamiento**: Estos modelos generan datos de manera secuencial, prediciendo el siguiente elemento basándose en los elementos anteriores.
   - **Ejemplos**: PixelRNN, PixelCNN, y modelos de lenguaje como GPT (Generative Pre-trained Transformer).
   - **Aplicaciones**: Generación de texto, imágenes y música.

3. **Redes Neuronales Variacionales (VAEs)**:
   - **Funcionamiento**: Las VAEs son una clase de modelos generativos que aprenden a representar y generar datos en un espacio latente de manera probabilística.
   - **Aplicaciones**: Generación de imágenes, interpolación de datos, y aprendizaje de representaciones latentes.

4. **Modelos de Transformación Espacial**:
   - **Funcionamiento**: Estos modelos aprenden transformaciones espaciales para modificar datos de entrada de manera específica.
   - **Aplicaciones**: Alineación y transformación de imágenes y datos en general.

5. **Redes Generativas de Flujos Normales**:
   - **Funcionamiento**: Estos modelos utilizan transformaciones invertibles y se entrenan maximizando la verosimilitud de los datos.
   - **Aplicaciones**: Generación de imágenes y otros tipos de datos.

6. **Modelos basados en memoria**:
   - **Funcionamiento**: Estos modelos almacenan ejemplos de datos y generan nuevos datos basándose en la similitud con los datos almacenados.
   - **Aplicaciones**: Generación basada en ejemplos anteriores, como en la generación de música.


<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

## Tipos de Variables


Las variables se pueden clasificar en cuantitativas y cualitativas según la naturaleza de la información que representan. A continuación, se describen los tipos de cada una:

#### Variables Cuantitativas:

Son aquellas que representan una cantidad y pueden ser medidas numéricamente. Se dividen en:

1. **Discretas**: Estas variables pueden tomar valores específicos y contables, generalmente enteros. No pueden tener valores fraccionarios entre dos valores consecutivos.
   - **Ejemplo**: Número de hijos en una familia, cantidad de estudiantes en un aula.

2. **Continuas**: Estas variables pueden tomar cualquier valor dentro de un rango específico. Pueden tener valores fraccionarios.
   - **Ejemplo**: Altura de una persona, peso, temperatura.

#### Variables Cualitativas:

Son aquellas que describen características o cualidades que no pueden ser medidas con números. Se dividen en:

1. **Nominales**: Estas variables representan categorías o etiquetas sin un orden inherente.
   - **Ejemplo**: Color de ojos (azul, verde, marrón), género (masculino, femenino), tipo de vehículo (sedán, camioneta, convertible).

2. **Ordinales**: Estas variables representan categorías con un orden o jerarquía específico, pero la distancia entre las categorías no es uniforme ni tiene un significado específico.
   - **Ejemplo**: Niveles de educación (primaria, secundaria, universitaria), grados de satisfacción (insatisfecho, neutral, satisfecho).

>Es importante mencionar que, en algunas situaciones, las variables cualitativas ordinales pueden ser codificadas numéricamente para facilitar su análisis (por ejemplo, asignando 1 a "insatisfecho", 2 a "neutral" y 3 a "satisfecho"). Sin embargo, esto no convierte la variable en cuantitativa, ya que los números simplemente representan categorías con un orden específico y no tienen un significado cuantitativo real.

La correcta identificación y clasificación de las variables es esencial en estadística y investigación, ya que determina qué tipos de análisis son apropiados para los datos recopilados.

#### Ejemplo Practico

```markdown
| Nro. | Age | Sex | BP     | Colesterol | Na       | K       | Drug  |
|------|-----|-----|--------|------------|----------|---------|-------|
| 1    | 23  | F   | HIGH   | HIGH       | 0.792535 | 0.031258| drugY |
| 2    | 47  | M   | LOW    | HIGH       | 0.739309 | 0.056468| drugC |
| 3    | 47  | M   | LOW    | HIGH       | 0.697269 | 0.068944| drugC |
| 4    | 28  | F   | NORMAL | HIGH       | 0.563682 | 0.072289| drugX |
| 5    | 61  | F   | LOW    | HIGH       | 0.559294 | 0.030998| drugY |
| ...  | ... | ... | ...    | ...        | ...      | ...     | ...   |
| 197  | 16  | M   | LOW    | HIGH       | 0.743021 | 0.061886| drugC |
| 198  | 52  | M   | NORMAL | HIGH       | 0.549945 | 0.055581| drugX |
| 199  | 23  | M   | NORMAL | NORMAL     | 0.78452  | 0.055959| drugX |
| 200  | 40  | F   | LOW    | NORMAL     | 0.683503 | 0.060226| drugX |
```

Podemos clasificar el tipo de cada atributo de la siguiente manera:

1. **Nro.**: Cuantitativo Discreto - Representa un número de identificación o secuencia.
2. **Age**: Cuantitativo Discreto - Representa la edad en años completos.
3. **Sex**: Cualitativo Nominal - Indica el género (F para femenino, M para masculino).
4. **BP (Presión arterial)**: Cualitativo Ordinal - Indica el nivel de presión arterial (HIGH, LOW, NORMAL).
5. **Colesterol**: Cualitativo Ordinal - Indica el nivel de colesterol (HIGH, NORMAL).
6. **Na (Sodio)**: Cuantitativo Continuo - Representa una medida numérica del nivel de sodio.
7. **K (Potasio)**: Cuantitativo Continuo - Representa una medida numérica del nivel de potasio.
8. **Drug**: Cualitativo Nominal - Indica el tipo de medicamento (drugY, drugC, drugX, etc.).

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

## Descripciones Estadísticas Básicas
Las descripciones estadísticas básicas son herramientas fundamentales para entender y resumir un conjunto de datos. Estas medidas son esenciales para tomar decisiones informadas sobre cómo procesar y analizar los datos

#### Medidas de Tendencia Central
Estas medidas indican dónde se encuentra el "centro" de un conjunto de datos.

1. **Media (Promedio)**
   - Es la suma de todos los valores en un conjunto de datos dividida por el número de valores en ese conjunto.
   - Fórmula:
     \[
     \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
     \]

2. **Mediana**
   - Es el valor que divide un conjunto de datos en dos mitades, de modo que la mitad de los valores son menores o iguales a la mediana y la otra mitad son mayores o iguales.

3. **Moda**
   - Es el valor o valores que aparecen con mayor frecuencia en un conjunto de datos.

4. **Rango Medio**
   - Es el promedio del valor más bajo y el valor más alto en un conjunto de datos.
   - Fórmula:
     \[
     \text{Rango Medio} = \frac{\text{Valor Mínimo} + \text{Valor Máximo}}{2}
     \]

#### Medidas de Dispersión
Estas medidas indican cuánto varían los datos alrededor de la tendencia central.

1. **Varianza**
   - Es el promedio de las diferencias al cuadrado entre cada valor y la media.
   - Fórmula para la varianza de una población (denotada como \(\sigma^2\)):
     \[
     \sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}
     \]
   - Fórmula para la varianza de una muestra (denotada como \(s^2\)):
     \[
     s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}
     \]

2. **Desviación Estándar**
   - Es la raíz cuadrada de la varianza.
   - Fórmulas:
     \[
     \sigma = \sqrt{\sigma^2}
     \]
     \[
     s = \sqrt{s^2}
     \]

3. **Rango**
   - Es la diferencia entre el valor máximo y el valor mínimo en un conjunto de datos.

4. **Cuartiles**
    Dividen un conjunto de datos en cuatro partes iguales. El primer cuartil (Q1) es el valor que separa el 25% inferior de los datos, el segundo cuartil (Q2) es la mediana y el tercer cuartil (Q3) es el valor que separa el 75% inferior de los datos.

5. **Rango Intercuartil (IQR)**
   - Es la diferencia entre el tercer y el primer cuartil. Ayuda a medir la dispersión de los valores en el medio 50% de un conjunto de datos.
   - Fórmula:
     \[
     IQR = Q3 - Q1
     \]

Estas medidas son esenciales para comprender la distribución, la tendencia central y la variabilidad de un conjunto de datos.

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

## Graficos (Un choclo)

#### 1. Diagrama de Barras



<table><td>

- **Descripción**: Representa datos categóricos con barras rectangulares de longitudes proporcionales a los valores que representan.
- **Uso**: Se utiliza para comparar diferentes categorías de datos.
- **Ejemplo**: Puedes usar un diagrama de barras para mostrar las ventas de diferentes productos en un mes.
</td><td>


<img src='https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/8a8e7142-3fe2-4a57-9345-68e6cb5f133c' width='1000px'>
</td></table>



#### 2. Diagrama de Torta (o Gráfico Circular)

<table><td>

- **Descripción**: Representa datos en proporciones a un todo. Cada "rebanada" de la torta representa una categoría.
- **Uso**: Se utiliza para mostrar proporciones o porcentajes.
- **Ejemplo**: Puedes usar un diagrama de torta para mostrar la distribución del presupuesto de una empresa entre diferentes departamentos.
</td><td><img src='https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/4a8cf0d5-f2ec-459c-ba5c-9c57e2580193' width='1000px'></td></table>



#### 3. Histograma
- **Descripción**: Es similar a un diagrama de barras, pero se utiliza para representar la distribución de un conjunto de datos continuos o intervalos.
- **Uso**: Se utiliza para visualizar la distribución de frecuencias de un conjunto de datos.
- **Ejemplo**: Puedes usar un histograma para mostrar la distribución de edades de los empleados en una empresa.

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/ac455d0b-0f26-499a-8a47-49f8076afbb0)


#### 4. Diagrama de Caja (o Boxplot)
El diagrama de cajas, también conocido como "box plot" o "whisker plot", es una herramienta gráfica que proporciona una representación visual de la distribución y dispersión de un conjunto de datos. Es especialmente útil para identificar la mediana, los cuartiles y posibles valores atípicos en los datos.


![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/96759b0b-5b8a-483c-b9f1-f52dbbc928d2)

Se consideran valores atípicos leves a los que se encuentran a 1.5\*RIC más allá de los límites de la caja y atípicos extremos a los que están más allá de 3\*RIC.

A continuación, te explico sus componentes y cómo interpretarlos:

1. **Caja Central:**
   - La caja en sí representa el rango intercuartil (IQR), que es la distancia entre el primer cuartil (Q1) y el tercer cuartil (Q3). El IQR contiene la mitad central de los datos.
   - La línea dentro de la caja representa la mediana (Q2), que es el valor que divide el conjunto de datos en dos mitades. La mediana indica el valor central de los datos.

2. **Bigotes (Whiskers):**
   - Los "bigotes" son las líneas que se extienden desde la caja hacia los valores máximo y mínimo dentro de un rango determinado.
   - El bigote superior se extiende desde Q3 hasta el valor máximo dentro de 1.5*IQR de Q3.
   - El bigote inferior se extiende desde Q1 hasta el valor mínimo dentro de 1.5*IQR de Q1.
   - Los valores fuera de este rango se consideran valores atípicos y a menudo se representan con puntos o asteriscos fuera de los bigotes.

3. **Valores Atípicos:**
   - Son los puntos que caen fuera del rango de los bigotes. Estos puntos representan valores que son inusualmente altos o bajos en comparación con el resto del conjunto de datos.

4. **Rango:**
   - Es la distancia entre el valor mínimo y el valor máximo del conjunto de datos, incluidos los valores atípicos.

**Interpretación:**
- **Distribución de los datos:** Si la mediana está cerca del centro de la caja, los datos están aproximadamente simétricamente distribuidos. Si está más cerca de Q1 o Q3, los datos están sesgados.
- **Dispersión:** El ancho de la caja (IQR) indica la variabilidad de los datos. Una caja más ancha sugiere una mayor dispersión.
- **Valores Atípicos:** Los puntos fuera de los bigotes indican valores atípicos que pueden requerir una investigación adicional.
- **Comparación:** Los diagramas de cajas son útiles para comparar la distribución de varios conjuntos de datos en paralelo.

El diagrama de cajas es una herramienta poderosa para visualizar la distribución de un conjunto de datos, identificar su variabilidad y detectar valores atípicos. Es ampliamente utilizado en estadísticas y análisis de datos para obtener una rápida visión general de la distribución de los datos.

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/5c6b7a62-8456-4b03-87af-a7bce9e6021d)

#### 5. Diagrama de Dispersión (o Scatter Plot)
- **Descripción**: Muestra puntos en un plano cartesiano, donde cada punto representa una observación con dos variables.
- **Uso**: Se utiliza para visualizar la relación entre dos variables cuantitativas.
- **Ejemplo**: Puedes usar un diagrama de dispersión para mostrar la relación entre las horas de estudio y las calificaciones obtenidas por los estudiantes.

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/40cc78bd-fc43-4f5e-a14e-f50930955338)

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

### Relación entre atributos numéricos

<table><td>

Al momento de construir un modelo resulta de interés saber si dos atributos numéricos se encuentran linealmente relacionados o no. Para ello se usa el coeficiente de correlación lineal.
</td><td>

<img src='https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/2f9ee564-ae47-494b-9953-9c83dd33887c' width='1300px'>
</td></table>

> Diagrama de dispersión entre la longitud y el ancho del pétalo de una flor

### Coeficiente de correlación lineal

- Si 0.5≤  abs(Corr(A,B)) < 0.8 se dice que A y B tienen una correlación lineal débil.
- Si abs(Corr(A,B)) ≥ 0.8 se dice que A y B tienen una correlación lineal fuerte
- Si abs(Corr(A,B))<0.5 se dice que A y B no están correlacionados linealmente. Esto NO implica que son independientes, sólo que entre ambos no hay una correlación lineal

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

## 01b_Analisis de datos



<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

## 01c_Preprocesamiento de datos

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7c13752b-5a48-4a88-816d-242330e90478' height="10" width="100%">


# Conceptos Fuera de la teoria pero que sirven para reforsar el conocimiento


<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7c13752b-5a48-4a88-816d-242330e90478' height="10" width="100%">

# Derivadas Parciales

Las derivadas parciales son un concepto fundamental en cálculo multivariable y tienen aplicaciones en diversas áreas, como la física, la ingeniería y, por supuesto, en el aprendizaje automático y las redes neuronales.

### Definición:

Una derivada parcial de una función de varias variables es la derivada de esa función con respecto a una de sus variables, manteniendo las otras variables constantes.

### Notación:

Si \( f \) es una función de las variables \( x \) y \( y \), entonces la derivada parcial de \( f \) con respecto a \( x \) se denota de las siguientes maneras:
\[ \frac{\partial f}{\partial x} \quad \text{o} \quad f_x \]

De manera similar, la derivada parcial de \( f \) con respecto a \( y \) se denota como:
\[ \frac{\partial f}{\partial y} \quad \text{o} \quad f_y \]

### Ejemplo:

Considera la función \( f(x, y) = x^2y + xy^2 \).

1. La derivada parcial de \( f \) con respecto a \( x \) es:
\[ \frac{\partial f}{\partial x} = 2xy + y^2 \]

2. La derivada parcial de \( f \) con respecto a \( y \) es:
\[ \frac{\partial f}{\partial y} = x^2 + 2xy \]

### Aplicaciones en Aprendizaje Automático:

Las derivadas parciales son esenciales en el aprendizaje automático, especialmente en el entrenamiento de redes neuronales. Cuando se ajusta un modelo, se busca minimizar una función de pérdida o costo. Para hacerlo, se utiliza el algoritmo de descenso del gradiente, que requiere calcular el gradiente de la función de pérdida. El gradiente es simplemente un vector que contiene todas las derivadas parciales de la función con respecto a cada uno de los parámetros del modelo. Estas derivadas parciales indican cómo cambiar cada parámetro para reducir el error.

En resumen, las derivadas parciales proporcionan una manera de entender cómo una función cambia en una dirección específica en un espacio multidimensional, y son herramientas cruciales en muchos campos de la ciencia y la ingeniería.

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7c13752b-5a48-4a88-816d-242330e90478' height="10" width="100%">

# Suma Ponderada

Una suma ponderada es una combinación lineal de ciertos valores donde cada valor tiene un peso o ponderación asociado. En lugar de sumar los valores directamente, cada valor se multiplica por su peso correspondiente y luego se suman los resultados.

La fórmula general para una suma ponderada de \( n \) valores es:

\[ \text{Suma ponderada} = w_1 \cdot x_1 + w_2 \cdot x_2 + \ldots + w_n \cdot x_n \]

Donde:
- \( x_1, x_2, \ldots, x_n \) son los valores.
- \( w_1, w_2, \ldots, w_n \) son los pesos o ponderaciones correspondientes a cada valor.

### Ejemplo:

Supongamos que estamos calculando el promedio final de un estudiante en un curso que tiene tres componentes: tareas, exámenes y un proyecto final. Cada componente tiene un peso diferente en la calificación final:

- Tareas: 40%
- Exámenes: 50%
- Proyecto final: 10%

Si el estudiante obtuvo las siguientes calificaciones:
- Tareas: 85
- Exámenes: 90
- Proyecto final: 95

La calificación final ponderada sería:

\[ \text{Calificación final} = 0.40 \times 85 + 0.50 \times 90 + 0.10 \times 95 = 88 \]

Por lo tanto, la calificación final del estudiante sería 88.

### Aplicaciones:

Las sumas ponderadas son comunes en muchos campos:

1. **Aprendizaje automático**: En una neurona artificial de una red neuronal, la entrada se combina mediante una suma ponderada antes de pasar por una función de activación.
2. **Economía**: Para calcular índices como el Índice de Precios al Consumidor (IPC), se utiliza una suma ponderada de los precios de diferentes bienes y servicios.
3. **Educación**: Como en el ejemplo anterior, para calcular calificaciones finales basadas en diferentes componentes con diferentes ponderaciones.
4. **Investigación y análisis de datos**: Al combinar diferentes indicadores o métricas en un solo valor o índice.

En resumen, una suma ponderada es una herramienta matemática útil que permite combinar diferentes valores teniendo en cuenta su relevancia o importancia relativa.

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7c13752b-5a48-4a88-816d-242330e90478' height="10" width="100%">

# Funcion de activación

La función de activación en una red neuronal introduce no linealidades en el modelo, lo que le permite aprender y representar relaciones más complejas en los datos. Veamos qué significa esto con más detalle:

### Linealidad vs. No Linealidad:

1. **Funciones Lineales**: Una función es lineal si cumple con dos propiedades: aditividad y homogeneidad. En términos simples, una función lineal tiene la forma \(f(x) = mx + b\), donde \(m\) y \(b\) son constantes. No importa cuántas capas lineales apiles una encima de la otra en una red neuronal, la combinación seguirá siendo una transformación lineal. Esto limita la capacidad de la red para representar funciones más complejas.

2. **Funciones No Lineales**: Estas funciones no cumplen con las propiedades de aditividad y homogeneidad. Introducen curvas y permiten que la función tenga una forma más compleja. Las funciones no lineales pueden representar una amplia variedad de relaciones y patrones en los datos.

### Importancia de las No Linealidades en Redes Neuronales:

- **Capacidad de Modelado**: Al introducir no linealidades, una red neuronal puede aprender y modelar relaciones complejas en los datos. Esto es esencial para tareas como la clasificación de imágenes, donde las relaciones entre los píxeles pueden ser altamente no lineales.

- **Profundidad y Aprendizaje Jerárquico**: Las no linealidades permiten que las redes neuronales profundas aprendan características a diferentes niveles de abstracción. Por ejemplo, en una CNN que procesa imágenes, las primeras capas pueden aprender a detectar bordes, las capas intermedias pueden aprender a detectar formas, y las capas más profundas pueden aprender a detectar objetos completos.

### Ejemplos de Funciones de Activación No Lineales:

1. **ReLU (Rectified Linear Unit)**: \(f(x) = max(0, x)\). Es una de las funciones de activación más populares en redes neuronales profundas debido a su simplicidad y eficacia.

2. **Sigmoid**: \(f(x) = \frac{1}{1 + e^{-x}}\). Toma valores entre 0 y 1.

3. **Tanh (Tangente Hiperbólica)**: \(f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}\). Toma valores entre -1 y 1.

4. **Leaky ReLU**: Una variante de ReLU que permite pequeños valores negativos cuando \(x < 0\).

En resumen, las no linealidades son esenciales para la capacidad de las redes neuronales para aprender y representar relaciones complejas en los datos. Sin ellas, la red sería simplemente una combinación lineal de sus entradas, lo que limitaría severamente su utilidad.

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/f8906f0d-e728-4bd4-a5ab-acfaa18dc0b5)

## Explicación mas detallada

1. **ReLU (Rectified Linear Unit)**:
   - **Fórmula**: \(f(x) = max(0, x)\)
   - **Descripción**: La función ReLU es bastante simple. Si el valor de entrada \(x\) es positivo, devuelve \(x\). Si \(x\) es negativo o cero, devuelve 0.
   - **Gráficamente**: Imagina una línea que se eleva a 45 grados para valores positivos de \(x\) y se aplana completamente para valores negativos.
   - **Uso**: Es ampliamente utilizado en redes neuronales profundas porque es computacionalmente eficiente y ayuda a mitigar el problema del desvanecimiento del gradiente en cierta medida.

2. **Sigmoid**:
   - **Fórmula**: \(f(x) = \frac{1}{1 + e^{-x}}\)
   - **Descripción**: La función sigmoid toma cualquier valor de entrada y lo "aprieta" en un rango entre 0 y 1. Es una función en forma de "S".
   - **Gráficamente**: Imagina una curva en forma de "S" que se aplana a medida que se acerca a 0 y 1.
   - **Uso**: Fue ampliamente utilizado en las primeras redes neuronales, especialmente como función de activación en la capa de salida para clasificación binaria. Sin embargo, tiene problemas de desvanecimiento del gradiente en redes profundas, por lo que su uso ha disminuido en favor de ReLU y variantes.

3. **Tanh (Tangente Hiperbólica)**:
   - **Fórmula**: \(f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}\)
   - **Descripción**: Similar a la función sigmoid, pero en lugar de comprimir los valores en el rango [0,1], los comprime en el rango [-1,1].
   - **Gráficamente**: Imagina una curva en forma de "S" similar a la sigmoid, pero que se extiende desde -1 hasta 1 en lugar de 0 hasta 1.
   - **Uso**: Es preferible a la función sigmoid en muchos casos porque los valores centrados alrededor de 0 facilitan el aprendizaje.

4. **Leaky ReLU**:
   - **Fórmula**: \(f(x) = x\) si \(x > 0\), \(f(x) = \alpha x\) si \(x \leq 0\), donde \(\alpha\) es un pequeño valor positivo (por ejemplo, 0.01).
   - **Descripción**: Es una variante de ReLU que permite valores negativos pequeños cuando la entrada es menor que cero. Esto ayuda a evitar que las neuronas "mueran" y no se activen en absoluto.
   - **Gráficamente**: Similar a ReLU, pero en lugar de ser completamente plana para valores negativos, tiene una pendiente leve (determinada por \(\alpha\)).
   - **Uso**: Se utiliza como una solución al problema de las "neuronas muertas" en ReLU, donde algunas neuronas dejan de contribuir y se vuelven inactivas.

Estas funciones de activación introducen no linealidades en la red, lo que permite que la red aprenda relaciones más complejas en los datos. La elección de la función de activación puede depender de la naturaleza del problema y la arquitectura de la red.

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7c13752b-5a48-4a88-816d-242330e90478' height="10" width="100%">

# Descenso del Gradiente

> Video de Dot csv sobre [Descenso gradiente](https://www.youtube.com/watch?v=A6FiCDoz8_4)



El descenso del gradiente es un algoritmo de optimización utilizado para minimizar una función objetivo, que suele ser una función de pérdida o costo en el contexto del aprendizaje automático. Es especialmente útil para entrenar modelos con muchos parámetros, como las redes neuronales.

La idea detrás del descenso del gradiente es ajustar iterativamente los parámetros del modelo en la dirección que reduce el error, es decir, en la dirección opuesta al gradiente de la función de pérdida con respecto a esos parámetros.

### Funcionamiento básico del descenso del gradiente:

1. **Inicialización**: Selecciona un punto inicial (un conjunto inicial de parámetros) y un valor para la tasa de aprendizaje.

2. **Cálculo del Gradiente**: Calcula el gradiente de la función de pérdida con respecto a los parámetros en el punto actual. El gradiente es un vector que apunta en la dirección de máximo crecimiento de la función, y su magnitud indica cuán rápido crece la función en esa dirección.

3. **Actualización de Parámetros**: Ajusta los parámetros en la dirección opuesta al gradiente. La magnitud del ajuste está determinada por la tasa de aprendizaje.

4. **Iteración**: Repite los pasos 2 y 3 hasta que el gradiente sea muy pequeño (lo que indica que estás cerca de un mínimo) o hasta que se alcance un número máximo de iteraciones.

### Variantes y consideraciones:

- **Tasa de Aprendizaje**: Es un hiperparámetro que determina el tamaño de los pasos que se toman en cada iteración. Una tasa de aprendizaje demasiado alta puede hacer que el algoritmo oscile y no converja, mientras que una tasa de aprendizaje demasiado baja puede hacer que la convergencia sea muy lenta.

- **Descenso del Gradiente Estocástico (SGD)**: En lugar de usar todo el conjunto de datos para calcular el gradiente en cada paso (lo que puede ser costoso en términos de tiempo y memoria), el SGD utiliza un solo ejemplo o un pequeño lote (batch) en cada iteración.

- **Métodos con Momento**: Estos métodos, como el descenso del gradiente con momento o Adam, utilizan información de gradientes anteriores para acelerar la convergencia y superar mínimos locales.

- **Mínimos Locales**: Una de las preocupaciones con el descenso del gradiente es que puede quedar atrapado en mínimos locales, especialmente en funciones no convexas. Sin embargo, en la práctica, especialmente en el contexto de redes neuronales profundas, esto suele ser menos problemático de lo que se podría pensar.

El descenso del gradiente es fundamental en el aprendizaje automático y el aprendizaje profundo, y entender su funcionamiento y sus variantes es esencial para entrenar modelos eficientemente.

![1_yd9YMy2pkzCY-9jrsWFesA](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/c8e13577-0171-41af-8c93-0d34305992c2)

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7c13752b-5a48-4a88-816d-242330e90478' height="10" width="100%">