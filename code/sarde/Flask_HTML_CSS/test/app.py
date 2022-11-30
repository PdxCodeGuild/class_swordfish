from flask import Flask, render_template, redirect, request
from jsondb import JsonDB


app = Flask(__name__)


db = JsonDB('db.json')
# print('database!!!!!!!!!', db)
# [{'text': 'walk the dog', 'priority': 'high'}, {'text': 'butter the cat', 'priority': 'medium'}, {'text': 'wash dishes', 'priority': 'low'}]
db.load()

# @app.route('/')
# def index():
#     return 'Hello World!'

# http://127.0.0.1:5000/todos/


@app.route('/todos/')
def todos():
    todos = db.get('todos')
    # print('To-Do List', todos)
    return render_template('index.html', todos=todos)

# http://127.0.0.1:5000/add/


@app.route('/add/',  methods=['POST'])
def add():
    the_todo = request.form['text']
    print('new to-do', the_todo)
    # print('We are adding something')
    return redirect('/todos/')


app.run(debug=True)
