from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route('/operation_result/', methods = ['POST'])
def operation_result():
    Distance = request.form['Distance']
    Distance = int(Distance)
    Units = request.form['Units']
    Output = request.form['Output']
    metrics = {
    "ft" : 0.3048,
    "feet" : 0.3048,
    "foot" : 0.3048,
    "mile" : 1609.34,
    "miles" : 1609.34,
    "meter" : 1,
    "meters" : 1,
    "km" : 1000,
    "kilometer" : 1000,
    "kilometers" : 1000,
    "yard" : 0.9144,
    "yards" : 0.9144,
    "inch" : 0.0254,
    "inches" : 0.0254
    }
    total = Distance * metrics[Units]
    total_2 = total / metrics[Output]

    
    
    return render_template(
    'index.html',
    Distance=Distance,
    Units=Units,
    Output=Output,
    metrics=metrics,
    total=total,
    total_2=total_2
    )

app.run(debug=True)
