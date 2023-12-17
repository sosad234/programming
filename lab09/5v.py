import requests

def weather_generator(cities, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather" # сайт с погодой
    for city in cities:
        response = requests.get(base_url, params={"q": city, "appid": api_key})
        data = response.json()
        yield data

# Использование генератора
api_key = "5b35fa97ec38d7d5b13eebb6ea3faf98"  # Здесь API ключ
cities = []
while True:
    city = input("Введите название города ('exit' для выхода из строки ввода): ")
    if city.lower() == 'exit':
        break
    cities.append(city)

for weather_data in weather_generator(cities, api_key):
    print(weather_data)