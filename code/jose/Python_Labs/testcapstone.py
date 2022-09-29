import requests
import json
import pprint
import time
import random

# response = requests.get('https://opentdb.com/api.php?amount=15&category=9&difficulty=easy', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
# results = response.json()

print("Let's play Trvia Showdown! You will play against me >:D")
time.sleep(3)
print("If you answer more correct answers than me, you win!")
time.sleep(3)
print("The higher the dificulty, the smarter you make me :p")
time.sleep(3)
print("If the trivia prompt is a statement, it is either a True or False answer")
time.sleep(3)
print('Good luck!')
time.sleep(3)


difficulty = input('Please select your level of difficulty(Easy/Medium/Hard): ').lower()
category = {'general knowledge': '9', 'books': '10', 'film': '11', 'music': '12', 'tv': '14', 
'video games': '15', 'board games': '16', 'science and nature': '17', 'computers': '18', 'mythology': '20', 
'sports': '21', 'geography': '22', 'history': '23', 'politics': '24', 'animals': '27'}
user_category = input('Please select a category from the following list:\nGeneral Knowledge\nBooks\nFilm\nMusic\nTV\nVideo Games\nBoard Games\nScience and Nature\nComputers\nMythology\nSports\nGeography\nHistory\nPolicitcs\nAnimals\n').lower()
category_number = category[user_category]

response = requests.get('https://opentdb.com/api.php?amount=15&category=' + category_number + '&difficulty=' + difficulty, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
results = response.json()
# print(results)
computer_score = ()

if difficulty == 'easy':
    computer_score = random.randint(2, 5)
elif difficulty == 'medium':
    computer_score = random.randint(3, 8)
elif computer_score == 'hard':
    computer_score = random.randint(4, 10)

user_score = (0)
questions_list = results ['results']
# print(questions_list)
for i, question in enumerate(questions_list):
    raw_question = question['question']
    question['question'].replace('&#039;', "'")             #replacing the value of &#039 to the actual string representation of '
    question['question'].replace('&quot;', '"')                                  
    print(question['question'])
    true_answer = question['correct_answer']
    false_answers = question['incorrect_answers']
    joined_vals = false_answers.extend(true_answer)
    print(joined_vals)


    # print('Your choice of answers are: \n' + question[])
    user_answer = input('Please enter your answer: ').capitalize()
    if user_answer in question['correct_answer'] or user_answer == question['correct_answer']:
        print('Survey says....')
        user_score += 1
        time.sleep(3)
        print('Correct!')
    elif user_answer != question ['correct_answer']:
        print('Survey says....')
        time.sleep(3)
        print('Incorrect =(')
        print('The correct answer/s is/are: '+ question['correct_answer'])

print('And we are now at the end! Let\'s tally up the score...')
time.sleep(3)
print("Carry the three, floor divide by 1056...")
time.sleep(3)
if user_score > computer_score:
    print("Your score is " + str(user_score))
    time.sleep(2)
    print("My score is " + str(computer_score))
    time.sleep(1)
    print('You won! Let\'s play again!')
else: 
    print("Your score is " + str(user_score))
    time.sleep(2)
    print("My score is " + str(computer_score))
    time.sleep(1)
    print('I won! Great job though! Lets play again!')
# question1 = questions_list [0]['question']

# print(question1)