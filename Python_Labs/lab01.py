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

conversion_values = { 'feet': 0.3048,
'miles': 1609.34, 
'meters': 1, 
'kilometers': 1000,
'yards': 0.9144,
'inches': 0.0254 
}

distance = input('What is the distance: ')

distance = int(distance)

user_units = input('What are the units? (feet/miles/meters/kilometers/yards/inches): ')

chosen_conversion = distance * conversion_values[user_units]

print(f"{distance} {user_units} is", round(chosen_conversion, 2), "m")