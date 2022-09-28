import requests
import json
import pprint
import time

response = requests.get('https://opentdb.com/api.php?amount=15&category=9&difficulty=easy', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
results = response.json()

questions_list = results ['results']
for i, question in enumerate(questions_list):
    print(question[i]['question'])
    user_answer = input('Please enter your answer: ')
    if user_answer == question[i]['correct answer']:
        print('Correct!')
    elif user_answer == question[i]['incorrect answer'] or question [i]['incorrect answers']:
        print('Incorrect =(')


# question1 = questions_list [0]['question']

# print(question1)