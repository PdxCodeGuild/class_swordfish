import string
from flask import Flask, render_template, request, redirect

letters = string.ascii_lowercase
# input_string = input('Enter a string: ').lower()
# rot = int(input('Enter rotation (1-26): '))

def encode(x, rot):
    message = [letters[(letters.index(i) + rot) % len(letters)] if i in letters else i for i in x] # is this too dense?
    message = ''.join(message)
    return message

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        rot = int(request.form['rot'])
        text = request.form['text'].lower()
        encoded_text = encode(text, rot)
        return render_template('index.html', encoded_text = encoded_text)
    return render_template('index.html')

app.run(debug=True)