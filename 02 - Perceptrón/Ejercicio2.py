import pandas as pd
from sklearn.preprocessing import StandardScaler
import perceptron as p
import os

PATH_BASE = os.path.dirname(os.path.dirname(__file__))
PATH_SOURCE = os.path.join(PATH_BASE, "Datos")

# Archivo de datos
FILE_NAME = 'hojas.csv'
FILE_PATH = os.path.join(PATH_SOURCE, FILE_NAME)

try:
    with open(FILE_PATH, mode='r', encoding="UTF-8") as file:
        df = pd.read_csv(file)
    X = df[['Perimetro', 'Area']].values
    y = df['Clase'].apply(lambda x: 1 if x == 'Helecho' else 0).values
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    perceptron = p.Perceptron(input_size=2, lr=0.01, epochs=300)
    perceptron.fit(X_scaled, y)
    
    print(perceptron.__str__())
    
except FileNotFoundError:
    print('No existe el archivo', FILE_PATH)
except NotADirectoryError:
    print('La ruta no es un directorio ', PATH_SOURCE)