from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

posts = [
    {
        'title': 'Memories That You Call',
        'artist': 'ODESZA, Monsoonsiren',
        'album': 'In Return',
        'lyrics': 'Can feel your heart#Yearning slow#Can feel#Slow all the memories, that you call'
    },
    {
        'title': 'Nothing\'s Gonna Happen (Demo)',
        'artist': 'The Staves',
        'album': 'Nothing\'s Gonna Happen (Demo)',
        'lyrics':'How can I rearrange#And put it on the page#When the enemy\'s at the door?#And there\'s nothing you can do#They\'ve never seen before#And everybody knows#Nothing\'s gonna happen#With your back against the door#Could I be the only one still waiting?#I can wait some more#Tell me what happens#Will I be okay?#I can see a fire from a mile away#\'Cause nothing\'s gonna happen#With your back against the door#If I could reach you now#I\'d say that I am proud#With everything you\'ve done#And the wonderful man#I know you have become#\'Cause maybe you don\'t know#Nothing\'s gonna happen#With your back against the door#Could I be the only one still waiting?#I can wait some more#Tell me what happens#Will I be okay?#Tell me that you\'ll love me#When you\'re miles away#Nothing\'s gonna happen#With your back against the door#Loneliness is on the dawn#Loving is a lie#I saw it on the sign#It\'s a line to drag you in#It\'s false advertising#And no one wants to see#Nothing\'s gonna happen#With your back against the door#Could I be the only one still waiting?#I can wait some more#Tell me what happens#Will I be okay?#I can see a fire from a mile away#\'Cause nothing\'s gonna happen#With your back against the door#Oh#Oh#Oh#Oh#Oh, oh'
    },
    {
        'title': 'Witness Trees',
        'artist': 'Henry Jamison',
        'album': 'The Years',
        'lyrics': 'To be alone for a time, for a long time#On a road between contentments#Witness trees in a line, in a long line#Witness my resentments#Every petty little thought of mine#Where do you go, my darling?#When you do not sing#Where do you go?#And you\'ve been told#The streaks of gold#In your hair mean nothing#Oh no, not so#To be afraid for a time, for long time#That there\'s no angel watching#I see a sign in the breeze#In the wind in the trees#In the skies over Austin#Where do you go, my darling?#When you do not sing#Where do you go?#And you\'ve been told#The streaks of gold#In your hair mean nothing#Oh no, not so'
    },
    {
        'title': 'Pain',
        'artist': 'The War On Drugs',
        'album': 'A Deeper Understanding',
        'lyrics': 'Go to bed now I can tell#Pain is on the way out now#Look at the way the domino falls away#I know it\'s hard looking in#Knowing that tomorrow you\'ll be back again#Hang your head and let me in, I\'m waiting#So long#I was staring into the light#When I saw you in the distance, I knew that you\'d be mine#Am I moving back in time?#Just standing still?#I met a man with a broken back#He had a fear in his eyes that I could understand#I can\'t even shake the hand#Without breaking it#I\'ve been pulling on a wire, but it just won\'t break#I\'ve been turning up the dial, but I hear no sound#I resist what I cannot change#And I wanna find what can\'t be found#I\'m aware of the time we lost#Like a demon in the doorway, waiting to be born#But I\'m here all alone, just begging#Pull me close and let me hold you in#Give me the deeper understanding of who I am#Yeah, I\'m moving back again, I\'m waiting, yeah#I\'m just pulling on a wire, but it just won\'t break#I\'ve been turning up the dial, but I hear no sound#I resist what I cannot change, own it in your own way#Yeah, I wanna find what can\'t be found'
    }
]


app.run(debug=True)

