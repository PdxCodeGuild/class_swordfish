from jsondb import JsonDB
from flask import Flask, render_template, json
app = Flask(__name__)
# Next, write a Flask app that uses the JsonDB class
# to load the database
# and render a template containing the information.


# @app.route('/')
# def index():
#     return 'Hello World!'


@app.route('/')
def index():
    database = JsonDB('db.json')
    #print('database!!!!!!!!!', database)
    database.load()
    the_thing = database.get('todos')
    # print(the_thing)

    #a_string = 'abcdefgh'
    return render_template('labgroup.html', the_thing=the_thing)


app.run(debug=True)
