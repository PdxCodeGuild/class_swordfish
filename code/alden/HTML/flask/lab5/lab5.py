# import numbers
# from urllib.parse import parse_qs
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form['text']
        code = list(code)
        rot = int(request.form['number'])

        final = rotation(code, rot)
        final = ''.join(final)
        return render_template('index.html', final = final)
    return render_template('index.html')

def rotation(code, rot):
    final = [alf[(alf.index(i) + rot) % len(alf)]for i in code if i in alf]
    return final
app.run(debug=True)