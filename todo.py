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


@app.route('/', methods=['GET', 'POST'])
def index():
    
    db = JsonDB('db.json')
    db.load()
    list_of_dicts = db.get('todos', 0)
    # list_of_dicts += 1
    # y = db.set('x', list_of_dicts)
    the_string = {'key': 'value'}
    print(list_of_dicts)
    # print(y)
    if request.method == 'POST':
        response = dict(request.form)
        full_list = list_of_dicts.append(response)
        print(list_of_dicts)
        db.save()
        print(response)

        # db.set("todo-item", )
        return redirect('/')
    
    return render_template('todo.html', list_of_dicts=list_of_dicts)


app.run(debug=True)