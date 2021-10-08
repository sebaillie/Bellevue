# Sebastian Baillie
# October 8, 2021
# Weather API Class Project
from tkinter import *
from functools import partial

import requests
import json
import tkinter as tk
import time

apiKey = "ead79b169f02f08408e034d2b7a3a1e6"

# startMsg created using "figlet" command on Linux
startMsg = """             __        __   _                            _         
             \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___ _ 
              \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ (_)
               \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
                \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___(_)
                                                                   
          __        __         _   _               _  _     _    _ _ 
          \ \      / /__  __ _| |_| |__   ___ _ __| || |   / \  | | |
           \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__| || |_ / _ \ | | |
            \ V  V /  __/ (_| | |_| | | |  __/ |  |__   _/ ___ \| | |
             \_/\_/ \___|\__,_|\__|_| |_|\___|_|     |_|/_/   \_\_|_|
"""

# Start menu user will see every time they start/restart program
def printStartMenu():
    print("Please select an option below to get started:")
    print("1) Start in GUI")
    print("2) Start in Command Line")
    print("3) Exit")
    return input()

###### API CALL FOR WEATHER DATA ######
def getWeatherData(place):
    try:
        # requests weather data from website using above variables
        return requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + place + '&appid=' + apiKey + "&units=imperial")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

###### PUTS WEATHER DATA INTO LIST #####
def weatherInfo(weatherJSON):
    return [weatherJSON["name"],
            str(weatherJSON["main"]["temp"]) + " F",
            str(weatherJSON["main"]["temp_max"]) + " F",
            str(weatherJSON["main"]["temp_min"]) + " F",
            str(weatherJSON["main"]["humidity"]) + "%",
            str(weatherJSON["wind"]["speed"]) + " MPH"]

# Prints all weather info for GUI mode
def startWeather(locationBar, data1, data2, data3, data4, data5, data6):
    # gets location data from search bar
    location = locationBar.get()
    # returns API call using location and API key
    response = getWeatherData(location)
    # finally gets weather info from json and puts it into a list
    weatherInfo1 = response.json()
    weatherData = weatherInfo(weatherInfo1)
    # changes labels in window to returned weather data
    data1["text"] = weatherData[0]
    data2["text"] = weatherData[1]
    data3["text"] = weatherData[2]
    data4["text"] = weatherData[3]
    data5["text"] = weatherData[4]
    data6["text"] = weatherData[5]

####### STARTS GUI MODE HERE ######
def startGUIMode():
    root = tk.Tk()
    locationBar = tk.StringVar(root)
    ####### ELEMENT SETUP FOR TKINTER ######
    # First is the search label, search bar, and search button (at the bottom)
    topLabel = Label(root, text = "Please enter a City or ZIP Code: ")
    searchBar = Entry(root, textvariable = locationBar)
    # Labels on the left
    label1 = Label(root, text = "Current weather data for: ")
    label2 = Label(root, text = "Current Temperature:  ")
    label3 = Label(root, text = "Today's High Temperature: ")
    label4 = Label(root, text = "Today's Low Temperature: ")
    label5 = Label(root, text = "Humidity: ")
    label6 = Label(root, text = "Windspeed: ")
    # Labels on the right
    data1 = Label(root, text = "XXXX")
    data2 = Label(root, text = "XXXX")
    data3 = Label(root, text = "XXXX")
    data4 = Label(root, text = "XXXX")
    data5 = Label(root, text = "XXXX")
    data6 = Label(root, text = "XXXX")
    # Search button that calls startWeather and uses 7 arguments
    searchBtn = Button(root, text = "Search", command = partial(startWeather, locationBar, data1, data2, data3, data4, data5, data6))
    # Finally the done button that closes the window and takes user to main menu.
    doneBtn = Button(root, text = "Done", command = root.destroy)
    
    ###### GRID SETUP FOR TKINTER ######
    # Using Tkinter's Grid function to easily place labels
    # First is the search label, search bar, and search button
    topLabel.grid(row = 0, column = 0, sticky = W, pady = 2)
    searchBar.grid(row = 1, column = 0, sticky = W, pady = 2)
    searchBtn.grid(row = 1, column = 1, sticky = E, pady = 2)
    # next are the 
    label1.grid(row = 2, column = 0, sticky = W, pady = 2)
    label2.grid(row = 3, column = 0, sticky = W, pady = 2)
    label3.grid(row = 4, column = 0, sticky = W, pady = 2)
    label4.grid(row = 5, column = 0, sticky = W, pady = 2)
    label5.grid(row = 6, column = 0, sticky = W, pady = 2)
    label6.grid(row = 7, column = 0, sticky = W, pady = 2)
    data1.grid(row = 2, column = 1, sticky = E, pady = 2)
    data2.grid(row = 3, column = 1, sticky = E, pady = 2)
    data3.grid(row = 4, column = 1, sticky = E, pady = 2)
    data4.grid(row = 5, column = 1, sticky = E, pady = 2)
    data5.grid(row = 6, column = 1, sticky = E, pady = 2)
    data6.grid(row = 7, column = 1, sticky = E, pady = 2)
    doneBtn.grid(row = 8, columnspan = 2)
    # Tkinter MainLoop
    root.mainloop()
    
    
##### COMMAND LINE MODE STARTS HERE ######
def startCLMode():
    while True:
        ## Put stuff here
        location = input("Please enter the city or zip code you would like get weather information for: ")
        response = getWeatherData(location)
        weatherInfo1 = response.json()
        # Prints all necessary information in a readable format
        weatherData = weatherInfo(weatherInfo1)
        printWeatherInfo(weatherData)
        # asks if user will like to enter a new location
        userResponse = input("Would you like to start over? (yes/no) ")
        if userResponse == 'yes' or userResponse == 'y':
            return
        else:
            print("Goodbye!")
            exit()

# Prints all weather info in console 
def printWeatherInfo(weatherData):
    print("\nCurrent weather data for " + weatherData[0] + ":")
    print("Current Temp: \t" + weatherData[1])
    print("Today's High: \t" + weatherData[2])
    print("Today's Low: \t" + weatherData[3])
    print("Humidity: \t" + weatherData[4])
    print("Windspeed: \t" + weatherData[5])
    print()


####### MAIN FUNCTION ######
if __name__ == "__main__":
    print(startMsg)
    while True:
        startOption = printStartMenu()
        if startOption == "1":
            startGUIMode()
        elif startOption == "2":
            startCLMode()
        elif startOption == "3":
            print("Goodbye!")
            exit()
        else:
            print("Error: Option " + startOption + " not found.\n")
            time.sleep(1)
