from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
# def index():
#     return 'Hello World!'

def index():
    posts = [
        {
            'title': "Actually, people call me Marty.",
            'author': "Marty McFly",
            'date': "November 5, 1955",
            'body': "Yeah, I think it's a major embarrassment having an uncle in prison. Let's get you into a radiation suit, we must prepare to reload. Shape up, man. You're a slacker. You wanna be a slacker for the rest of your life? What did your mother ever see in that kid? I'm gonna get that son-of-a-bitch. Working."
        },
        {
            'title': "Doc. Look at the time, you've got less than 4 minutes, please hurry.",
            'author': "George McFly",
            'date': "November 5, 1985",
            'body': "Flux capacitor. Well yeah, you know we have two of them. Go. We never would have fallen in love. Your not gonna be picking a fight, Dad, dad dad daddy-o. You're coming to a rescue, right? Okay, let's go over the plan again. 8:55, where are you gonna be.So tell me, future boy, who's president of the United States in 1985? Crazy drunk drivers."
        },
        {
            'title': "Hey see you tonight, Pop. Woo, time to change that oil.",
            'author': "Doc Brown",
            'date': "December 5, 1975",
            'body': "Yeah Mom, we know, you've told us this story a million times. You felt sorry for him so you decided to go with him to The Fish Under The Sea Dance.I still don't understand, how am I supposed to go to the dance with her, if she's already going to the dance with you. Yeah well look, Marvin, Marvin, you gotta play. See that's where they kiss for the first time on the dance floor. And if there's no music, they can't dance, and if they can't dance, they can't kiss, and if they can't kiss, they can't fall in love and I'm history. Scram, McFly. Go. Hey beat it, spook, this don't concern you."
        },
        {
            'title': "Whoa, this is heavy.",
            'author': "Lorraine McFly",
            'date': "December 15, 1955",
            'body': " Oh, Marty, I almost forgot, Jennifer Parker called. "
        },        
    ]
    
            
  
    return render_template('index.html', posts=posts)

app.run(debug=True)
