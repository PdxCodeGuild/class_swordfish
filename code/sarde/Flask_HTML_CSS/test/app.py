from flask import Flask, render_template
from jsondb import JsonDB


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/todos/')
def todos():
    db = JsonDB('db.json')
    print('database!!!!!!!!!', db)
    # [{'text': 'walk the dog', 'priority': 'high'}, {'text': 'butter the cat', 'priority': 'medium'}, {'text': 'wash dishes', 'priority': 'low'}]
    db.load()
    todos = db.get('todos')
    print('To-Do List', todos)

    return render_template('index.html', todos=todos)


app.run(debug=True)
