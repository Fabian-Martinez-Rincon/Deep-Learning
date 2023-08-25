import os
import pandas as pd

DATA = {
    'Nombre': ['Juan', 'María', 'Pedro', 'José'],
    'Edad': [20, 26, 18, 22],
    'Pais': ['Argentina', 'Peru', 'Brasil', 'Chile']
}
PATH_BASE = os.path.dirname(os.path.abspath(__file__))

PATH_PROSSED = os.path.join(PATH_BASE, "PandasEjercicio2")

PATH_SOURCE_TAB = os.path.join(PATH_PROSSED, "Ej2Tap.csv")
PATH_SOURCE_SPOT = os.path.join(PATH_PROSSED, "Ej2Spot.csv")
PATH_SOURCE_EXCEL = os.path.join(PATH_PROSSED, "Ej2Ex.xlsx")
PATH_SOURCE_JSON = os.path.join(PATH_PROSSED, "Ej2Json.json")

if not os.path.exists(PATH_PROSSED):
    os.makedirs(PATH_PROSSED, exist_ok=True)

DF = pd.DataFrame(DATA)

DF.to_csv(PATH_SOURCE_TAB,index=False,sep='\t')
DF.to_csv(PATH_SOURCE_SPOT,index=False,sep=';')
DF.to_excel(PATH_SOURCE_EXCEL)
DF.to_json(PATH_SOURCE_JSON,orient='records',lines=True) 