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

### Discreta

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

### Continua

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

El aprendizaje supervisado es un tipo de aprendizaje automático donde se proporciona un conjunto de datos de entrada junto con las respuestas correctas (etiquetas) con el objetivo de entrenar un modelo que pueda hacer predicciones precisas sobre datos no vistos previamente.

### Clasificación


En problemas de clasificación, el objetivo es predecir una etiqueta categórica o discreta para una entrada dada. Es decir, se clasifica la entrada en una de varias categorías o clases.

<table><td>


- Determinar si un correo electrónico es spam o no spam.
- Clasificar una imagen en categorías como "gato", "perro" o "pájaro".
- Diagnosticar si un paciente tiene una enfermedad específica o no.

</td><td>



<img src='https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/37c37b79-0381-4afb-b898-d04a698eec25' width='400px'>
</td></table>



### Regresión

En problemas de regresión, el objetivo es predecir un valor continuo para una entrada dada. A diferencia de la clasificación, donde se predice una etiqueta de clase, en la regresión se predice una cantidad numérica.

<table><td>

- Predecir el precio de una casa basado en sus características (tamaño, ubicación, número de habitaciones, etc.).
- Estimar la temperatura de una ciudad en un día futuro.
- Prever las ventas de un producto en los próximos meses.

</td><td>



<img src='https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/99613447-4e22-4947-b037-b24b10919dc3' width='800px'>
</td></table>


### Diferencias

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

## Redes Neuronales Convolucionales

Una Red Neuronal Convolucional es un tipo especializado de red neuronal diseñada específicamente para procesar datos con una estructura similar a una cuadrícula, como imágenes.

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/3eafca50-417f-4487-a85a-67a125350401)

1. **Capas Convolucionales**: Estas capas aplican un conjunto de filtros a la entrada. Cada filtro detecta características específicas, como bordes, texturas o colores. La operación de convolución escanea la imagen con un pequeño "ventana" y aplica una transformación para producir un mapa de características.

2. **Función de Activación**: Después de cada convolución, se aplica una función de activación, como la función ReLU (Rectified Linear Unit), para introducir no linealidades en el modelo. [Mas información](/Documentos/FuncionesDeActivacion.html)

3. **Pooling o Submuestreo**: Estas capas reducen la dimensionalidad espacial (ancho y alto) de los datos, conservando las características más importantes. Una técnica común es el "max pooling", que selecciona el valor máximo de un grupo de valores.

4. **Capas Totalmente Conectadas (FC, Fully Connected)**: Después de varias capas convolucionales y de pooling, las CNNs suelen tener una o más capas totalmente conectadas que procesan la información y producen la salida final, como una clasificación.

5. **Clasificación**: La última capa de una CNN generalmente produce una distribución de probabilidad sobre las clases objetivo, utilizando una función como la función softmax.




## 01b_Analisis de datos

## 01c_Preprocesamiento de datos