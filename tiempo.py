from re import X
import requests
from pprint import pprint

API_key = 'f5372532ea74eb3ed4621336599fe238'
city = input('Introduce una ciudad: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_key + '&q=' + city

weather_data = requests.get(base_url).json()
x = []

def data():
    for i in weather_data:
        x.append([i,' ---> ' ,weather_data[i]])
    return x

my_list = x 
#pprint(weather_data)

for i in weather_data:
    print(i,' ---> ' ,weather_data[i])