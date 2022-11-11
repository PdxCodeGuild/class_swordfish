import json
from flask import Flask, render_template, request, redirect
from jsondb import JsonDB
app = Flask(__name__)

@app.route('/')


@app.route('/', methods=['GET', 'POST'])
def index():
    db = JsonDB('db.json')
    db.load()
    x = db.get('todos', 0)
    if request.method == 'POST':
        db.load()
        todo_list = []
        todos = {}
        for dict in x:
            todo_list.append(dict)
        todo_text = request.form['input_text']
        print("to do:", todo_text)
        priority = request.form['priority']
        print(priority)
        todos['text'] = todo_text
        todos['priority'] = priority
        todo_list.append(todos)
        db.set('todos', todo_list)
        
        db.save()
        
        
        
        return redirect('/')
    
    
    the_string = 'the other world'
    return render_template('index.html', the_string=the_string, x=x)
    
        
        
    # db = JsonDB('db.json')
    # db.set('text', 'input_text')
    # db.save()
app.run(debug=True)
