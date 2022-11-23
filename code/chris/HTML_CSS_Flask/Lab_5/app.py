from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# localhost:5000
# Simple Unit Converter

# statement = []

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        units = request.form['units']
        # print(units)
        distance = float(request.form['distance'])
        if units == 'ft':
            conversion = round(distance * 0.3048, 2)
        elif units == 'mi':
            conversion = round(distance * 1609.34, 2)
        elif units == 'km':
            conversion = round(distance * 1000, 2)
        # statement.append(units)
        return render_template('index.html', thing_to_template=conversion)
    elif request.method == "GET":
        return render_template('index.html')

app.run(debug=True)