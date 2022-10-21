from flask import Flask, json, render_template, request
import json
import string
import random

app = Flask(__name__)


@app.route('/')
def home():
    app.logger.info(f'request /')
    return render_template("index.html")


def GeneratePassword(pass_len):
    printable_chars = string.printable[:-2]
    for r in ['\t','\n','\r',' ']:
        printable_chars = printable_chars.replace(r,'')
    random_chars = random.sample(printable_chars, pass_len)
    return ''.join(random_chars)


@app.route('/generated_password', methods=["POST"])
def GenerateRequest():
    if request.method == "POST":
        try:
            pasword_length = int(request.json['length'])
            password = GeneratePassword(pasword_length)
            data = {
                "password" : password
            }
        except:
            data = {
                'password' : False,
            }
        return json.dumps(data)

app.run(debug=True)