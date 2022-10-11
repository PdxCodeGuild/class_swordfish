'''
A simple JSON-based database that can be used with Flask.
Usage:
'''
from flask import Flask, render_template, request, redirect
from jsondb import JsonDB
# x = db.get('todos', 0)
# x.append(x[0])
# db.set('todos', x)
# db.save()
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    db = JsonDB('db.json')
    db.load()
    todos = db.get('todos', 0)
    if request.method=='POST':
      text = request.form['text']
      priority = request.form['priority']
      new_do = {'text':text, 'priority':priority}
      todos.append(new_do)
      db.set('todos', todos) # we were sacing 'todos' as text - should save 'todos' as todos
      db.save() 
      return redirect('/')
    return render_template('index.html', todos = todos)

app.run(debug=True)