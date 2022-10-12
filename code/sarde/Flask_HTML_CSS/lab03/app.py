# Install Flask framework and build route="Hello World"
from flask import Flask, render_template
app = Flask(__name__)


# Create a list of at least four dictionaries for your blog posts
posts = [
    {
        'title': "Hello & Welcome",
        'author': "Sarde Essilfie",
        'date': "October 6th, 2022",
        'body': "Buckeye Ipsum woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus."
    },
    {
        'title': "Upcoming Apple Products: M2 Pro and M2 Max chips-Macbook Pro.",
        'author': "Sarde Essilfie",
        'date': "October 7th, 2022",
        'body': "RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence."
    },
    {
        'title': "Tech For Travel: Apple Airtags",
        'author': "Sarde Essilfie",
        'date': "October 8th, 2022",
        'body': "Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio."
    },
    {
        'title': "Code With Me",
        'author': "Sarde Essilfie",
        'date': "October 9th, 2022",
        'body': "SMorrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state the union tbdbitl OH-IO script ohio carmen ohio Hagerty hall Fisher John Glenn buckeyes Lee Horvath Michael Redd the Lantern Morrill Hayes st. john's excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy river Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus woody Archie Griffin WOSU oval mirror lake horseshoe moritz scarlet gray Brutus buckeye leaf ohio state."
    }
]
print(posts)
print(type(posts))

# pass posts into template
'''
@app.route('/')
def index():
    return 'Hello World!'
'''


@app.route('/')
def index():
    blog_posts = posts
    #the_string = 'wjdasfjajshfjlasf'
    return render_template('lab03.html', blog_posts=blog_posts)
    # return render_template('lab03.html')


app.run(debug=True)

# print(posts.title)
# print(type(posts))
