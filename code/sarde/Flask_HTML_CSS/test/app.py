from flask import Flask, render_template
from jsondb import JsonDB


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/todo/')
def todo():
    # database = JsonDB('db.json')
    #print('database!!!!!!!!!', database)
    # database.load()
    # the_thing = database.get('todos')
    # print(the_thing)

    #a_string = 'abcdefgh'
    return render_template('index.html')


app.run(debug=True)
