import pandas as pd
import geocoder
from geopy.geocoders import Nominatim
from pandas.core.frame import DataFrame
from geopy.extra.rate_limiter import RateLimiter


accidentes = pd.read_excel('data\muertosJH.xlsx',sheet_name='Hoja1')

i=0
while i < len(accidentes):
  drc = accidentes.loc[i][14]

  direccion = drc + ", " + "Cali" + ', ' + "Valle del Cauca"
  accidentes.loc[i,'Dir_Concatenada'] = direccion
  i+=1


dataset = pd.DataFrame(accidentes)

localizador = Nominatim(user_agent = 'Geocodificador')

#Hacemos un delay para evitar que el geolocalizador nos niegue el acceso
geocode = RateLimiter(localizador.geocode, min_delay_seconds = 1)
#Creamos la localizacion y se guarda en una columna
dataset['localizacion'] = dataset['Dir_Concatenada' ].apply(geocode) 

#Obtenemos el punto
dataset['punto'] = dataset['localizacion'].apply(lambda loc: tuple(loc.point) if loc else (3.319788, -76.5255499, 0.0))

#Dividimos el punto en latitud y longitud 
dataset[['lat','long','alt']] = pd.DataFrame(dataset['punto'].tolist(), index = dataset.index)

dataset.to_csv('dataset_muertos',index=False)

nueva_data = dataset
