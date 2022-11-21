from jsondb import JsonDB

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


texts = []
# localhost:5000

# @app.route('/', methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         print(request.form)
#         text = request.form['text']
#         print(text)
#         texts.append(text)
#         return redirect("/")

#     return render_template('grp2_Flask.html', texts=texts)

# app.run(debug=True)

#@app.route('/', methods=['GET', 'POST'])
@app.route('/')
def index():
    db = JsonDB('db.json')
    db.load()
    list_of_dicts = db.get('todos', 0)
    #x += 1
    # db.set('x', x)
    # db.save()
    # x = db.get('todos', 0)
    y = db.set('x', list_of_dicts)
    # x += 1
    # db.set('x', x)
    the_string = {'key': 'value'}
    print(list_of_dicts)
    print(y)
    if request.method == 'POST':
        db.save('db.json')
        return redirect("/")
    return render_template('grp2_Flask.html', list_of_dicts=list_of_dicts, the_string=y)
    

app.run(debug=True)