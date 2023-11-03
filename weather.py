# Imports
import requests
import json


# taking input of city name 
city = input("Enter city name : ")

# API 
url = f"https://api.weatherapi.com/v1/current.json?key=7a34f7ca017742d19f6160849232810&q={city}"
r = requests.get(url)

wdic = json.loads(r.text)
temp = wdic["current"]["temp_c"]
print(f"The current temp in {city} is {temp}")