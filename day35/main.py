import requests


URL = 'https://api.openweathermap.org/data/2.5/onecall'

LAT = 36.544441
LON = 31.995407

API_KEY = ''

params = {
    'lat': LAT,
    'lon': LON,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

res = requests.get(url=URL, params=params)
res.raise_for_status()
data = res.json()

will_rain = False

for hour_data in data['hourly'][:12]:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella!')
