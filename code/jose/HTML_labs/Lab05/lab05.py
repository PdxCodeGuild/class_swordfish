import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

def unit_conversion(user_units, user_distance, desired_units):
    """converts units to user desired. Takes two arguments, user unit (x) and user distance (y) for (x, y)"""
    conversion_values = { 'feet': 0.3048,
    'miles': 1609.34, 
    'meters': 1, 
    'kilometers': 1000,
    'yards': 0.9144,
    'inches': 0.0254 
    }

    conversion_values_meters = {'feet': 3.2808399,
    'miles': .00621,
    'kilometers': .001,
    'yards': 1.0936133,
    'inches': 39.3700787,
    'meters': 1
    }
    if user_units == 'feet':
        userunits_meters = user_distance * conversion_values['feet']
    elif user_units == 'miles':
        userunits_meters = user_distance * conversion_values['miles']
    elif user_units == 'kilometers':
        userunits_meters = user_distance * conversion_values['kilometers']
    elif user_units == 'yards':
        userunits_meters = user_distance * conversion_values['yards']
    elif user_units == 'inches':
        userunits_meters = user_distance * conversion_values['inches']
    elif user_units == 'meters':
        userunits_meters = user_distance * conversion_values['meters']
    final_converted_units = userunits_meters * conversion_values_meters[desired_units]
    return final_converted_units

converted_units = ''

# @app.route('/product/<name>')
# def get_product(name):
#   return "The product is " + str(name)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('lab05.html')
    else:
        #getting info from user to process and send back a response
        response = request.form
        user_distances = response['numbers']
        user_distance = int(user_distances)
        user_units = response['unit type']
        desired_units = response['desired units']
        converted_units = unit_conversion(user_units, user_distance, desired_units)

        print(response)
        print(user_distance)
        print(user_units)
        print(converted_units)
        return render_template('lab05.html', converted_units=converted_units)


    

    # return render_template('lab05.html', converted_units=converted_units)







app.run(debug=True)



# def unit_conversion(user_units, user_distance):
#     conversion_values = { 'feet': 0.3048,
#     'miles': 1609.34, 
#     'meters': 1, 
#     'kilometers': 1000,
#     'yards': 0.9144,
#     'inches': 0.0254 
#     }

#     conversion_values_meters = {'feet': 3.2808399,
#     'miles': .00621,
#     'kilometers': .001,
#     'yards': 1.0936133,
#     'inches': 39.3700787
#     }
#     if user_units == 'feet':
#         userunits_meters = user_distance * conversion_values['feet']
#     elif user_units == 'miles':
#         userunits_meters = user_distance * conversion_values['miles']
#     elif user_units == 'kilometers':
#         userunits_meters = user_distance * conversion_values['kilometers']
#     elif user_units == 'yards':
#         userunits_meters = user_distance * conversion_values['yards']
#     elif user_units == 'inches':
#         userunits_meters = user_distance * conversion_values['inches']
#     elif user_units == 'meters':
#         userunits_meters = user_distance * conversion_values['meters']

#     final_converted_units = userunits_meters * conversion_values_meters[desired_units]
#     print ('Your new units are ' + str(final_converted_units) + str(desired_units))