from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
            'title': "What do we do now? The Alien Invation.",
            'author': "Rockcandy Clutterbuck",
            'date': "November 3rd, 1908",
            'body': "The ladies always say Khaled you smell good, I use no cologne. Cocoa butter is the key. To succeed you must believe. When you believe, you will succeed. We don’t see them, we will never see them. In life you have to take the trash out, if you have trash in your life, take it out, throw it away, get rid of it, major key. You should never complain, complaining is a weak emotion, you got life, we breathing, we ABDUCTED....",
        },
        {
            'title': "The empire has fallen!  You won't believe to who!",
            'author': "Julia Seaver",
            'date': "August 24th, 150",
            'body': "Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris. Hi mindless mortuis soulless creaturas, imo evil stalking monstra adventus resi dentevil vultus comedat cerebella viventium. Qui animated corpse, cricket bat max brucks terribilem incessu zomby. The voodoo sacerdos flesh eater, suscitat mortuos comedere carnem virus. Zonbi tattered for solum oculi eorum defunctis go lum cerebro. Nescio brains an Undead zombies. Sicut malus putrid voodoo horror. SPOILER ALERT (it was the goths)...",
        },
        {
            'title': "Brews, Beards, and Breasts! Witching guide for dating.",
            'author': "Broom Broom Luis",
            'date': "October 31, 2076",
            'body': "Et instant id single origin, cream irish, decaffeinated, kopi-luwak turkish crema iced, americano, filter chicory shop sit sweet single origin french press. Carajillo arabica caramelization crema extra  strong, cappuccino et, white redeye, a espresso americano crema variety mazagran, cup irish con panna caramelization mazagran breve body froth. Aftertaste con panna a, skinny aromatic that, medium frappuccino doppio, eu, trifecta grounds, whipped, half and half instant beans aromatic single shot. Wings, macchiato shop est, latte organic, grounds, turkish, aroma con panna, half and half that galão brewed con panna wings arabica, rich, affogato dark rich grinder filter. Skinny organic barista, percolator americano, iced foam qui crema, cappuccino cup organic flavour bar  caffeine americano that. Half and half, crema pumpkin spice est instant robusta doppio barista, coffee aromatic americano, crema, affogato roast saucer percolator qui cup cortado saucer shop. Milk white decaffeinated, rich crema aged so, viennese organic, flavour body qui strong foam in kopi-luwak.",
        },
        {
            'title': "Plain, Plane, & Plane. A DIY guide to fields, aircraft, & levels of existance.",
            'author': "I am a gitty goat",
            'date': "October 6th, 2022",
            'body': "Might want to play a bit hard to get. Well that's easy to remember. 0118 999 88199 9119 725! ... 3! If anyone was ever rude to me, I used to carry their food around in my trousers. Oh my God! Before you brought it to their table? No, after! Of course, before! Why would I do it after? Unbelievable! Some idiot disabled his firewall, meaning all the computers on Seven are teeming with viruses, plus I've just had to walk all the way down the motherfudging stairs, because the lifts are broken AGAIN! A gay musical, called Gay. That's quite gay. Gay musical? Aren't all musicals gay? This must be, like, the gayest musical ever. No, no, that's the music you heard when it come on. I'll put this with the rest of the fire....",
        }]
        
    return render_template('index.html', posts = posts)

app.run(debug=True)