<div align="center"> 

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

<img src='https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat'><img src='https://img.shields.io/github/stars/Fabian-Martinez-Rincon/Computabilidad-y-Complejidad'><img src='https://img.shields.io/github/repo-size/Fabian-Martinez-Rincon/Computabilidad-y-Complejidad'>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=1200&pause=1000&color=F78E23&center=true&width=635&lines=Deep Learning"/>



<a title="" href="https://cafecito.app/ei-materias"><img src="/Documentos/Cafecito.png" alt="" /></a>

</div>

> pip install pandas

<div align='center'>
<button onclick="toggleDarkMode()">Oscuro</button>
<a href='https://github.com/Fabian-Martinez-Rincon/Deep-Learning/tree/main'><button style='background: #ecec00'> ⭐ </button></a>
<a href='https://github.com/Fabian-Martinez-Rincon'><button style='background: #000000'>Github</button></a>

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5
' height="10" width="100%"></div>


- Parcial 06/11/2023
- [Practica 0 Introducción a Python]()
- [Practica 1 Análisis de datos y preprocesamientoCarpeta](#práctica-2-mt)


<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5
' height="10" width="100%">

# Practica 0 Introducción a Python

---

## Jupyter Notebooks y Google Colab

### Ejercicio 1

**¿Qué es un cuaderno (notebook) Jupyter?**

Un cuaderno Jupyter es una herramienta de código abierto que permite crear y compartir documentos interactivos que contienen código, ecuaciones, visualizaciones y texto narrativo. Los cuadernos Jupyter son ideales para crear un ambiente donde se pueden combinar la ejecución de código y la documentación en un solo lugar.

**¿Qué es una celda?**
Una celda es la unidad básica de contenido en un cuaderno Jupyter. Es un espacio donde se puede escribir código para ser ejecutado o se puede introducir texto para explicación y documentación.

**¿Qué tipos de celdas existen?**

Existen tres tipos principales de celdas en un cuaderno Jupyter:
1. **Celda de código:** Contiene código que puede ser ejecutado. Al correr esta celda, los resultados se muestran debajo de ella.
2. **Celda de texto/Markdown:** Esta celda contiene texto formateado utilizando el lenguaje Markdown. Permite incluir explicaciones, imágenes, enlaces y más.
3. **Celda Raw:** Es una celda que no se renderiza. Se utiliza para introducir contenido que no se desea ejecutar o transformar.

**¿Qué es un entorno de ejecución?**
Un entorno de ejecución se refiere al contexto o espacio donde se ejecuta un código o programa. Proporciona todas las herramientas, bibliotecas, variables y recursos necesarios para que el código funcione correctamente. En el ámbito de Jupyter, el entorno de ejecución es gestionado por un "kernel", que es el encargado de interpretar y ejecutar el código escrito en las celdas.

**¿Cuánto tiempo dura una sesión de un entorno?**
La duración de una sesión de entorno de ejecución varía según dónde se esté ejecutando el cuaderno:
- **Localmente:** En un Jupyter Notebook ejecutado en una máquina local, el entorno de ejecución (o kernel) continúa funcionando hasta que el usuario lo detiene o cierra el cuaderno.
- **En plataformas en la nube:** En plataformas como Google Colab, la duración de una sesión puede ser limitada. Por ejemplo, las sesiones gratuitas en Google Colab suelen tener una duración máxima de 12 horas. Es recomendable revisar la documentación específica de la plataforma que se esté utilizando para detalles precisos.

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5
' height="10" width="100%">

### Ejercicio 2

Las celdas de código de un cuaderno no solo permiten ejecutar instrucciones de Python. Utilizando el símbolo ! (signo de admiración) es posible ejecutar los comandos disponibles desde la línea de comandos de su sistema operativo. De esta manera `!ls` o `!dir` (dependiendo el sistema operativo) listan los archivos de la carpeta actual y `!pip` o `!conda` permiten administrar los paquetes python.

Experimente la ejecución de varios comandos del sistema operativo a través de celdas de código. Entre las
pruebas incluya la invocación de:
- python para determinar la versión instalada.
- pip show nombre (pandas, numpy, tensorflow, etc.) de paquete para saber la versión instalada.
- comandos que permitan crear y eliminar carpetas.


El ejercicio que has mencionado se refiere a la ejecución de comandos del sistema operativo directamente desde un cuaderno Jupyter (o IPython). A continuación, te mostraré cómo hacerlo:

[Resolución en el jupyter Notebook](https://github.com/Fabian-Martinez-Rincon/Deep-Learning/blob/main/Practica/Practica0/ejercicio2.ipynb)

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5
' height="10" width="100%">

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

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/7eebf649-e558-43e2-ad5f-9977dc5ff3e5
' height="10" width="100%">