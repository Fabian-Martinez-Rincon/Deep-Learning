import pandas as pd
from sklearn.preprocessing import StandardScaler
import perceptron as p
import os

FILE_PATH = './Practica/Datos/hojas.csv'
file_path = './Practica/Datos/hojas.csv'
df = pd.read_csv(file_path)
print(df)
print()

X = df[['Perimetro', 'Area']].values
y = df['Clase'].apply(lambda x: 1 if x == 'Helecho' else 0).values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

perceptron = p.Perceptron(input_size=2, lr=0.01, epochs=300)
perceptron.fit(X_scaled, y)

print("Pesos del Perceptrón:", perceptron.W)
