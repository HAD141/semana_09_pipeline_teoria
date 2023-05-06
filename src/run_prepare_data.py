import pandas as pd
import yaml

def prepare_data(filename_raw:str = "dataset/forecast_raw.csv",
                 filename_prepared:str = "dataset/forecast_prepared.csv"):
    """ Prepara los datos para el entrenamiento.

    Args:
        filename_raw (str): Contiene el nombre del archivo con los datos raw.
            Defaults to "dataset/forecast_raw.csv".
        filename_prepared(str): Contiene el nombre del archivo donde voy a
            guardar el nuevo dataset. Defaults to "dataset/forecast_prepared.csv".
    """
    # levantos los parametros desde un archivo
    params = yaml.safe_load(open("params.yaml"))["prepare"]

    # levanto el archivo "dataset/forecast_raw.csv"
    data = pd.read_csv(filename_raw)

    # tomo el valor del archivo de parámetros de prepare->parking
    parking = params["parking"]

    # filtro la columna nombre por el valor "Easo" que sale del archivo
    #   "params.yaml"
    # borro las columnas "nombre" y "timestamp"
    # arreglo el orden del índice
    data = data.loc[data["nombre"] == parking, :]\
        .drop(["nombre", "timestamp"], axis = 1)\
        .reset_index(drop = True)

    # guardo el nuevo dataset
    data.to_csv(filename_prepared, index = False)

if __name__ == "__main__":
    prepare_data()
