from weatherbit.api import Api

api_key = "a93db6d8adbe4bcd90d7bb65d3eb079b"
lat = 38.00
lon = -125.75

api = Api(api_key)

	# Set the granularity of the API - Options: ['daily','hourly','3hourly']
	# Will only affect forecast requests.
api.set_granularity('daily')

	# Query by lat/lon
forecast = api.get_forecast(lat=lat, lon=lon)

	# You can also query by city:
forecast = api.get_forecast(city="Raleigh,NC")

	# Or City, state, and country:
forecast = api.get_forecast(city="Raleigh", state="North Carolina", country="US")

# To get a daily forecast of temperature, and precipitation:
print(forecast.get_series(['temp','precip']))

	# Get daily history by lat/lon:
api.set_granularity('daily')
history = api.get_history(lat=lat, lon=lon, start_date='2018-02-01',end_date='2018-02-02')

# To get a daily time series of temperature, precipitation, and rh:
print(history.get_series('weather'))

# Get hourly history by lat/lon
api.set_granularity('hourly')
history = api.get_history(lat=lat, lon=lon, start_date='2018-02-01',end_date='2018-02-02')
	
	# To get an hourly time series of temperature, precipitation, and rh:
print(history.get_series('weather'))