'''
#Lab 1: Unit Converter(redo)
'''
'''
This lab will involve writing a program, that allows the user to convert a number between units
'''
'''
Version 1
'''
'''
Ask the user for the number of feet, and print out the equivalent distance in meters. 
Hint: 1 ft is 0.3048 m. 
output = meters = multiply input distance by 0.3048
'''
units = {
    'feet': 0.3048,
}
# ask the user to input the number of feet
feet = input('Enter the distance in feet?: ')  # 200
# convert the feet entered by the user to an integer
converted_feet = int(feet)
# print(type(converted_feet))
total = feet * units['feet']
print(total)  # 60.96
