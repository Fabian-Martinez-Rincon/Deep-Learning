# main.py

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import perceptron as p

def load_and_preprocess_data(file_path):
    """Carga y preprocesa los datos desde un archivo CSV."""
    try:
        with open(file_path, mode='r', encoding="UTF-8") as file:
            df = pd.read_csv(file)
    except FileNotFoundError as e:
        raise Exception(f"El archivo {file_path} no se encuentra.") from e
    except Exception as e:
        raise Exception("Error desconocido al abrir el archivo.") from e

    X = df[['Perimetro', 'Area']].values
    y = df['Clase'].apply(lambda x: 1 if x == 'Helecho' else 0).values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler

def predict_new_leaf(perceptron, scaler, perimetro, area):
    entrada_nueva = np.array([[perimetro, area]])
    entrada_nueva_norm = scaler.transform(entrada_nueva)
    entrada_nueva_norm = np.insert(entrada_nueva_norm, 0, 1)
    z_nuevo = np.dot(perceptron.W, entrada_nueva_norm)
    y_nuevo = 1 if z_nuevo >= 0 else 0
    return z_nuevo, y_nuevo

def main():
    """Función principal."""
    # Define constantes para las rutas de archivos
    PATH_BASE = os.path.dirname(os.path.dirname(__file__))
    PATH_SOURCE = os.path.join(PATH_BASE, "Datos")
    FILE_NAME = 'hojas.csv'
    FILE_PATH = os.path.join(PATH_SOURCE, FILE_NAME)

    try:
        X_scaled, y, scaler = load_and_preprocess_data(FILE_PATH)
        perceptron = p.Perceptron(input_size=2, lr=0.01, epochs=300)
        perceptron.fit(X_scaled, y)
        print(perceptron)

        perimetro_nuevo = 770
        area_nueva = 5000
        z_nuevo, y_nuevo = predict_new_leaf(perceptron, scaler, perimetro_nuevo, area_nueva)
        
        print(f"La suma ponderada (z) es: {z_nuevo}")
        print(f"La salida del perceptrón (y) es: {y_nuevo}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
