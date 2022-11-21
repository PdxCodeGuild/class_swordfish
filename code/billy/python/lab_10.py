'''
program: lab_10
author: billy frick
date: 23 september 2022

function:   > this program will utilize the 'Dad Joke' API.
            > a request will be made from the https.
            > the reponse will be be returned in JSON format.
            > the user will be given a random dad joke.
'''

# imports
import requests
import time
import json

# this will send the http request and create the 'accept' header.
response = requests.get('https://icanhazdadjoke.com/',headers={'accept': 'application/json'})

# converts reponse to json and saves it as a variable.
dad_joke = response.json()

print('\nHere comes a dad joke...\n')

# delays the next print statement by 2 seconds.
time.sleep(2)

print(dad_joke['joke'],'\n')

# delays the next print statement by 3 seconds.
time.sleep(3)

print("*badum tss*\n")

# end