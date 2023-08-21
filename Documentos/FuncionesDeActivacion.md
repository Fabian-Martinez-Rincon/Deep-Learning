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