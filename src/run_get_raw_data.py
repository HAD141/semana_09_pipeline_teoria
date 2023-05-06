import os
import pandas as pd

def get_raw_data(url:str = "https://drive.google.com/uc?id=1-eyAJLxk-pQQHO9sRkQ_BFGZAuzFtPSw",
                  filename:str = "dataset/forecast_raw.csv"):
    """ Obtiene el archivo desde un repositorio en la nube y lo guarda en un
        archivo local.

    Args:
        url (str): Contiene la url de donde descargar el archivo. Defaults
            to "https://drive.google.com/uc?id=1-eyAJLxk-pQQHO9sRkQ_BFGZAuzFtPSw"
        filename (str): Contiene el path del archivo que debo guardar.
            Defaults to "dataset/forecast_raw.csv".
    """
    # levanto el dataset
    data = pd.read_csv(url)
    
    # extraemos el/los directorios
    folder = os.path.dirname(filename)
    # verificamos si existe el directorio "dataset"
    if not os.path.exists(folder):
        # sino existe lo creamos
        os.makedirs(folder, exist_ok=True)

    # guardamos el archivo con el path "dataset/forecast_raw.csv"
    data.to_csv(filename, index=False)

if __name__ == "__main__":
    get_raw_data()
