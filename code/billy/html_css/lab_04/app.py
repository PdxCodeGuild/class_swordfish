from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        order = request.form['input_text']
        print(order)
        # handle data here
        return render_template('index.html')
        
    return render_template('index.html')
    
app.run(debug=True)