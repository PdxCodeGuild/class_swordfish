import datetime

from flask import Flask, render_template
app = Flask(__name__)

def get_temperature():
    # request from weather api
    return 63

# localhost:5000
@app.route('/')
def index():
    current_time = datetime.datetime.now()
    temperature = get_temperature()
    nums = [1,4,25,36,49]
    return render_template('index.html', current_time=current_time, temperature=temperature, nums=nums)

app.run(debug=True)