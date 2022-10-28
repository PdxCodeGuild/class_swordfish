from flask import Flask
app = Flask(__name__)



from flask import Flask
app = Flask(__name__)

# localhost:5000
@app.route('/')
def index():
    return 'you\'re home'

# localhost:5000/path1/
@app.route('/path1/')
def path1():
    return 'you\'re at path 1'

# localhost:5000/path2/
@app.route('/path2/')
def path2():
    return 'you\'re at path 2'

# localhost:5000/path2/path3/
@app.route('/path2/path3/')
def path3():
    return 'you\'re at path 3'

@app.route('/')
def index():
    return 'Hello World!'

app.run(debug=True)    