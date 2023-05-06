import os

import pandas as pd
import pickle
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.ensemble import RandomForestRegressor
import yaml


def train(filename_dataset:str = "dataset/forecast_prepared.csv",
          model_name:str = "models/model.pickle"):
    """ Función para el entrenamiento.

    Args:
        filename_dataset (str): Contiene el nombre del archivo del dataset.
            Defaults to "dataset/forecast_prepared.csv"
        model_name (str): Contiene el nombre del archivo de pesos que
            entrenamos. Defaults to "models/model.pickle"
    """
    # levantos los parametros desde un archivo
    params = yaml.safe_load(open("params.yaml"))["train"]

    # tomo los valores del archivo de parámetros de train->...
    seed = params["seed"]
    steps = params["steps"]
    lags = params["lags"]

    # extraemos el/los directorios
    folder = os.path.dirname(model_name)
    # verificamos si existe el directorio "dataset"
    if not os.path.exists(folder):
        # sino existe lo creamos
        os.makedirs(folder, exist_ok=True)

    # levantamos los datos del archivo "dataset/forecast_prepared.csv"
    data = pd.read_csv(filename_dataset)
    # creamos los dataset de train y test
    data_train = data[:-steps]["libres"]
    data_test  = data[-steps:]["libres"]

    # creamos la clase para entrenar
    forecaster = ForecasterAutoreg(
        regressor=RandomForestRegressor(random_state=seed),
        lags=lags)
    # entrenamos el model
    forecaster.fit(y=data_train)

    # guardamos el archivo de pesos del modelo entrenado
    with open(model_name, "wb") as fd:
        pickle.dump(forecaster, fd)

if __name__ == "__main__":
    train()
