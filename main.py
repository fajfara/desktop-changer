#!/usr/bin/env python

import os
import requests
import urllib
import urllib.request
from random import *
import datetime

# System and date varibales
background_path = '/home/fajfara/Pictures/daily-backgrounds/'
datumDanes = '{date:%Y-%m-%d}'.format( date=datetime.datetime.now())

# Weather api variables
apiKeyWeather = 'WEATHER-API-KEY'
userCity = 'Kranj'
urlW = 'https://api.openweathermap.org/data/2.5/weather?q=' + userCity + '&APPID=' + apiKeyWeather

# unsplash api key
clientId = 'UNSPLASH-API-KEY'

def changeBackground(data):
    randomPicIndex = randint(0, len(data['results']) - 1)
    download_url = data['results'][randomPicIndex]['urls']['full']
    filename = 'ozadje-za-dan-' + datumDanes + '-index-' + str(randomPicIndex)

    imgFile = open(background_path + filename + ".jpeg", 'wb')
    imgFile.write(urllib.request.urlopen(download_url).read())
    imgFile.close()
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/fajfara/Pictures/daily-backgrounds/"+ filename + ".jpeg")
    print("Check:" + background_path + filename)





# weather api get data
rW = requests.get(urlW)
weatherData = rW.json()

# Unsplash settings
photoQuery =  weatherData['weather'][0]['main']
url = 'https://api.unsplash.com/search/photos'
parametersUnsplash = {
    'client_id': clientId,
    'query': photoQuery,
    'per_page': 30
}
r = requests.get(url, params=parametersUnsplash)

changeBackground((r.json()))


