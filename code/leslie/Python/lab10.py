import requests


response = requests.get('https://icanhazdadjoke.com/', headers = {'Accept': 'application/json'}, params={'User-Agent': '(https://github.com/PdxCodeGuild/class_swordfish/code/leslie)'})

the_joke = response.json()["joke"]
print(the_joke)


