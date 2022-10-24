from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
            'title': "Basketball",
            'author': "Yamil Nasser",
            'date': "October 1st, 2022",
            'body': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt dicta architecto dolorum, numquam enim fugit placeat illum temporibus voluptatem repellat quidem odio inventore sint sed vitae! Ad quia ratione similique accusamus. Fugit quo sed, repudiandae eaque nemo, ipsam eos aperiam ut voluptatem libero aliquid, impedit rem voluptatibus? Voluptatum, cumque molestias."
        },
        {
            'title': "Snowboarding",
            'author': "Anthony Macias",
            'date': "October 2nd, 2022",
            'body': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt dicta architecto dolorum, numquam enim fugit placeat illum temporibus voluptatem repellat quidem odio inventore sint sed vitae! Ad quia ratione similique accusamus. Fugit quo sed, repudiandae eaque nemo, ipsam eos aperiam ut voluptatem libero aliquid, impedit rem voluptatibus? Voluptatum, cumque molestias."
        },
        {
            'title': "Football",
            'author': "Edwin Suarez",
            'date': "October 3rd, 2022",
            'body': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt dicta architecto dolorum, numquam enim fugit placeat illum temporibus voluptatem repellat quidem odio inventore sint sed vitae! Ad quia ratione similique accusamus. Fugit quo sed, repudiandae eaque nemo, ipsam eos aperiam ut voluptatem libero aliquid, impedit rem voluptatibus? Voluptatum, cumque molestias."
        },
        {
            'title': "Soccer",
            'author': "Juan Jurado",
            'date': "October 4th, 2022",
            'body': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt dicta architecto dolorum, numquam enim fugit placeat illum temporibus voluptatem repellat quidem odio inventore sint sed vitae! Ad quia ratione similique accusamus. Fugit quo sed, repudiandae eaque nemo, ipsam eos aperiam ut voluptatem libero aliquid, impedit rem voluptatibus? Voluptatum, cumque molestias."
        },
    ]
    # name = 'bob'
    # temperature = 67
    # nums = [1, 2, 3]  
    return render_template('index.html') #name=name, temperature=temperature, nums=nums)
