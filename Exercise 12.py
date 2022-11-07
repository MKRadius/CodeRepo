#Exercise 12.1
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



#Exercise 12.2
import requests

while True:
    city_name = input("Enter city name: ")
    request = "https://api.openweathermap.org/data/2.5/weather?q=" + str(city_name) + "&appid=e5ffc7d7fbfe9285e108756cb60ec915"
    response = requests.get(request).json()

    print(response)