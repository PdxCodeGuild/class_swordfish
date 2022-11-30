from flask import Flask, render_template, redirect, request
from jsondb import JsonDB


app = Flask(__name__)


db = JsonDB('db.json')
# print('This is my database', db)
# [{'text': 'walk the dog', 'priority': 'high'}, {'text': 'butter the cat', 'priority': 'medium'}, {'text': 'wash dishes', 'priority': 'low'}]
db.load()

# @app.route('/')
# def index():
#     return 'Hello World!'

# http://127.0.0.1:5000/todos/
priorities = ['high', 'medium', 'low']


@app.route('/todos/')
def get_todos():
    todos = db.get('todos')
    # print('To-Do List', todos)
    return render_template('index.html', todos=todos, priorities=priorities)

# http://127.0.0.1:5000/add/


@app.route('/add/',  methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # print('print')
        todos = db.get('todos')
        # print('the todos')
        todo_text = request.form['text']
        print('todo_text:', todo_text)
        todo_priority = request.form['priority']
        print('todo_priority:', todo_priority)
        todo = {
            'text': todo_text,
            'priority':  todo_priority,
        }
        todos.append(todo)
        db.set('todos', todos)
        db.save()
        print('todos:', todos)
        # print('We are adding something')
    return redirect('/todos/')
    # return render_template('index.html')


app.run(debug=True)
