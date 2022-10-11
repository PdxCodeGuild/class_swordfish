from jsondb import JsonDB
db = JsonDB('db.json')
db.load()
x = db.get('x', 0)
x += 1
db.set('x', x)
db.save()
import json
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

class JsonDB:
    def __init__(self, path='db.json'):
        self.path = path
        self.data = None
    
    def load(self):
        with open(self.path, 'r') as file:
            self.data = json.loads(file.read())
    
    def save(self):
        with open(self.path, 'w') as file:
            file.write(json.dumps(self.data, indent=4, sort_keys=True))
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
    
    def clear(self, key=None):
        if key is not None:
            del self.data[key]
        else:
            self.data = {}
@app.route('/', methods=['GET', 'POST'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_form/', methods=['POST'])
def temperature():
    print(request.form) # {'person_name': 'Jane', 'person_age': 34}
    person_name = request.form['person_name'] # Jane
    person_age = request.form['person_age'] # 34
    # handle data here
    return redirect('/')

def index():
    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
        # handle data here
        return redirect('/')
    return render_template('index.html')
