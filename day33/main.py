import requests


url = 'https://api.sunrise-sunset.org/json'

params = {
    'lat': '45.267136',
    'lng': '19.833549',
    'formatted': 0
}

res = requests.get(url=url, params=params)
res.raise_for_status()
data = res.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise, sunset)
