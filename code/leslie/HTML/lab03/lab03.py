from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

posts = [
    {
        'title': "Actually, people call me Marty.",
        'author': "Marty McFly",
        'date': "November 5, 1955",
        'body': "Yeah, I think it's a major embarrassment having an uncle in prison."
    },
    {
        'title': "Doc. Look at the time, you've got less than 4 minutes, please hurry.",
        'author': "George McFly",
        'date': "November 5, 1985",
        'body': "So tell me, future boy, who's president of the United States in 1985? Crazy drunk drivers."
    },
    {
        'title': "Hey see you tonight, Pop. Woo, time to change that oil.",
        'author': "Doc Brown",
        'date': "December 5, 1975",
        'body': "Yeah Mom, we know, you've told us this story a million times. You felt sorry for him so you decided to go with him to The Fish Under The Sea Dance."
    },
    {
        'title': "Whoa, this is heavy.",
        'author': "Lorraine McFly",
        'date': "December 15, 1955",
        'body': " Oh, Marty, I almost forgot, Jennifer Parker called. "
    },
    
]

app.run(debug=True)
