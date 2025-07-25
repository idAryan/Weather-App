import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
API_key=os.getenv('API_KEY')
@dataclass
class WeatherData:
    main:str
    description:str
    icon:str
    temperature:int


def get_lat_lon(city_name,state_code,country_code,API_key):
    response=requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data=response[0]
    lat,lon=data.get('lat'),data.get('lon')
    return lat,lon
def get_current_weather(lat,lon,API_key):
    response=requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&unit=metric').json()
    data=WeatherData(
        main=response['weather'][0].get('main'),
        description=response['weather'][0].get('description'),
        icon=response['weather'][0].get('icon'),
        temperature=int(response['main'].get('temp'))
    )
    return data
def main(city_name,state_code,country_code):
    lat,lon=get_lat_lon(city_name,state_code,country_code,API_key)
    weather_data=get_current_weather(lat,lon,API_key)
    return weather_data
if __name__=="__main__":
    lat,lon=get_lat_lon('Toronto','ON','CA',API_key)
    print(get_current_weather(lat,lon,API_key))

