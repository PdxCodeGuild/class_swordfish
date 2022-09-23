import requests
import json
import pprint
import time
import re

response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

results = response.json()
# print(results)
joke = results['joke']

joke_line = re.split('[?]', joke)                   #seperated the joke lines by creating a list of both

print(f"{joke_line[0]+'?'}")                        #printing the joke's first line here
time.sleep(3)                                       #delaying the punnchline by 3 seconds
print(joke_line[1])                                 #printing out the punchline after the time delay


# time.sleep(6)
# pprint.pprint(joke)

