import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import perceptron as p  # Asegúrate de que este módulo esté en el mismo directorio o en tu PYTHONPATH

def load_and_preprocess_data(file_path):
    """
    Carga y preprocesa los datos desde un archivo CSV.

    Parámetros:
    - file_path: Ruta al archivo CSV.

    Retorna:
    - X_scaled: Características escaladas.
    - y: Etiquetas.
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        df = pd.read_csv(file)
    X = df[['Perimetro', 'Area']].values
    y = df['Clase'].apply(lambda x: 1 if x == 'Helecho' else 0).values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y

def train_perceptron(X, y):
    """
    Entrena un Perceptrón y lo devuelve.

    Parámetros:
    - X: Características.
    - y: Etiquetas.

    Retorna:
    - Un objeto Perceptrón entrenado.
    """
    perceptron = p.Perceptron(input_size=2, lr=0.01, epochs=300)
    perceptron.fit(X, y)
    return perceptron

def main():
    """Función principal."""
    # Configurar rutas de archivos
    PATH_BASE = os.path.dirname(os.path.dirname(__file__))
    PATH_SOURCE = os.path.join(PATH_BASE, "Datos")
    FILE_NAME = 'hojas.csv'
    FILE_PATH = os.path.join(PATH_SOURCE, FILE_NAME)

    try:
        X_scaled, y = load_and_preprocess_data(FILE_PATH)
    except FileNotFoundError:
        print(f'No existe el archivo {FILE_PATH}')
        return
    except NotADirectoryError:
        print(f'La ruta no es un directorio {PATH_SOURCE}')
        return
    else:
        trained_perceptron = train_perceptron(X_scaled, y)
        print(trained_perceptron.__str__())

if __name__ == "__main__":
    main()
