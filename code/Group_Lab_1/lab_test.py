import json
from flask import Flask, render_template, request, redirect
from jsondb import JsonDB
app = Flask(__name__)

@app.route('/')
def index():
    db = JsonDB('db.json')
    db.load()
    x = db.get('todos', 0)
    the_string = 'the other world'
    return render_template('index.html', the_string=the_string, x=x)


app.run(debug=True)