import os
import requests

api_key = os.environ['weather_api']

def get_weather(city='Amsterdam', api_key=api_key):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units=metric'
    r = requests.get(url)
    content = r.json()
    list = content['list']
    with open("data.csv", "a") as file:
        for forecast in list:
            file.write(f"{city},{forecast['dt_txt']},{forecast['main']['temp']},{forecast['weather'][0]['description']}\n")

get_weather()