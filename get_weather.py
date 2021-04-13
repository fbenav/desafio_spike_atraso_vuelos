import pandas as pd
from dateutil.relativedelta import relativedelta

from weatherbit.api import Api

api_key = "a93db6d8adbe4bcd90d7bb65d3eb079b"
api = Api(api_key)


datos = pd.read_csv('baseSCL2017.csv',index_col = 0)

datos_amb = datos[['Fecha-I','SIGLADES','SIGLAORI']]
datos_amb['Fecha-I'] = pd.to_datetime(datos['Fecha-I'])

datos_amb.nunique()
len(datos_amb.drop_duplicates())

########################################################################################
# hay 67.397 comb difernetes de fecha, origen, destino                                 # 
# hay 53.252 comb diferentes de fecha, origen                                          #
# (recordemos que el origen esta fijo y coincide con el numero de fechas diferentes)   #
#                                                                                      #  
#                                                                                      #
# Si queremos tener todas las combinaciones de climas para fecha,origen,destino,       #
# es decir (2020-03-01 23:00:00, nublado, soleado), necesitamos realizar un            #
# total de 67.397 + 53.252 = 120.649 consultas a alguna API.                           #   
########################################################################################

# La api de openweathermap.org permite realizar 1M de consultas diarias, limitadas
# a 60 consultas por minuto, PERO, para obtener la data historica hay que pagar:
#
#
# *Only for Starter and Medium plans:* The maximum historical data depth 
#  in one API response is one week.
###################################################################################

#La api de weatherbit.io permite realizar 500 consultas diarias, sin limitaciones
#que nos impidan calcular el dato para una observacion, pero como calculamos
#arriba, no es suficiente para obtener todos los datos que necesitamos en el
#periodo que tenemos disponible.
###################################################################################

# Para la api de weatherbit.io utilizamos el siguiente codigo:
# (el codigo es funcional, pero exede el numero de consultas)

testeo = True

if testeo:
    test = datos_amb['Fecha-I'].loc[0]
    
    start = str(test.date())
    end   = str(test.date()+ relativedelta(days = 1))
    
    api.set_granularity('hourly')
    #history = api.get_history(city="Santiago",country="CL", start_date= '2017-01-01', end_date= '2017-01-02')
    history = api.get_history(city="Santiago",country="CL", start_date= start, end_date= end)
    
    	
    # To get an hourly time series of temperature, precipitation, and rh:
    a = pd.io.json.json_normalize(history.get_series('weather'))
    aa = a[a['datetime'] == test.replace(microsecond=0, second=0, minute=0)]
    clima = aa['weather.description'].iloc[0]
    
    print(history.get_series('weather'))
    print("")
    print(clima)


def get_weather(fecha):
    start = str(fecha.date())
    end   = str(fecha.date()+ relativedelta(days = 1))
    
    api.set_granularity('hourly')
    #history = api.get_history(city="Santiago",country="CL", start_date= '2017-01-01', end_date= '2017-01-02')
    history = api.get_history(city="Santiago",country="CL", start_date= start, end_date= end)
    
    	
    # To get an hourly time series of temperature, precipitation, and rh:
    a = pd.io.json.json_normalize(history.get_series('weather'))
    aa = a[a['datetime'] == test.replace(microsecond=0, second=0, minute=0)]
    clima = aa['weather.description']
    
    return clima

#cortamos para no exceder el numero de consultas a la appy
datos_sample = datos_amb.iloc[0:400]

datos_sample['weather'] = datos_sample['Fecha-I'].apply(get_weather)