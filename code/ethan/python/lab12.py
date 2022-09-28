# Warhammer40k Army Point Tracker

# using pandas library

import pandas as pd

units = pd.read_csv('40k_units.csv')

dictionary = units.to_dict('index')

x = 0

point_total = 0

army_list = []

answer = 'yes'

while answer == 'yes':
    unit_name = input('What unit would you like to add to your list? ')

    unit_quantity = int(input('what quantity would you like to add? '))

    for i in dictionary:
        if unit_name in dictionary[x]['name']:
            point_value = dictionary[x]['point value']
            point_total = point_total + point_value * unit_quantity
            unit_point_total = point_value * unit_quantity
            unit_point_total = str(unit_point_total)
            quantity_string = str(unit_quantity)
            name_string = dictionary[x]['name']
            list_entry = name_string + ' ' + 'x' + quantity_string + ' ' + 'points:' + ' ' + unit_point_total
            army_list.append(list_entry)
            x+=1
        else:
            x+=1
    print(army_list)
    print(f'Total points: {point_total}')
    answer = input('Would you like to add another unit to your list? ')

print(army_list)
print(point_total)