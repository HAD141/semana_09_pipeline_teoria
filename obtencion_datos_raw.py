import os
import pandas as pd

# url de donde voy a descargar el dataset
url = 'https://drive.google.com/uc?id=1KhPl1gaejgxmm5GNTRu3fVqKjIkLlA91ql5fZMT1wjs'
# levanto el dataset
data = pd.read_csv(url)
# verificamos si existe el directorio "dataset"
if not os.path.exists("dataset"):
  # sino existe lo creamos
  os.makedirs("dataset")
# guardamos el archivo con el path "dataset/forecast_raw.csv"
data.to_csv('dataset/forecast_raw.csv', index=False)
