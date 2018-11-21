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
apiKeyWeather = 'API'
userCity = 'Kranj'
urlW = 'https://api.openweathermap.org/data/2.5/weather?q=' + userCity + '&APPID=' + apiKeyWeather

# unsplash api key
clientId = 'UNSPLASH'

def changeBackground(data):
    randomPicIndex = randint(0, len(data['results']) - 1)
    download_url = data['results'][randomPicIndex]['urls']['full']
    filename = 'ozadje-za-dan-' + datumDanes + '-index-' + str(randomPicIndex)

    imgFile = open(background_path + filename + ".jpeg", 'wb')
    imgFile.write(urllib.request.urlopen(download_url).read())
    imgFile.close()
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/fajfara/Pictures/daily-backgrounds/"+ filename + ".jpeg")
    print("Check:" + background_path + filename)

def checkIfNightOrDay():
    now = datetime.datetime.now()
    if now.hour > 7 and now.hour < 18:
        timeOfDay = 'day'
        return timeOfDay
    else:
        timeOfDay = 'night'
        return timeOfDay

def checkFolder():
    path, dirs, files = next(os.walk(background_path))
    file_count = len(files)
    if file_count > 10:
        for the_file in os.listdir(background_path):
            file_path = os.path.join(background_path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
    else:
        return




# weather api get data
rW = requests.get(urlW)
weatherData = rW.json()

# Unsplash settings

photoQuery = weatherData['weather'][0]['main']  + ' ' + checkIfNightOrDay()
url = 'https://api.unsplash.com/search/photos'
parametersUnsplash = {
    'client_id': clientId,
    'query': photoQuery,
    'per_page': 100
}

print(parametersUnsplash['query'
                         ''])
r = requests.get(url, params=parametersUnsplash)

checkFolder()
changeBackground((r.json()))


