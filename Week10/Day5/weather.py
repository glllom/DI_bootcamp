from pyowm.owm import OWM
from pyowm.utils import timestamps
owm = OWM('fbeca56154cfb9f74c56f39cbe6dc461')
mgr = owm.weather_manager()
mgr_air_pollution = owm.airpollution_manager()
reg = owm.city_id_registry()
city = input("Input a city: ").strip()
city_id = reg.ids_for(city, matching='exact')[0][0]
city_country = reg.ids_for(city, matching='exact')[0][2]

observation = mgr.weather_at_place(city+','+city_country)
weather = observation.weather
temperature = weather.temperature('celsius').get('temp')
wind = weather.wind().get('speed')
sunrise_time = weather.sunrise_time(timeformat='date').strftime("%H:%M")
sunset_time = weather.sunset_time(timeformat='date').strftime("%H:%M")

print(f"Current temperature in {city}: {temperature}")
print(f"Current wind speed in {city}: {wind}")
print(f"Today’s sunrise and sunset times of {city} are: {sunrise_time} and {sunset_time}")
forecast = mgr.forecast_at_place(city+','+city_country, '3h').forecast
print("Forecast today:")
for weather in forecast:
    print(weather.reference_time('date').strftime("%H:%M"), weather.status)

