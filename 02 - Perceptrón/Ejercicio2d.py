import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import perceptron as p

def load_data(file_path):
    """Carga los datos desde un archivo CSV."""
    with open(file_path, mode='r', encoding="UTF-8") as file:
        df = pd.read_csv(file)
    return df

def preprocess_data(df):
    """Preprocesa los datos y devuelve características y etiquetas."""
    X = df[['Perimetro', 'Area']].values
    y = df['Clase'].apply(lambda x: 1 if x == 'Helecho' else 0).values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y

def run_multiple_trainings(X, y, num_executions=50, max_iterations=100):
    """Ejecuta múltiples entrenamientos y devuelve estadísticas."""
    successful_executions = 0
    total_iterations = 0
    
    for _ in range(num_executions):
        perceptron = p.Perceptron(input_size=2, lr=0.01, epochs=max_iterations)
        perceptron.fit(X, y)
        
        y_pred = [perceptron.predict(x) for x in X]
        if accuracy_score(y, y_pred) == 1.0:
            successful_executions += 1
            total_iterations += max_iterations

    percentage_successful = (successful_executions / num_executions) * 100
    average_iterations = total_iterations / successful_executions if successful_executions > 0 else 0
    
    return percentage_successful, average_iterations

if __name__ == "__main__":
    PATH_BASE = os.path.dirname(os.path.dirname(__file__))
    PATH_SOURCE = os.path.join(PATH_BASE, "Datos")
    FILE_NAME = 'hojas.csv'
    FILE_PATH = os.path.join(PATH_SOURCE, FILE_NAME)
    
    try:
        df = load_data(FILE_PATH)
        X_scaled, y = preprocess_data(df)
        percentage_successful, average_iterations = run_multiple_trainings(X_scaled, y)
        
        print(f"Porcentaje de ejecuciones exitosas: {percentage_successful}")
        print(f"Promedio de iteraciones en ejecuciones exitosas: {average_iterations}")

    except FileNotFoundError:
        print(f'No existe el archivo {FILE_PATH}')
    except NotADirectoryError:
        print(f'La ruta no es un directorio {PATH_SOURCE}')
