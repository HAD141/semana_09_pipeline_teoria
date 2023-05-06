import json
import os
import pandas as pd
import pickle
import sklearn.metrics as metrics
import yaml

def evaluate(metrics_file:str = "metrics.json",
             filename_dataset:str = "dataset/forecast_prepared.csv",
             model_name:str = "models/model.pickle"):
    """ Función para evaluar el model

    Args:
        metrics_file (str): Nombre del archivo donde se guardan la métricas.
            Defaults to "metrics.json"
        filename_dataset (str): Contiene el nombre del archivo del dataset.
            Defaults to "dataset/forecast_prepared.csv"
        model_name (str): Contiene el nombre del archivo de pesos que
            entrenamos. Defaults to "models/model.pickle"
    """

    # extraemos el/los directorios
    folder = os.path.dirname(metrics_file)
    # verificamos si existe el directorio "dataset"
    if len(folder) > 0 and not os.path.exists(folder):
        # sino existe lo creamos
        os.makedirs(folder, exist_ok=True)

    # levantos los parametros desde un archivo
    params = yaml.safe_load(open("params.yaml"))["train"]

    # levanto el dataset
    dataset = pd.read_csv(filename_dataset)
    # tomo los valores del archivo de parámetros de train->...
    predict_steps = params['steps']

    # levanto el archivo de pesos del entrenamiento
    with open(model_name, "rb") as f:
        forecaster = pickle.load(f)

    # genero un dataset de evaluación del
    data_test  = dataset.sample(n=predict_steps)
    predictions = forecaster.predict(steps=predict_steps)
    # obtengo las métricas
    mae = metrics.mean_absolute_error(data_test, predictions)
    mse = metrics.mean_squared_error(data_test, predictions)
    # guargo las métricas
    with open(metrics_file, "w") as f:
        json.dump({'mae': mae, "mse": mse}, f, indent = 2)

if __name__ == "__main__":
    evaluate()
