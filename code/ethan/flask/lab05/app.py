from urllib import request
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')

@app.route('/', methods=['GET', 'POST'])
def index():
    conversion = 0
    if request.method == 'POST':

        distance = request.form['value']
        distance = float(distance)

        inputunit = request.form['start-unit']

        output = request.form['end-unit']


        if output == "feet":
            output = .3048
        elif output == "miles":
            output = 1609.34
        elif output == "meters":
            output = 1.0
        elif output == "kilometers":
            output = 1000.0


        ft = .3048
        mi = 1609.34
        m = 1.0
        km = 1000.0

        if inputunit == "feet":
            meters = distance * ft
            conversion = meters / output
            conversion = float(conversion)
        elif inputunit == "miles":
            meters = distance * mi
            conversion = meters / output
            conversion = float(conversion)
        elif inputunit == "meters":
            meters = distance * m
            conversion = meters / output
            conversion = float(conversion)
        elif inputunit == "kilometers":
            meters = distance * km
            conversion = meters / output
            conversion = float(conversion)
        
        
        
        return render_template('index.html', conversion=conversion)
    
    
    return render_template('index.html', conversion=conversion)
    

app.run(debug=True)