
from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def index():
    posts = [ {'title': 'Yui Reopens',
    'author': 'Katherine Chew Hamilton',
    'date': 'March 3rd, 2022',
    'body': ''
},{
    'title': 'Paydirt, a Respectable Drinking Establishment',
    'author': 'PDX Monthly',
    'date': '2022',
    'body': 'An cocktail bar located in Northeast Portland, this bar may not have food but the location is amazing. THey are connected together with four restaurants in a small complex called "The Zipper". You can get a very spciy fried chicken sandwich from Basilisk, amazing Mexican food from Tight Tacos, delicious Korean fried chicken from Sari Ramyun, and classic pizza from Boxcar Pizza.',
},{
    'title': 'Inside Division Cocktail Bar Someday, Opening Today',
    'author': 'Alex Frane',
    'date':'January 2nd, 2020' ,
    'body':'Someday bar is locaed on fabulous Division St. in Southeast. The restaurant shares its space with three other food carts in their cozy backalley patio space.',
},{
    'title': 'Deadshot PDX: The Most Unique Cocktails in Portland',
    'author': 'Sean',
    'date': 'February 2nd, 2020',
    'body':'A unique cocktail bar with fantastic food! THe drinks are upper tier quality out of all of the cocktail lounges in Portland. Definitely a must try!' ,
}
    ]

    return render_template('webpage.html', posts=posts)

app.run(debug=True)