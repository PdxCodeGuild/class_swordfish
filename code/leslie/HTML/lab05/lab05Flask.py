from flask import Flask, render_template, request
app = Flask(__name__)



# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!!</p>"

nums = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        distance = request.form['input_distance']
        print("Your distance: ", distance)
        nums.append(distance)
        inch_to_meter = float(distance)/(39.37)
        foot_to_meter = float(distance)/(3.281)
        yard_to_meter = float(distance)/(1.094)
        miles_to_meters = float(distance) * (1609)
        kilometers_to_meters = float(distance) * (1000)
        
        if request.form['units'] == "inches":            
            print(inch_to_meter, " in meters")
            return render_template('index.html', inch_to_meter=inch_to_meter)

        elif request.form['units'] == "feet":
            print(foot_to_meter, " in meters")
            return render_template('index.html', foot_to_meter=foot_to_meter)
            
        elif request.form['units'] == "yards":
            print(yard_to_meter, " in meters")
            return render_template('index.html', yard_to_meter=yard_to_meter)
        elif request.form['units'] == "miles":
            print(miles_to_meters, " in meters")
            return render_template('index.html', miles_to_meters=miles_to_meters)
        elif request.form['units'] == "kilometers":
            print(kilometers_to_meters, " in meters")
            return render_template('index.html', kilometers_to_meters=kilometers_to_meters)

        return render_template('index.html', distance=distance)
    return render_template('index.html')


app.run(debug=True)