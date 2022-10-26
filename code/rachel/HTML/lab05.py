from flask import Flask, render_template, request
app = Flask(__name__)

keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

answers = []

def index_value():
    position1 = keys.index(i)
    return(position1)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =="POST":
        response = user_word
        for i in user_word:
            position1 = index_value()

            if position1 >= 13:

                position2 = position1 - 13

                new_letter = keys[position2]

            else:

                position2 = position1 + 13 

                new_letter = keys[position2]

        answers = new_letter.append(i)

    return render_template('lab05.html', answers=answers)

app.run(debug=True)









# Simple version: the user could just input the word to encode.
# * web form and then project
# * This lab doesn’t require styling
# * spit results back to user using one of 2 options:
#     1. use json db from mob/group lab and replace stuff as needed
#     2. instead of redirect, render template and then pass in answer=answer