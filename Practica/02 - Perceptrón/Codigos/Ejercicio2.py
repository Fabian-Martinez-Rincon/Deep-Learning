import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Definir la clase Perceptrón
class Perceptron:
    def __init__(self, input_size, lr=1, epochs=100):
        self.W = np.zeros(input_size + 1)
        self.epochs = epochs
        self.lr = lr
    
    def activation_fn(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        return self.activation_fn(z)

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = np.insert(X[i], 0, 1)
                y = self.predict(X[i])
                e = d[i] - y
                self.W = self.W + self.lr * e * x

# Leer el archivo hojas.csv
file_path = './Practica/Datos/hojas.csv'
df = pd.read_csv(file_path)

# Extraer características y etiquetas
X = df[['Perimetro', 'Area']].values
y = df['Clase'].apply(lambda x: 1 if x == 'Helecho' else 0).values

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenar el Perceptrón
perceptron = Perceptron(input_size=2, lr=0.01, epochs=300)
perceptron.fit(X_scaled, y)

# Mostrar los pesos del Perceptrón entrenado
print("Pesos del Perceptrón:", perceptron.W)
