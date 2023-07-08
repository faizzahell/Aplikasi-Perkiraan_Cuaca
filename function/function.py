import requests
from googletrans import Translator
from dotenv import load_dotenv
import os

def getWeather(city):

  load_dotenv()

  CITY_NAME = city
  API_KEY = os.getenv('API_KEY')
  URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"

  response = requests.get(URL, timeout=1)

  if response.status_code == 200:
    weather = response.json()['weather'][0]['description']
    temprature = response.json()['main']['temp']
    humidity = response.json()['main']['humidity']
    wind = response.json()['wind']['speed']

    def translate_text(text, target_lang='id'):
        translator = Translator(service_urls=['translate.google.com'])
        translation = translator.translate(text, dest=target_lang)
        return translation.text
      
    text_to_translate = weather
    weatherTranslate = translate_text(text_to_translate).title()
    
    tempratureCelcius = f"{temprature - 273.15:.2f}" + " °C"
    humidityCity = f"{humidity}" + " %"
    windSpeed = f"{wind * 3.6:.2f}" + " km/h"
  
    return (tempratureCelcius, weatherTranslate, humidityCity, windSpeed)

  else:
    print('Kota tidak ditemukan.')