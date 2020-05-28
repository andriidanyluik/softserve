import pyowm

owm = pyowm.OWM('5b626cfbc81840ed25df6235c8313d7d')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
user_city = input("Введіть місто у якому потрібно дізнатись погоду! ")
observation = owm.weather_at_place(user_city)
w = observation.get_weather()
#print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(f"Speed wind:{w.get_wind()['speed']} km/hours")
print(f"huminidy: {w.get_humidity()} humidity")
print(f"temperature: {w.get_temperature('celsius')['temp']} celsius")

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)