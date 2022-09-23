import requests
import time
import json

response = requests.get('https://icanhazdadjoke.com/',headers={'accept': 'application/json'})

dad_joke = response.json()


print('\nHere comes a dad joke...\n')

time.sleep(2)

print(dad_joke['joke'],'\n')

time.sleep(3)

print("*badum tss*\n")