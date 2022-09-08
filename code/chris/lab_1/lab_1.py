#Version_1
#converter = input(f'What is the distance in feet? ')
#converter = float(converter) * 0.3048
#print(f'The converted amt is {converter}m')

#Version_2

#distance = input('What is the distance you would like to convert? ')
#units = input('What are the units? ')
#distance = int(distance) * 0.3048

#if units == 'ft':
    #print(distance)
#if units == 'mi':
    #distance = float(distance) * 1609.34
    #print(f'Thanks for entering, your result is {distance} mi')
#if units == 'm':
    #distance = float(distance) * 1
    #print(f'Thanks for entering, your result is {distance} m')
#if units == 'km':
    #distance = float(distance) * 1000
    #print(f'Thanks for entering, your result is {distance} km')

#Version_3
#if units == 'yard':
    #distance = float(distance) * 0.9144
    #print(f'Thanks for entering, your result is {distance} yd')
#if units == 'in':
    #distance = float(distance) * 0.0254
    #print(f'Thanks for entering, your result is {distance} in')

#Version_4

distance = input('What is the distance you would like to convert? ')
units = input('What are the units? ')
units_output = input('What is your desired unit output? ')
distance = int(distance) 

m = 1
mi = 1609.34
ft = 0.3048
km = 1000
yd = 0.9144
inches = 0.0254

if units == 'm':
    users_unit = m 
elif units == 'mi':
    users_unit = mi
elif units == 'ft':
    users_unit = ft
elif units == 'km':
    users_unit = km
elif units == 'yd':
    users_unit = yd
elif units == 'inches':
    users_unit = inches

if units_output == 'm':
    users_converter = m
elif units_output == 'mi':
    users_converter = mi
elif units_output == 'ft':
    users_converter = ft
elif units_output == 'km':
    users_converter = km
elif units_output == 'yd':
    users_converter = yd
elif units_output == 'inches':
    users_converter = inches

conversion = distance * users_unit


print(f'{round(conversion / users_converter,4)}')

