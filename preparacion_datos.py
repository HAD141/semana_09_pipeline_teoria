import pandas as pd
import yaml

# levantos los parametros desde un archivo
params = yaml.safe_load(open("params.yaml"))["prepare"]

# levanto el archivo "dataset/forecast_raw.csv" 
data = pd.read_csv("dataset/forecast_raw.csv")

# tomo el valor del archivo de parámetros de prepare->parking
parking = params["parking"]

# filtro la columna nombre por el valor "Easo" que sale del archivo "params.yaml"
# luego borro las columnas "nombre" y "timestamp"
# reseteo los valores del indice
data = data.loc[data["nombre"] == parking, :]\
    .drop(["nombre", "timestamp"], axis = 1)\
    .reset_index(drop = True)

# guardo el nuevo dataset
data.to_csv("dataset/forecast_preparados.csv", index = False)
