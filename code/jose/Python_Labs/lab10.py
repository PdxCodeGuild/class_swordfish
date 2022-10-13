import requests
import json
import pprint
import time
import re

response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

results = response.json()
# print(results)
jokes = results['joke']                 #can print here with a joke from the web
joke = jokes.split('?')                 # Trying to split up the jokes here by punctuation
print(joke[0])                                  
time.sleep(3)
if len(joke) > 1:
    line_of_joke = str(joke[1::].pop())         #printing out the joke with a delay given the length of the joke lines in the text
    print(line_of_joke)

# time.sleep(6)
# pprint.pprint(joke)

