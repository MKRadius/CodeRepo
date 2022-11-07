#Exercise 12.1
"""
import requests

while True:
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()
    joke = response["value"]
    
    print(joke)
    print("Another joke? (Y/N)")
    answer = input("Input: ")

    if answer == "Y" or answer == "y":
        continue
    else:
        break
"""


#Exercise 12.2
import requests
import json

weather_info = {}

while True:
    city_name = input("Enter city name: ")
    request = "https://api.openweathermap.org/data/2.5/weather?q=" + str(city_name) + "&appid=e5ffc7d7fbfe9285e108756cb60ec915&units=metric"
    response = requests.get(request).json()

    weather_info["main_weather_condition"] = response["weather"][0]["main"]
    weather_info["weather_decription"]      = response["weather"][0]["description"]

    weather_info["temp"]        = response["main"]["temp"]
    weather_info["feels_like"]  = response["main"]["feels_like"]
    weather_info["temp_min"]    = response["main"]["temp_min"]
    weather_info["temp_max"]    = response["main"]["temp_max"]
    weather_info["pressure"]    = response["main"]["pressure"]
    weather_info["humidity"]    = response["main"]["humidity"]

    weather_info["wind_speed"]       = str( int(response["wind"]["speed"]) * 3.6)

    #print(json.dumps(weather_info, indent = 2))

    print("Weather in " + city_name)
    print("")
    print(f"{weather_info['main_weather_condition']} ({weather_info['weather_decription']})")
    print(f"Temperature: {weather_info['temp']} (Min: {weather_info['temp_min']} - Max: {weather_info['temp_max']})")
    print("Humidity: " + str(weather_info["humidity"]) + "%")
    print("Pressure: " + str(int(weather_info["pressure"]) / 1000) + "hPa")
    print("Wind speed: "+ str(weather_info["wind_speed"]) + "km/h")
