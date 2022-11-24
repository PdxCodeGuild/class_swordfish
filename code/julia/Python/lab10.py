# Dad Joke API

import requests
import time 

response = requests.get('https://icanhazdadjoke.com/', headers ={'accept' : 'Application/json'})

data = response.json()

print("Joke loading...")
time.sleep(3)
print(f"\nResults: {data['joke']}")