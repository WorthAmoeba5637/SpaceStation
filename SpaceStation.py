# Name: Cooper Irish
# Date: 12/11/2025
# Period: 4
# Lab: SpaceStation.py
# Description: Students use web services to gather and process live data from the internet.
#
#     Style - Code format, whitespace and PEP-8 style is followed making code easy to read.
#     Comments - Blocks of code are well commented, every function has a descriptive comment.
#     Tests -   The program runs as described in the specifications without errors(passes all tests).
#

import json  # to interpret JSON data from a web service
import urllib.request  # to load data from a specific web service api
import turtle  # for images
import time # for time

# TODO: Step 1 Who is in space?
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('There are' ,result['number'], 'People in Space')
print('They are:')
for i in result['people']:
    print('\t',i['name'], 'on the', i['craft'])
    
# TODO: Step 2 Where is the ISS?
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print("Latitude:", lat)
print("Longitude:", lon)

screen = turtle.Screen()
screen.setup(1280,640)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon),float(lat))
# TODO: Step 5 How could you make the program more interactive?
# Click for new overhead location?
# Ask User for location for overhead location?
# Make the program update automatically?

# use screen.mainloop() to keep the window open
screen.mainloop()