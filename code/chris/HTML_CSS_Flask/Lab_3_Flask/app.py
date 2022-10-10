from flask import Flask, render_template
app = Flask(__name__)

# localhost:5000
# Step 1
@app.route('/')
def index():
    return 'Hello World!'

# Step 2-4
# localhost:5000/path1/
@app.route('/path1/')
def path1():
    posts = [
    { 
        'title': "The fall of Da Bears", 
        'author': "Philly M", 
        'date': "October 3rd, 2022", 
        'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu volutpat odio facilisis mauris sit amet. Aenean pharetra magna ac placerat vestibulum lectus. Libero volutpat sed cras ornare arcu dui vivamus arcu felis. Ultricies mi eget mauris pharetra et ultrices. Adipiscing commodo elit at imperdiet dui accumsan. Fringilla ut morbi tincidunt augue. Non nisi est sit amet. Et sollicitudin ac orci phasellus egestas. Id diam maecenas ultricies mi eget mauris pharetra et. Pulvinar etiam non quam lacus suspendisse faucibus interdum. Aliquam purus sit amet luctus venenatis lectus magna fringilla urna. Parturient montes nascetur ridiculus mus mauris vitae ultricies leo integer."
    }, {
        'title': "Why is Justin F. the worst Qb",
        'author': "Philly M",
        'date': "September 19th, 2022",
        'body': "Id aliquet lectus proin nibh nisl condimentum. Non arcu risus quis varius quam. Vitae nunc sed velit dignissim. Rhoncus urna neque viverra justo. Mauris augue neque gravida in. Augue ut lectus arcu bibendum. Et odio pellentesque diam volutpat commodo sed egestas egestas fringilla. Morbi quis commodo odio aenean sed. Duis ultricies lacus sed turpis tincidunt id aliquet. Dui accumsan sit amet nulla facilisi morbi tempus iaculis urna. Eget velit aliquet sagittis id consectetur purus ut faucibus. Senectus et netus et malesuada fames ac."
    }, {
        'title': "Did we just waste our #1 draft pick???",
        'author': "Philly M",
        'date': "April 30th, 2021",
        'body': "Feugiat in ante metus dictum at tempor. Pharetra vel turpis nunc eget lorem dolor sed viverra ipsum. Ut eu sem integer vitae justo eget magna. Lorem ipsum dolor sit amet consectetur adipiscing elit duis. Vitae semper quis lectus nulla at volutpat diam. Egestas dui id ornare arcu odio ut sem nulla. At auctor urna nunc id cursus metus aliquam eleifend mi. Ultricies lacus sed turpis tincidunt id aliquet risus feugiat in. Id diam vel quam elementum pulvinar etiam non quam lacus. "
    }, {
        'title': "Gosh, The Bears are horrible",
        'author': "Philly M",
        'date': "December 28th, 2020",
        'body': "Etiam erat velit scelerisque in dictum non. Sed odio morbi quis commodo odio aenean sed. Mauris in aliquam sem fringilla ut. Placerat in egestas erat imperdiet sed. Neque sodales ut etiam sit amet nisl purus in mollis. Duis ut diam quam nulla. Sed turpis tincidunt id aliquet risus feugiat in. Nibh sit amet commodo nulla facilisi nullam vehicula ipsum a. Condimentum id venenatis a condimentum vitae sapien pellentesque. Viverra adipiscing at in tellus integer feugiat scelerisque varius morbi. Neque convallis a cras semper auctor. Ipsum a arcu cursus vitae congue. Semper viverra nam libero justo laoreet sit amet cursus."
    }]
    return render_template('index.html', posts=posts)

app.run(debug=True)