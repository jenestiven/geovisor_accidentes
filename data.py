
import pandas as pd

data_heridos_opt = pd.read_csv('data\dataset_heridos.csv')
data_heridos_opt['EDAD'] = data_heridos_opt['EDAD'].replace('NS', 0)
data_heridos_opt['EDAD'] = data_heridos_opt['EDAD'].astype(float)
data_heridos_opt['EDAD'] = data_heridos_opt['EDAD'].astype(int)
#ESTADO CIVIL
data_heridos_opt['ESTADO CIVIL'] = data_heridos_opt['ESTADO CIVIL'].replace('SIN INFORMACION','NO INFO')
data_heridos_opt['ESTADO CIVIL'] = data_heridos_opt['ESTADO CIVIL'].replace('NO APLICA','NO INFO')
data_heridos_opt['ESTADO CIVIL'] = data_heridos_opt['ESTADO CIVIL'].replace('NO APLICA ','NO INFO')
data_heridos_opt['ESTADO CIVIL'] = data_heridos_opt['ESTADO CIVIL'].fillna('NO INFO')
#SERVICIO
data_heridos_opt['SERVICIO'] = data_heridos_opt['SERVICIO'].replace('NS/NR Ó SIN INFORMACIÓN','NO INFO')
data_heridos_opt['SERVICIO'] = data_heridos_opt['SERVICIO'].replace('SIN INFORMACIÓN','NO INFO')
data_heridos_opt['SERVICIO'] = data_heridos_opt['SERVICIO'].replace('PÚBLICO','PUBLICO')
data_heridos_opt['SERVICIO'] = data_heridos_opt['SERVICIO'].replace('SI','NO INFO')
data_heridos_opt['SERVICIO'] = data_heridos_opt['SERVICIO'].replace('NO APLICA','NO INFO')
data_heridos_opt['SERVICIO'] = data_heridos_opt['SERVICIO'].replace('NO APLICA ','NO INFO')
data_heridos_opt['SERVICIO'] = data_heridos_opt['SERVICIO'].fillna('NO INFO')
#AÑO
data_heridos_opt['AÑO'] = data_heridos_opt['AÑO'].replace('NS',2014)
#CONDICION VICTIMA
data_heridos_opt['CONDICION VICTIMA'] = data_heridos_opt['CONDICION VICTIMA'].replace('PEATON','PEATÓN')
#CLASE ACCIDENTE
data_heridos_opt['CLASE ACCIDENTE'] = data_heridos_opt['CLASE ACCIDENTE'].replace('CHOQUE CON OTRO VEHÍCULO','CHOQUE CON OTRO VEHICULO')
data_heridos_opt['CLASE ACCIDENTE'] = data_heridos_opt['CLASE ACCIDENTE'].replace('CHOQUE ','CHOQUE CON OBJETO FIJO O EN MOVIMIENTO')
data_heridos_opt['CLASE ACCIDENTE'] = data_heridos_opt['CLASE ACCIDENTE'].replace('CHOQUE CON OBJETO FIJO O EN MO','CHOQUE CON OBJETO FIJO O EN MOVIMIENTO')
data_heridos_opt['CLASE ACCIDENTE'] = data_heridos_opt['CLASE ACCIDENTE'].replace('CHOQUE CON OBJETO FIJO O EN MOVIMIENTO ','CHOQUE CON OBJETO FIJO O EN MOVIMIENTO')
data_heridos_opt['CLASE ACCIDENTE'] = data_heridos_opt['CLASE ACCIDENTE'].replace('CAÍDA DEL OCUPANTE','CAIDA DEL OCUPANTE')
data_heridos_opt['CLASE ACCIDENTE'] = data_heridos_opt['CLASE ACCIDENTE'].replace('SIN INFORMACION','NO INFO')

#--------------------------------------------------------------------------------------------------------
data_muertos_opt = pd.read_csv('data\dataset_muertos.csv')
data_muertos_opt['EDAD'] = data_muertos_opt['EDAD'].replace('NS', 0)
data_muertos_opt['EDAD'] = data_muertos_opt['EDAD'].astype(float)
data_muertos_opt['EDAD'] = data_muertos_opt['EDAD'].astype(int)
#SERVICIO
data_muertos_opt['SERVICIO'] = data_muertos_opt['SERVICIO'].replace('SIN INFORMACIÓN','NO INFO')
data_muertos_opt['SERVICIO'] = data_muertos_opt['SERVICIO'].replace('SIN INFORMACION','NO INFO')
data_muertos_opt['SERVICIO'] = data_muertos_opt['SERVICIO'].replace('SERVICIO PÚBLICO','PUBLICO')
data_muertos_opt['SERVICIO'] = data_muertos_opt['SERVICIO'].replace('SERVICIO PUBLICO','PUBLICO')
data_muertos_opt['SERVICIO'] = data_muertos_opt['SERVICIO'].replace('PÚBLICO','PUBLICO')
data_muertos_opt['SERVICIO'] = data_muertos_opt['SERVICIO'].fillna('NO INFO')
#ESTADO CIVIL
data_muertos_opt['ESTADO CIVIL'] = data_muertos_opt['ESTADO CIVIL'].replace('SIN INFORMACION','NO INFO')
data_muertos_opt['ESTADO CIVIL'] = data_muertos_opt['ESTADO CIVIL'].replace('NO APLICA','NO INFO')
#CONDICION VICTIMA
data_muertos_opt['CONDICION VICTIMA'] = data_muertos_opt['CONDICION VICTIMA'].replace('PEATON','PEATÓN')
data_muertos_opt['CONDICION VICTIMA'] = data_muertos_opt['CONDICION VICTIMA'].replace('SIN INFORMACIÓN','NO INFO')
data_muertos_opt['CONDICION VICTIMA'] = data_muertos_opt['CONDICION VICTIMA'].replace('SIN INFORMACION ','NO INFO')
#CLASE ACCIDENTE
data_muertos_opt['CLASE ACCIDENTE'] = data_muertos_opt['CLASE ACCIDENTE'].replace('CHOQUE CON OTRO VEHÍCULO','CHOQUE CON OTRO VEHICULO')
data_muertos_opt['CLASE ACCIDENTE'] = data_muertos_opt['CLASE ACCIDENTE'].replace('SIN INFORMACION','NO INFO')
data_muertos_opt['CLASE ACCIDENTE'] = data_muertos_opt['CLASE ACCIDENTE'].replace('NS/NR - SIN INFORMACION','NO INFO')
data_muertos_opt['CLASE ACCIDENTE'] = data_muertos_opt['CLASE ACCIDENTE'].replace('NS/NR - SIN INFORMACIÓN','NO INFO')
#-------------------------------------------------------------------------------------------------------------------------------
años_heridos = pd.read_csv('data\Años_heridos')
sexo_heridos = pd.read_csv('data\Sexo_heridos')
años_muertos = pd.read_csv('data\Años_muertos')
dias_muertos = pd.read_csv('data\Dias_muertos')
horas_muertos = pd.read_csv('data\Horas_muertos')
sexo_muertos = pd.read_csv('data\Sexo_muertos')

