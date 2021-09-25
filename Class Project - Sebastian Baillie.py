# Sebastian Baillie
# September 24, 2021
# Weather API Class Project

import requests
import json

def printWeatherInfo(weatherJSON):
    print("\nCurrent weather data for " + weatherJSON["name"] + ":")
    print("Current Temp: \t" + str(weatherJSON["main"]["temp"]))
    print("Today's High: \t" + str(weatherJSON["main"]["temp_max"]))
    print("Today's Low: \t" + str(weatherJSON["main"]["temp_min"]))
    print("Humidity: \t" + str(weatherJSON["main"]["humidity"]))
    print("Windspeed: \t" + str(weatherJSON["wind"]["speed"]))
    print()

if __name__ == "__main__":
    isRunning = True
    while True:
        # Asks user to input city or zip code
        place = input("Please enter the city or zip code you would like get weather information for: ")
        # My API token that was given by openweathermap
        apiKey = "ead79b169f02f08408e034d2b7a3a1e6"

        try:
            # requests weather data from website using above variables
            response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + place + '&appid=' + apiKey + "&units=imperial")
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        # puts the json dictionary into a var 'weatherInfo'
        weatherInfo = response.json()
        # Prints all necessary information in a readable format
        printWeatherInfo(weatherInfo)

        # asks if user will like to enter a new location
        userResponse = input("Would you like to enter a new location? (yes/no)")
        if userResponse == 'no' or userResponse == 'n':
            print("Goodbye!")
            exit()
