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

## 01a_Introduccion

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

"Discreta" y "continua" son términos que se refieren a dos tipos diferentes de variables o conjuntos de datos. Vamos a definir y diferenciar cada uno.

### Discreta

Una variable discreta es aquella que puede tomar un número finito o un conjunto contable infinito de valores. Estos valores suelen ser resultados específicos y separados, y no pueden ser subdivididos de manera significativa.

- **Ejemplos**
  - El número de estudiantes en una clase (puedes tener 20, 21, 22 estudiantes, pero no 20.5 estudiantes).
  - El número de lanzamientos de una moneda hasta obtener cara.
  - La cantidad de libros en una estantería.
- **Características**
  - Los valores que puede tomar son contables.
  - No tiene sentido hablar de valores "entre" dos valores discretos adyacentes. Por ejemplo, entre 3 y 4 estudiantes, no hay ningún valor válido.

### Continua

Una variable continua es aquella que puede tomar cualquier valor dentro de un rango específico. Estos valores pueden ser subdivididos infinitamente, y hay un número infinito de valores posibles entre dos valores cualesquiera.

- **Ejemplos**
  - La altura de una persona (puede ser 1.75 metros, 1.751 metros, 1.7512 metros, etc.).
  - El tiempo que tarda un corredor en completar una maratón.
  - La temperatura de una habitación.
- **Características**
  - Los valores que puede tomar son incontables dentro de un rango.
  - Siempre hay valores intermedios entre dos valores cualesquiera, sin importar cuán cercanos estén.

En resumen, mientras que las variables discretas toman valores específicos y separados, las variables continuas pueden tomar cualquier valor dentro de un rango continuo. Estas distinciones son fundamentales en estadísticas, matemáticas y muchas áreas de la ciencia y la ingeniería.

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

### Aprendizaje Supervisado

El aprendizaje supervisado es un tipo de aprendizaje automático donde se proporciona un conjunto de datos de entrada junto con las respuestas correctas (etiquetas) con el objetivo de entrenar un modelo que pueda hacer predicciones precisas sobre datos no vistos previamente.


### Clasificación
En problemas de clasificación, el objetivo es predecir una etiqueta categórica o discreta para una entrada dada. Es decir, se clasifica la entrada en una de varias categorías o clases.

- **Ejemplos**
  - Determinar si un correo electrónico es spam o no spam.
  - Clasificar una imagen en categorías como "gato", "perro" o "pájaro".
  - Diagnosticar si un paciente tiene una enfermedad específica o no.
- **Características**: 
  - Las respuestas (etiquetas) son discretas y pertenecen a un conjunto finito.
  - No hay orden inherente entre las clases. Por ejemplo, en una clasificación de animales, "gato" no es mayor ni menor que "perro".

### Regresión
En problemas de regresión, el objetivo es predecir un valor continuo para una entrada dada. A diferencia de la clasificación, donde se predice una etiqueta de clase, en la regresión se predice una cantidad numérica.

- **Ejemplos**
  - Predecir el precio de una casa basado en sus características (tamaño, ubicación, número de habitaciones, etc.).
  - Estimar la temperatura de una ciudad en un día futuro.
  - Prever las ventas de un producto en los próximos meses.
- **Características**
  - Las respuestas son valores numéricos continuos.
  - Hay un orden inherente en las respuestas. Por ejemplo, un precio de casa de \$300,000 es mayor que uno de \$200,000.

</td></tr></table>

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/c7e97813-e3f9-4779-b3cd-39c1dc6127b9)

En resumen, la principal diferencia entre clasificación y regresión en el aprendizaje supervisado radica en el tipo de respuesta que se está tratando de predecir. Si es una categoría o clase, es un problema de clasificación. Si es un valor numérico continuo, es un problema de regresión.

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5' height="10" width="100%">

### Red Neuronal Artificial

Es un modelo computacional inspirado en la forma en que las redes neuronales biológicas del cerebro humano procesan la información. Está compuesta por unidades llamadas "neuronas" o "nodos" organizadas en capas. Aquí tienes una representación visual simplificada de una RNA:

![Red Neuronal Artificial](https://showme.redstarplugin.com/d/d:mfplYxEO)


Ahora, desglosemos los componentes y el funcionamiento básico de una RNA:

**Entradas (Input Layer)**
Aquí es donde la red recibe la información del mundo exterior. Cada neurona en esta capa representa una característica distinta del dato de entrada.

**Capas Ocultas (Hidden Layers)**
Estas son las capas entre la entrada y la salida. Las neuronas en estas capas realizan transformaciones en los datos de entrada. Una RNA puede tener varias capas ocultas, y la profundidad de estas capas es lo que da lugar a la denominación "redes neuronales profundas" o "deep learning".

**Salidas (Output Layer)**
Esta capa produce el resultado o la predicción de la red. El número de neuronas aquí depende del tipo de tarea. Por ejemplo, para una tarea de clasificación binaria, podría haber solo una neurona.

**Neurona**
Es la unidad básica de una RNA. Recibe varias entradas, las multiplica por sus respectivos pesos, suma los productos y luego pasa el resultado a través de una función de activación para producir una salida.

**Pesos**
Son valores que determinan la importancia de una entrada particular para una neurona. Estos se ajustan durante el proceso de entrenamiento para mejorar la precisión de la red.

**Función de Activación**
Es una función matemática que determina si una neurona debe activarse o no. Las funciones de activación más comunes incluyen la función sigmoide, ReLU (Rectified Linear Unit) y tanh.

El entrenamiento de una RNA implica ajustar los pesos de las conexiones entre las neuronas para minimizar el error entre las predicciones de la red y los valores reales. Esto se hace utilizando algoritmos como el descenso del gradiente.

Las RNAs son fundamentales en muchos campos del aprendizaje automático y la inteligencia artificial, incluyendo la visión por computadora, el procesamiento del lenguaje natural, y la predicción de series temporales, entre otros.


## 01b_Analisis de datos

## 01c_Preprocesamiento de datos