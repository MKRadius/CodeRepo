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
    city_name = input("Enter city name (Input nothing to exit): ")
    if city_name == "":
        break
    request = "https://api.openweathermap.org/data/2.5/weather?q=" + str(city_name) + "&appid=e5ffc7d7fbfe9285e108756cb60ec915"

    print("What unit of measurement do you want to use?")
    print("1. Standard (K)")
    print("2. Metric   (°C)")
    print("3. Imperial (°F)")
    unit = input("Input (1/2/3): ")

    if unit == "1":
        temp_unit = "K"
        velocity_multiplication = 3.6
        speed_unit = "km/h"
    elif unit == "2":
        request += "&units=metric"
        temp_unit = "°C"
        velocity_multiplication = 3.6
        speed_unit = "km/h"
    elif unit == "3":
        request += "&units=imperial"
        temp_unit = "°F"
        velocity_multiplication = 2.24
        speed_unit = "mph"


    
    response = requests.get(request).json()

    weather_info["main_weather_condition"] = response["weather"][0]["main"]
    weather_info["weather_decription"]      = response["weather"][0]["description"]

    weather_info["temp"]        = response["main"]["temp"]
    weather_info["feels_like"]  = response["main"]["feels_like"]
    weather_info["temp_min"]    = response["main"]["temp_min"]
    weather_info["temp_max"]    = response["main"]["temp_max"]
    weather_info["pressure"]    = response["main"]["pressure"]
    weather_info["humidity"]    = response["main"]["humidity"]

    weather_info["wind_speed"]       = str(round(int(response["wind"]["speed"]) * velocity_multiplication, 2))

    #print(json.dumps(weather_info, indent = 2))

    print("Weather in " + city_name)
    print("")
    print(f"{weather_info['main_weather_condition']} ({weather_info['weather_decription']})")
    print(f"Temperature: {round(weather_info['temp'])}{temp_unit} (Min: {round(weather_info['temp_min'])}{temp_unit} - Max: {round(weather_info['temp_max'])}{temp_unit})")
    print("Humidity: " + str(weather_info["humidity"]) + "%")
    print("Pressure: " + str(int(weather_info["pressure"]) / 1000) + "hPa")
    print("Wind speed: "+ str(weather_info["wind_speed"]) + speed_unit)
    print("")
