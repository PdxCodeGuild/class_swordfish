'''Lab 10: Dad Joke API
'''
'''
-Use the Dad Joke API to get a dad joke and display it to the user.
-You may want to also use time.sleep to add suspense.
'''
'''Part 1
-Use the requests library to send an HTTP request to https://icanhazdadjoke.com/
-with the accept header as application/json
    -This will return a dad joke in JSON format.
-You can then use the .json() method on the response to get a dictionary
-Get the joke out of the dictionary and show it to the user.

-https://github.com/PdxCodeGuild/class_swordfish/blob/main/1%20Python/docs/15%20Requests.md
-https://github.com/PdxCodeGuild/class_swordfish/blob/main/1%20Python/labs/10%20Dad%20Joke%20API.md
'''
'''
Part 2(optional)
-Add the ability to "search" for jokes using another endpoint.
-Create a REPL that allows one to enter a search term and go through jokes one at a time
-You can also add support for multiple pages.
'''
import requests
import pprint
import time
response = requests.get(
    'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
print(response.text)  # --> type class 'str'
# {"id":"daaUfibh","joke":"Why was the big cat disqualified from the race? Because it was a cheetah.","status":200}
joke = response.json()['joke']
# --> type class 'dict
# using sleep() to hault the code execution
time.sleep(3)  # --> halting code execution for 3 seconds
print(joke)
# print(type(response.json()))
