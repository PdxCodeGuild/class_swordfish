from flask import Flask, render_template

blog_posts = [
    {
        'title': "If I can't scuba, then what's this all been about? What am I working toward?",
        'author': "Creed Bratton",
        'date': "October 14th, 2005",
        'body': "Cheat code Tekken first-person SnD isometric view paddle level design LoL Tom Clancy's Ghost Recon pervasive game backward compatible retrogaming. Grand Theft Auto III Xbox Donkey Kong publisher bundling headshot educational game. Grand Theft Auto: San Andreas Third-Person emulator charge attack Sony PlayStation genre The Legend of Zelda: Majora's Mask. Credit-feeding Street Fighter OP 1-Up Metroid Prime casual Game MOBA compulsion loop shmups frame-rate PlayStation3.",
        'image_url': r"https://th.bing.com/th/id/R.6b865ae4d37ba3894585202a0b42e5e6?rik=gynnb8xpvpk0Qw&riu=http%3a%2f%2fi.dailymail.co.uk%2fi%2fpix%2f2009%2f11%2f03%2farticle-1224900-07102480000005DC-709_634x419.jpg&ehk=BPtmobIvCGxqnh7jlNqiH294Lp8Br2Drtp7aMVG3Mkc%3d&risl=&pid=ImgRaw&r=0",
        'alt_text': "A scuba diver with a great white shark."
    },
    {
        'title': "Quality Assurance",
        'author': "Creed Bratton",
        'date': "September 27th, 2010",
        'body': "Easter eggs Kirby random encounter cheats The Legend of Zelda: Majora's Mask Dark Souls Action game NBA 2K HP. Bottomless pit Xbox 360 capture the flag 3d graphics GBA battle pass Hacker Pwn corruptor Game Boy Color SNES AI Fighting Game. Multi-tap console faceroll console touchscreen track-ball Wii Fit Tony Hawk's technology tree Street Fighter cheat code PvE respawn. Ban Wombo Combo alpha Command & Conquer Healer exploit combo.",
    },
    {
        'title': "The Grass Roots",
        'author': "Creed Bratton",
        'date': "June 29th, 1995",
        'body': "Assist floaty remorting minigame One-shot-kill ragequit FPS. Madden Uncharted BioShock PSP headshot OP GUI PlayStation 2. Metal Gear KO Puzzle Game Sidescroller indie kill stealing player versus environment level waggle. Anti-aliasing shoulder buttons difficulty sandbox PvE Borderlands God Mode Dragon Quest PvP. Emulator Battlefield unlimited ammo kart racing boss Counter-Strike CPU heat map boss MLG Red Dead Redemption Halo. Crash Bandicoot gamer screen cheat SWTOR chems Game Over cutscene Konami code AI retrogaming drop-out.",
        'image_url': "https://upload.wikimedia.org/wikipedia/en/4/44/The_Grass_Roots_-_Midnight_Confessions_single.JPG",
        'alt_text': "The Grass Roots band."
    },
    {
        'title': "That Time I Got Arrested",
        'author': "Creed Bratton",
        'date': "April 17th, 2014",
        'body': "Last hitting manic shooter non-player character Glory Seeking gank Nintendo DS 1up commonwealth animation cancel action point NFL 2K1. Boss Tekken esp cheats warrior achievements HP GG backward compatible multi-tap D-Pad adventure. Pervasive game aiming down sights hack fps Spyro spoiler Multiplayer NES PvP CPU cel-shaded secret character SNES. Hot Coffee gold sink draw distance lagger emulator KK WoW 3d graphics Madden Mario. Red Dead Redemption 2 RTS Metal Gear headshot cheat spoiler overlay aggro guard. Recoi Portal 2 GameBattles PvE remorting farming map LoL GTA Critical Hit class RPG."
    }
]
about_me = [
    {
        'header': "About Me",
        'image_url': "https://www.trbimg.com/img-5c264438/turbine/mc-xpm-2014-02-20-mc-creed-bratton-sellersville-20140220",
        'alt_text': "Creed Braton posing for a photo.",
        'body': "MOBA SWTOR quest 1up Rayman quickscope Grand Theft Auto: San Andreas Red Dead Redemption AAA. The Oregon Trail nerf Sonic the Hedgehog Tom Clancy's Ghost Recon cutscene level design tank power spike demo quicksave. Sandbox Sidescroller console main quest rapid-fire Game Shark spoiler patch. Vaporware DPS damage per second Mario Kart paddle NBA Live Super Mario Camping/Active Camping nerf.",
    }
]
top_posts = [
    {
        'header': "Top Posts",
        'post_one': "https://static3.srcdn.com/wordpress/wp-content/uploads/2020/04/creed-the-office-feature-image.jpg",
        'alt_text_one': "Creed brushing his teeth.",
        'post_two': "https://i.pinimg.com/originals/5b/3c/1e/5b3c1e3b965d2cbe7a358fa1760ad1b7.jpg",
        'alt_text_two': "Creed covered in blood.",
        'post_three': "https://allcelebritywiki.com/images/profile/1581672955_1_Creed%20Bratton%201.jpg",
        'alt_text_three': "Creed on a desk, with a guitar."
    }
]
follow_me = [
    {
        'header': "Follow Me",
        'body': "Stats FPS achievements Ratchet & Clank floaty Hit Points (HP) The Legend of Zelda Tom Clancy's Ghost Recon. Slow-down Wii Fit Dark Souls PvP drop-out split-screen multiplayer model gank."
    }
]
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template("lab_03_blog.html", list_in_template=blog_posts, about_me_template=about_me, top_posts_template=top_posts, follow_me_template=follow_me)

app.run(debug=True)

