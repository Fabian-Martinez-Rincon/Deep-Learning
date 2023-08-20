import pandas as pd
data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'José'],
    'Edad': [20, 26, 18, 22],
    'Pais': ['Argentina', 'Peru', 'Brasil', 'Chile']
}

# Convertir el diccionario en un DataFrame
df = pd.DataFrame(data)

nuevo_registro = {'Nombre': 'Pablo', 'Edad': 30, 'Pais': 'Colombia'}
df2 = pd.DataFrame(nuevo_registro, df.index[-1:]+1)

df = pd.concat([df, df2])

columnas = df.columns.tolist()

df['Pais'] = df['Pais'].replace('Peru', 'Perú')

print(columnas)
print(df)