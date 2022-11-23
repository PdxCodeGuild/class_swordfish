# Dad Joke API

import requests
import json
import time 

time.sleep(3)

response = requests.get('https://icanhazdadjoke.com/', headers ={'accept' : 'Application/json'})

def dadjoke(response):
    if response == 200:
        

