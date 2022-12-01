from flask import Flask, render_template
from flask import request
app = Flask(__name__)

rot13={
            "a" : "n",
            "b" : "o",
            "c" : "p",
            "d" : "q",
            "e" : "r",
            "f" : "s",
            "g" : "t",
            "h" : "u",
            "i" : "v",
            "j" : "w",
            "k" : "x",
            "l" : "y",
            "m" : "z",
            "n" : "a",
            "o" : "b",
            "p" : "c",
            "q" : "d",
            "r" : "e",
            "s" : "f",
            "t" : "g",
            "u" : "h",
            "v" : "i",
            "w" : "j",
            "x" : "k",
            "y" : "l",
            "z" : "m",
        }

@app.route('/', methods=['GET','POST'])

def index():
        
    title = 'Rot 13'
    if request.method == 'POST':

        user_input = request.form.get("input", default='')
        print(user_input)

        encoded = ''
        for char in user_input:
            encoded += rot13[char]
        print(encoded)


        return render_template('index.html', encoded=encoded )
    else:    
        return render_template('index.html',title=title)


app.run(debug=True)