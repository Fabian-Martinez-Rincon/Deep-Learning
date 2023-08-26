import pandas as pd
from sklearn.preprocessing import StandardScaler
import perceptron as p

# Leer el archivo hojas.csv
file_path = './Practica/Datos/hojas.csv'
df = pd.read_csv(file_path)
print(df)
print()

# Extraer características y etiquetas
X = df[['Perimetro', 'Area']].values
y = df['Clase'].apply(lambda x: 1 if x == 'Helecho' else 0).values

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
print()

# Entrenar el Perceptrón
perceptron = p.Perceptron(input_size=2, lr=0.01, epochs=300)
perceptron.fit(X_scaled, y)

# Mostrar los pesos del Perceptrón entrenado
print("Pesos del Perceptrón:", perceptron.W)
