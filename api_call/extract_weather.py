import pandas as pd
from dateutil.relativedelta import relativedelta

from weatherbit.api import Api

api_key = "a93db6d8adbe4bcd90d7bb65d3eb079b"
api = Api(api_key)

datos = pd.read_csv('baseSCL2017.csv',index_col = 0)

datos_amb = datos[['Fecha-I','SIGLADES','SIGLAORI']]
datos_amb['Fecha-I'] = pd.to_datetime(datos['Fecha-I'])

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