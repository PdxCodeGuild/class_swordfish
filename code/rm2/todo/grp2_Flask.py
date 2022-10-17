import datetime

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

def get_temperature():
    # request from weather api
    return 63
texts = []

# localhost:5000
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        text = request.form['text']
        print(text)
        # do whatever we want with the text
        texts.append(text)
        return redirect("/")
    current_time = datetime.datetime.now()
    temperature = get_temperature()
    nums = [1,4,25,36,49]
    return render_template('index.html', current_time=current_time, temperature=temperature, nums=nums, texts=texts)

app.run(debug=True)