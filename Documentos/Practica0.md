<div align='center'>

# Practica 0 Introducción a Python

<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWwxNmxvcmZiNjFyNjF0NWwwN2ZkaGsxeGh1eTk0bHl6MG05N3ZobCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cbpsz18jDBrQdEhPKR/giphy.gif'></div>

# Jupyter Notebooks y Google Colab
### Ejercicio 1
**Respuestas:**
- **¿Qué es un cuaderno (notebook) Jupyter?**
  - Un cuaderno Jupyter es una herramienta de código abierto que permite crear y compartir documentos interactivos que contienen código, ecuaciones, visualizaciones y texto narrativo. Estos cuadernos se utilizan ampliamente en análisis de datos, enseñanza, ciencia de datos, entre otros. Los cuadernos Jupyter son ideales para crear un ambiente donde se pueden combinar la ejecución de código y la documentación en un solo lugar.
- **¿Qué es una celda?**
  - Una celda es la unidad básica de contenido en un cuaderno Jupyter. Es un espacio donde se puede escribir código para ser ejecutado o se puede introducir texto para explicación y documentación.
- **¿Qué tipos de celdas existen?**
  - Existen tres tipos principales de celdas en un cuaderno Jupyter:
    1. **Celda de código:** Contiene código que puede ser ejecutado. Al correr esta celda, los resultados se muestran debajo de ella.
    2. **Celda de texto/Markdown:** Esta celda contiene texto formateado utilizando el lenguaje Markdown. Permite incluir explicaciones, imágenes, enlaces y más.
    3. **Celda Raw:** Es una celda que no se renderiza. Se utiliza para introducir contenido que no se desea ejecutar o transformar.
- **¿Qué es un entorno de ejecución?**
  - Un entorno de ejecución se refiere al contexto o espacio donde se ejecuta un código o programa. Proporciona todas las herramientas, bibliotecas, variables y recursos necesarios para que el código funcione correctamente. En el ámbito de Jupyter, el entorno de ejecución es gestionado por un "kernel", que es el encargado de interpretar y ejecutar el código escrito en las celdas.
- **¿Cuánto tiempo dura una sesión de un entorno?**
  - La duración de una sesión de entorno de ejecución varía según dónde se esté ejecutando el cuaderno:
    - **Localmente:** En un Jupyter Notebook ejecutado en una máquina local, el entorno de ejecución (o kernel) continúa funcionando hasta que el usuario lo detiene o cierra el cuaderno.
    - **En plataformas en la nube:** En plataformas como Google Colab, la duración de una sesión puede ser limitada. Por ejemplo, las sesiones gratuitas en Google Colab suelen tener una duración máxima de 12 horas. Es recomendable revisar la documentación específica de la plataforma que se esté utilizando para detalles precisos.

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

### Ejercicio 2

Las celdas de código de un cuaderno no solo permiten ejecutar instrucciones de Python. Utilizando el símbolo ! (signo de admiración) es posible ejecutar los comandos disponibles desde la línea de comandos de su sistema operativo. De esta manera `!ls` o `!dir` (dependiendo el sistema operativo) listan los archivos de la carpeta actual y `!pip` o `!conda` permiten administrar los paquetes python.

Experimente la ejecución de varios comandos del sistema operativo a través de celdas de código. Entre las
pruebas incluya la invocación de:
- python para determinar la versión instalada.
- pip show nombre (pandas, numpy, tensorflow, etc.) de paquete para saber la versión instalada.
- comandos que permitan crear y eliminar carpetas.


El ejercicio que has mencionado se refiere a la ejecución de comandos del sistema operativo directamente desde un cuaderno Jupyter (o IPython). A continuación, te mostraré cómo hacerlo:

1. **Ejecutar comandos del sistema operativo**: 
   En un cuaderno Jupyter, puedes ejecutar comandos del sistema operativo precediendo el comando con un signo de exclamación `!`.

   Ejemplo:
   - Para listar los archivos en la carpeta actual (en sistemas Unix-like):
     ```python
     !ls
     ```
   - Para sistemas Windows:
     ```python
     !dir
     ```

2. **Determinar la versión de Python**:
   ```python
   !python --version
   ```

3. **Ver la versión de un paquete específico con pip**:
   - Para `pandas`:
     ```python
     !pip show pandas
     ```
   - Para `numpy`:
     ```python
     !pip show numpy
     ```
   - Y así sucesivamente para otros paquetes.

4. **Crear y eliminar carpetas**:
   - Crear una carpeta llamada "test_folder":
     ```python
     !mkdir test_folder
     ```
   - Eliminar la carpeta "test_folder":
     ```python
     !rmdir test_folder
     ```

Estos comandos se pueden ejecutar directamente en las celdas de un cuaderno Jupyter. Sin embargo, ten en cuenta que la capacidad de ejecutar comandos del sistema operativo desde un cuaderno puede variar según la configuración de seguridad y el entorno en el que se esté ejecutando el cuaderno.

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

### Ejercicio 3
Dado que el entorno de ejecución de un cuaderno Colab tiene un límite de duración, es importante descargar o salvar fuera del mismo los archivos que se generan.

Conecte su cuenta de Google Drive con Google Colab:

- Acceda a la url https://colab.research.google.com/ y autentíquese con su usuario Google. Cree un nuevo cuaderno (notebook).
- Asocie Drive con Colab. Compruebe que Drive queda montado como una carpeta.
- Suba un pequeño archivo de texto a Drive (NO a Colab) y ábralo desde una celda de código Colab utilizando el siguiente código:
  ```python
  ruta_arch = '....' # ruta y nombre a archivo a LEER desde su drive
  f = open(ruta_arch, 'r') # abre archivo para leer
  print(f.readlines()) # imprime contenido en pantalla
  f.close() # cierra archivo
  ```
- Genere el siguiente archivo y guárdelo en su carpeta Drive, comprobando que efectivamente se ha creado con el contenido esperado:
  ```python
  ruta_arch = '....' # ruta y nombre a archivo a ESCRIBIR en su drive
  f = open(ruta_arch, 'w') # abre archivo para escribir
  texto = 'Esta es una linea de texto\nEsta es otra línea de text'
  f.writelines(texto) # escribe contenido en archivo
  f.close() # cierra archivo
  ```

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

# Repaso de Python

### Ejercicio 1
Investigue/repase que son las listas, tuplas, conjuntos y diccionarios nativos de Python (puede consultar https://www.youtube.com/watch?v=CCUNuqqn7PQ) . Utilizando los constructores para cada tipo de dato genere códigos de ejemplo y recórralos imprimiendo sus valores.

1. **Listas**:
   - Son colecciones ordenadas y mutables.
   - Pueden contener cualquier tipo de dato: números, cadenas, otras listas, etc.
   - Se definen usando corchetes `[]`.

   Ejemplo:
   ```python
   lista = [1, 2, 3, 4, 5]
   for elemento in lista:
       print(elemento)
   ```

2. **Tuplas**:
   - Son colecciones ordenadas e inmutables.
   - Se definen usando paréntesis `()`.

   Ejemplo:
   ```python
   tupla = (1, 2, 3, 4, 5)
   for elemento in tupla:
       print(elemento)
   ```

3. **Conjuntos (sets)**:
   - Son colecciones no ordenadas y no tienen elementos duplicados.
   - Se definen usando llaves `{}` o con el constructor `set()`.

   Ejemplo:
   ```python
   conjunto = {1, 2, 3, 4, 5}
   for elemento in conjunto:
       print(elemento)
   ```

4. **Diccionarios**:
   - Son colecciones no ordenadas de pares clave-valor.
   - Las claves son únicas y pueden ser de cualquier tipo inmutable.
   - Se definen usando llaves `{}` con pares clave-valor separados por `:`.

   Ejemplo:
   ```python
   diccionario = {"a": 1, "b": 2, "c": 3}
   for clave, valor in diccionario.items():
       print(f"Clave: {clave}, Valor: {valor}")
   ```

Puedes ejecutar estos ejemplos en tu entorno Python para ver cómo funcionan. ¡Espero que esto te ayude a comprender mejor estos tipos de datos en Python!

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

### Ejercicio 2
Genere el código necesario para recorrer simultáneamente 2 listas con la misma cantidad de elementos e imprima los mismos utilizando un único for (tip: función zip).

<table border="1">
    <thead>
        <tr>
            <th>Código</th>
            <th>Salida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>

```python
lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']

for elemento1, elemento2 in zip(lista1, lista2):
    print(elemento1, elemento2)
```

</td>
<td>
  1 a<br>
  2 b<br>
  3 c<br>
  4 d<br>
  5 e
</td>
</tr>
</tbody>
</table>


<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

### Ejercicio 3
Implemente una función que a partir de la lista que recibe cómo parámetro, retorne una nueva lista sin elementos repetidos. Compruebe su correcto funcionamiento.

```python
def sin_repetidos(lista):
    """
    Esta función recibe una lista y retorna una nueva lista
     sin elementos repetidos.
    """
    return list(dict.fromkeys(lista))

# Prueba
lista_original = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
lista_sin_repetidos = sin_repetidos(lista_original)

lista_sin_repetidos
```

> [1, 2, 3, 4, 5, 6, 7]


La función `sin_repetidos` ha sido implementada correctamente. Al proporcionarle la lista \([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]\), ha retornado una nueva lista sin elementos repetidos: \([1, 2, 3, 4, 5, 6, 7]\).

El método utilizado convierte la lista en un diccionario para eliminar duplicados (ya que las claves de un diccionario no pueden repetirse) y luego convierte el diccionario de nuevo en una lista. Es un enfoque eficiente para lograr el objetivo.

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

### Ejercicio 4
Implemente una función que calcule la distancia entre 2 puntos (2D). Utilice la función sqrt del paquete math para implementarla y compruebe el correcto funcionamiento de la misma.

```python
import math

def distancia(punto1, punto2):
    """
    Esta función calcula la distancia entre dos puntos en un plano 2D.
    """
    dx = punto2[0] - punto1[0]
    dy = punto2[1] - punto1[1]
    return math.sqrt(dx**2 + dy**2)

# Prueba
punto_a = (1, 2)
punto_b = (4, 6)
distancia_calculada = distancia(punto_a, punto_b)

distancia_calculada
```
>5.0

La función `distancia` ha sido implementada correctamente. Al proporcionarle los puntos \( (1, 2) \) y \( (4, 6) \), ha calculado una distancia de 5.0 unidades entre ellos, lo que es consistente con la fórmula de distancia en un plano 2D. 

La fórmula para calcular la distancia entre dos puntos \( (x_1, y_1) \) y \( (x_2, y_2) \) en un plano 2D es:

\[
\text{distancia} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

### Ejercicio 5
Investigue y escriba código que demuestre el funcionamiento de los “slices” en listas

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">