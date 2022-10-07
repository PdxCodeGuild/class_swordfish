from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
            'title': "Waaaagh!",
            'author': "Warlord Dragnatz",
            'date': "December 20th, 40275",
            'body': "Weve got our Gargantz an weve got our weapons. Wot ain't we got? We aint got anyfing for target practice iz wot! So I'll tell you wot we're gonna do. Were gonna give da Humies a taste of ot metal death is wot. Wes gonna take Big Gork and Big Mork ere an wes gonna stomp Hummie!"
        }, {
            'title': "Im da best",
            'author': "Ghazghkull Thraka",
            'date': "June 8th, 41866",
            'body': "I'm da hand of Gork and Mork, dey sent me to rouse up da boyz to crush and kill cos da boyz forgot what dere ere for. I woz one of da boyz till da godz smashed me in da ead an I membered dat Orks is meant to conquer and make slaves of everyfing they dont kill."
        }, {
            'title': "best shoota",
            'author': "Nazdakka Boomsnik",
            'date': "april 30th, 40210",
            'body': "Da best shoota I eva made, dat iz. Loadza barrulz, so dat its ded shooty. Sept dat wun, cos dats da skorcha, dats burny insted. Yeah, good an propa. An da bullitz iz splosiv...dey goez boom inna fings wot youz shootin. An dat button dere...dats da best bit. Wot it duz, see, iz...iz...oh, zog. Nah, its nuffin boss. Nah, youz dont need ta see wot dat button duz...onist. Dont push it!"
        }
    ]
    return render_template('index.html', posts=posts)

app.run(debug=True)