conversion_values = { 'feet': 0.3048,
'miles': 1609.34, 
'meters': 1, 
'kilometers': 1000
}

user_measurement = input('Please enter a number to convert to meters: ')

user_measurement = int(user_measurement)

converted_measurment = user_measurement * conversion_values['feet']

print(converted_measurment)