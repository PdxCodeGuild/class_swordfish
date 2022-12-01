from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    
    posts = [
        {
            'title': "Chillwave offal you probably haven't heard of them",
            'author': "Blogger McBlogface",
            'date': "October 14th, 2021",
            'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
        }, 
        {
            'title': "Bacon Ipsum",
            'author': "Pete Nelson",
            'date': "June 2, 2021",
            'body': "Spicy jalapeno bacon ipsum dolor amet pork bacon corned beef ham hock spare ribs. Cow biltong kevin t-bone sirloin pork boudin, ham ribeye brisket bresaola tri-tip venison shank turkey. Ball tip filet mignon biltong frankfurter t-bone cupim. Ball tip andouille bresaola chuck short loin. Hamburger pork chop salami, ham hock buffalo beef ribs drumstick biltong.",
        },
        {
            'title': "The Most Presidential Lorem Ipsum in History",
            'author': "Obama Ipsum",
            'date': "June 28, 2006",
            'body':"'If you're organizing churches,' they said, 'it might be helpful if you went to church once in a while.' And I thought, 'Well, I guess that makes sense.' No, the word is very near. And yet words on a parchment would not be enough to deliver slaves from bondage, or provide men and women of every color and creed their full rights and obligations as citizens of the United States. And next week, we'll also hear about those occasions when he's broken with his party as evidence that he can deliver the change that we need. The challenges we face require tough choices, and Democrats as well as Republicans will need to cast off the worn-out ideas and politics of the past. God bless you.",

        },
        {
            'title': "Major Keys to Success",
            'author': "Khaled Ipsum",
            'date': "July 24, 2019",
            'body' : "Learning is cool, but knowing is better, and I know the key to success. It’s on you how you want to live your life. Everyone has a choice. I pick my choice, squeaky clean. Look at the sunset, life is amazing, life is beautiful, life is what you make it. Surround yourself with angels, positive energy, beautiful people, beautiful souls, clean heart, angel. Celebrate success right, the only way, apple. How’s business? Boomin. Bless up.",
            
        },
        {

          'title': "The Coffee Ipsum...",
            'author': "Coffee Ipsum",
            'date': "March 19, 2020",
            'body': "Est caffeine, affogato, robust turkish instant, ristretto coffee shop percolator cultivar turkish. Brewed, lungo, saucer id whipped, aromatic in, cup french press ut that decaffeinated. Carajillo, froth spoon, coffee galão, white, turkish organic instant kopi-luwak aged. Dark froth, irish redeye irish, cultivar, eu cappuccino viennese arabica barista ristretto. Cup to go carajillo galão steamed rich that a caffeine redeye saucer that."

        }


    ]
    return render_template('index.html',posts=posts)
app.run(debug=True)