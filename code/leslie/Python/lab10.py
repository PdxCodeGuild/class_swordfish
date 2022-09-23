import requests
import pprint

#response = requests.get('https://icanhazdadjoke.com/', headers = {'Accept': 'application/json'}, params={'User-Agent': '(https://github.com/PdxCodeGuild/class_swordfish/code/leslie)'})

#the_joke = response.json()["joke"]
#print(the_joke)


while True:
    jokes_keyword = input("What would you like to see jokes about?: ")
    response = requests.get('https://icanhazdadjoke.com/search', headers = {'Accept': 'application/json'}, params={'User-Agent': '(https://github.com/PdxCodeGuild/class_swordfish/code/leslie)', 'limit': 3, 'term': jokes_keyword})

    results = response.json()
    print(results)
    pprint.pprint(results)