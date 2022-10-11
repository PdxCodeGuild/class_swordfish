import datetime
from jsondb import JsonDB
# db = JsonDB('database.json')
# db.load()
# x = db.get('x', 0)
# x += 1
# db.set('x', x)
# db.save()
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

def get_temperature():
    # request from weather api
    return 63
texts = []


@app.route('/')
def index():
    
    db = JsonDB('db.json')
    db.load()
    list_of_dicts = db.get('todos', 0)
    # list_of_dicts += 1
    y = db.set('x', list_of_dicts)
    the_string = {'key': 'value'}
    print(list_of_dicts)
    print(y)
    if request.method == 'POST':
        db.save('db.json')
        return redirect('/')
    return render_template('todo.html', list_of_dicts=list_of_dicts, the_strings=y)


app.run(debug=True)