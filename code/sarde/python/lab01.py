'''
Lab 1: Unit Converter
'''
'''
Version 1
-Ask the user for the number of feet
-print equivalent distance in meters
- 1 ft is 0.3048 m.
-output = meters = multiply input distance by 0.3048
'''

'''
units = {
    'feet': 0.3048,
}
# ask user for number of feet
feet = input('What is the distance in feet?: ')
# convert feet to integer
feet = int(feet)
total = feet * units['feet']
print(f'{feet} ft is {round(total, 4)} m')
'''

'''
Version 2
-Allow the user to also enter the units
-depending on the unit, convert distance-meters
'''
units = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}
input_distance = input('What is the distance?: ')
input_unit = input('What are the units?: ')
# convert input_distance to an integer
distance = int(input_distance)
# convert input_units to an integer
unit = int(units[input_unit])
total = distance * unit
print(f'{input_distance} {input_unit} is {total} m')

'''
Version 3
-Add support for yards, and inches
-1 yard is 0.9144 m
-1 inch is 0.0254 m
'''
units = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}
input_distance = input('What is the distance?: ')
input_unit = input('What are the units?: ')
# convert input_distance to an integer
distance = int(input_distance)
# convert input_units to an integer
unit = int(units[input_unit])
total = distance * unit
print(f'{input_distance} {input_unit} is {total} m')
