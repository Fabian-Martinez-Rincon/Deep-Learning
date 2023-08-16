## Ejercicio 1
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

## Ejercicio 2

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