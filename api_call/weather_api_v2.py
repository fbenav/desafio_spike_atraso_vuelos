from pyowm import OWM

owm = OWM('1040fe196f5c27e9130f49d9c4e1db25')  # You MUST provide a valid API key

# Search for current weather in London (Great Britain)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('London,GB')
w = observation.weather
print(w)                  # <Weather - reference time=2013-12-18 09:20, status=Clouds>

# Weather details
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)

####################################################################################
from pyowm.owm import OWM
from pyowm.utils import timestamps, formatting

owm = OWM('1040fe196f5c27e9130f49d9c4e1db25')
mgr = owm.weather_manager()

import pandas as pd
from dateutil.relativedelta import relativedelta


datos = pd.read_csv('baseSCL2017.csv',index_col = 0)

datos_amb = datos[['Fecha-I','SIGLADES','SIGLAORI']]
datos_amb['Fecha-I'] = pd.to_datetime(datos['Fecha-I'])

test = datos_amb['Fecha-I'].loc[0]

print(timestamps.yesterday())
# what is the epoch for yesterday at this time?
yesterday_epoch = formatting.to_UNIXtime(test)

one_call_yesterday = mgr.one_call_history(lat=52.5244, lon=13.4105, dt=yesterday_epoch)

observed_weather = one_call_yesterday.current