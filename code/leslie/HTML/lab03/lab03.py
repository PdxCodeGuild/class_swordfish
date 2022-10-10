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
            'body': "Yeah, I think it's a major embarrassment having an uncle in prison. Marty, that's completely out of the question, you must not leave this house. you must not see anybody or talk to anybody. Anything you do could have serious repercussions on future events. Do you understand? Ahh. Yeah. Hey, hey, I've seen this one, I've seen this one. This is a classic, this is where Ralph dresses up as the man from space. Yeah Mom, we know, you've told us this story a million times. You felt sorry for him so you decided to go with him to The Fish Under The Sea Dance. Let's get you into a radiation suit, we must prepare to reload. Shape up, man. You're a slacker. You wanna be a slacker for the rest of your life? What did your mother ever see in that kid? I'm gonna get that son-of-a-bitch. Working."
        },
        {
            'title': "Doc. Look at the time, you've got less than 4 minutes, please hurry.",
            'author': "George McFly",
            'date': "November 5, 1985",
            'body': "Flux capacitor. My god, do you know what this means? It means that this damn thing doesn't work at all. Doc, look, all we need is a little plutonium. Lorenzo, where're you keys? What's that thing he's on? Hey Biff, check out this guy's life preserver, dork thinks he's gonna drown. Well yeah, you know we have two of them. Go. We never would have fallen in love. Your not gonna be picking a fight, Dad, dad dad daddy-o. You're coming to a rescue, right? Okay, let's go over the plan again. 8:55, where are you gonna be.So tell me, future boy, who's president of the United States in 1985? Crazy drunk drivers."
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
            'body': " Oh, Marty, I almost forgot, Jennifer Parker called. Good evening, I'm Doctor Emmet Brown, I'm standing here on the parking lot of- Alright, take it up, go. Doc. George McFly? Oh, he's kinda cute and all, but, well, I think a man should be strong, so he could stand up for himself, and protect the woman he loves. Don't you? Mom, is that you? Okay Doc, this is it. Alright, okay Jennifer. What if I send in the tape and they don't like it. I mean, what if they say I'm no good. What if they say, 'Get out of here, kid, you got no future.' I mean, I just don't think I can take that kind of rejection. Jesus, I'm beginning to sound like my old man. Well gee, I don't know. Huh? What did you sleep in your clothes again last night. I'm telling the truth, Doc, you gotta believe me."
        },        
    ]
    
            
  
    return render_template('index.html', posts=posts)

app.run(debug=True)
