'''
program: lab_01
author: billy frick
date: 7 september 2022

function: this program will allow the user to enter the distance of a unit
and have it converted into meters.

'''

unit_converter = {

    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'y': 0.9144,
    'in': 0.0254
}

distance = input("\n> what is the distance? ")

distance = int(distance)

unit = input("\n> what are the input units? ")

output_unit = input("\n> what are the output units? ")

output_distance = distance * unit_converter[unit]

# print(unit_converter[output_unit])

print(f"> {distance} {unit} is {output_distance / unit_converter[output_unit]}")