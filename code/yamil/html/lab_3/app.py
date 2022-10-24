from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
            'title': "Basketball",
            'image': "url_for('static',filename='lebron_wade.jpg')",
            'author': "Yamil Nasser",
            'date': "October 1st, 2022",
            'body': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt dicta architecto dolorum, numquam enim fugit placeat illum temporibus voluptatem repellat quidem odio inventore sint sed vitae! Ad quia ratione similique accusamus. Fugit quo sed, repudiandae eaque nemo, ipsam eos aperiam ut voluptatem libero aliquid, impedit rem voluptatibus? Voluptatum, cumque molestias."
        },
        {
            'title': "Snowboarding",
            'image': "url_for('static',filename='snowboarding.jpeg')",
            'author': "Anthony Macias",
            'date': "October 2nd, 2022",
            'body': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt dicta architecto dolorum, numquam enim fugit placeat illum temporibus voluptatem repellat quidem odio inventore sint sed vitae! Ad quia ratione similique accusamus. Fugit quo sed, repudiandae eaque nemo, ipsam eos aperiam ut voluptatem libero aliquid, impedit rem voluptatibus? Voluptatum, cumque molestias."
        },
        {
            'title': "Football",
            'image': "url_for('static',filename='dolphins_tua.jpg')",
            'author': "Edwin Suarez",
            'date': "October 3rd, 2022",
            'body': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt dicta architecto dolorum, numquam enim fugit placeat illum temporibus voluptatem repellat quidem odio inventore sint sed vitae! Ad quia ratione similique accusamus. Fugit quo sed, repudiandae eaque nemo, ipsam eos aperiam ut voluptatem libero aliquid, impedit rem voluptatibus? Voluptatum, cumque molestias."
        },
        {
            'title': "Soccer",
            'image': "url_for('static',filename='messi_v_ronaldo.jpg')",
            'author': "Juan Jurado",
            'date': "October 4th, 2022",
            'body': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt dicta architecto dolorum, numquam enim fugit placeat illum temporibus voluptatem repellat quidem odio inventore sint sed vitae! Ad quia ratione similique accusamus. Fugit quo sed, repudiandae eaque nemo, ipsam eos aperiam ut voluptatem libero aliquid, impedit rem voluptatibus? Voluptatum, cumque molestias."
        },
    ]
    return render_template('index.html', posts=posts)


app.run(debug=True)
