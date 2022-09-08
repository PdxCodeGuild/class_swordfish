# conversion_values = { 'feet': 0.3048,
# 'miles': 1609.34, 
# 'meters': 1, 
# 'kilometers': 1000
# }

# user_measurement = input('Please enter a number to convert to meters: ')

# user_measurement = int(user_measurement)

# converted_measurment = user_measurement * conversion_values['feet']

# print(converted_measurment)




# units = {'mi': 'miles',
# 'ft': 'feet',
# 'm': 'meter',
# 'km': 'kilometers'}

# conversion_values = { 'feet': 0.3048,
# 'miles': 1609.34, 
# 'meters': 1, 
# 'kilometers': 1000,
# 'yards': 0.9144,
# 'inches': 0.0254 
# }

# distance = input('What is the distance: ')

# distance = int(distance)

# user_units = input('What are the units? (feet/miles/meters/kilometers/yards/inches): ')

# chosen_conversion = distance * conversion_values[user_units]

# print(f"{distance} {user_units} is", round(chosen_conversion, 2), "m")


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
'inches': 39.3700787
}

user_distance = input('What is the distance?: ')
user_distance = int(user_distance)

user_units = input ('What is the units of the original distance?: ')
desired_units = input('What do you want the new unit of measurment to be?: ')

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

final_converted_units = userunits_meters * conversion_values_meters[desired_units]
print ('Your new units are ' + str(final_converted_units) + str(desired_units))



# print(new_units + desired_units)



 
    

# new_conversion = conversion_values[new_units] * chosen_conversion

# new_conversion = str(new_conversion)

# print('Your new conversion is', new_conversion + new_units)