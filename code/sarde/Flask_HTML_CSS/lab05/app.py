from flask import Flask, render_template, request, redirect
app = Flask(__name__)

abc = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}
# print(abc)
rot_13_alphabet = {
    0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd',
    5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
    10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
    15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
    20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
    25: 'y'
}
# print(rot_13_alphabet)


# @app.route('/')
# def index():
#     return 'Hello World!'

def rotate_by_13(alphabet, rot_13_alphabet, input_string):
    rotate_13 = 13
    working_string = ''
    # iterate over letters in the alphabet list
    for letter in input_string:
        # checks for spaces
        if (letter != ' '):
            # adds + 13 to the current index
            number = (alphabet[letter] - rotate_13 + 26) % 26
            # print(number)
            # print('rot_13_alphabet[number]', rot_13_alphabet[number])
            # working_string = working_string + rot_13_alphabet[number]
            working_string += rot_13_alphabet[number]
            # print('working_string', working_string)

    return working_string


STORAGE_LIST_OBJECT = []
STORAGE_INDEX = 0


@app.route('/', methods=["GET", "POST"])
def index():
    print(STORAGE_LIST_OBJECT)
    if request.method == "POST":
        if STORAGE_LIST_OBJECT:
            STORAGE_LIST_OBJECT.pop(STORAGE_INDEX)
        # print('!!!!!!!request.form', request.form)
        user_input = request.form['user_input']
        print(user_input)

    # user_input_word = 'qbt'
    # qbt
        the_ciphered_word = rotate_by_13(abc, rot_13_alphabet, user_input)
        STORAGE_LIST_OBJECT.insert(
            STORAGE_INDEX,
            the_ciphered_word
        )
        return redirect("/")
    # the_ciphered_word = 'wjdasfjajshfjlasf'
    return render_template('lab05.html', the_ciphered_word=STORAGE_LIST_OBJECT)


app.run(debug=True)
