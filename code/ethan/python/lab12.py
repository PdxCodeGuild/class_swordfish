# Warhammer40k Army Point Tracker

# using pandas library

import pandas as pd

units = pd.read_csv('40k_units.csv')

weapons = pd.read_csv('40k_wargear.csv')

wargear_dictionary = weapons.to_dict('index')

unit_dictionary = units.to_dict('index')

x = 0
y = 0

point_total = 0

army_list = []

answer = 'yes'
wargear_answer = 'yes'
wargear_point_total = 0
wargear = ''
wargear_quantity = ''

while answer == 'yes':
    
    unit_name = input('What unit would you like to add to your list? ')
    
    unit_quantity = int(input(f'What quantity of {unit_name} would you like to add? '))

    for i in unit_dictionary:
    
        if unit_name == unit_dictionary[x]['name']:
            point_value = unit_dictionary[x]['point value']
            x+=1
        else:
            x+=1
    x = 0
    
    wargear_answer = input('Would you like to add any special weapons to that unit? ')

    while wargear_answer == 'yes':

        wargear = input('What wargear would you like to add? ')

        wargear_quantity = int(input(f'what quantity of {wargear} would you like to add? '))

        for i in wargear_dictionary:
            
            if wargear == wargear_dictionary[y]['name']:
                wargear_point_value = wargear_dictionary[y]['point value']
                wargear_point_total = wargear_point_value * wargear_quantity
                wargear_quantity = str(wargear_quantity)                
                y+=1
            else:
                y+=1

        y = 0

        wargear_answer = input('Would you like to add another special weapon? ')

    point_total = point_total + wargear_point_total + point_value * unit_quantity
    unit_point_total = wargear_point_total + point_value * unit_quantity
    unit_point_total = str(unit_point_total)
    quantity_string = str(unit_quantity)
    list_entry = unit_name + ' ' + 'x' + quantity_string + ' ' + wargear + ' ' + 'x' + wargear_quantity + ' ' + 'points:' + ' ' + unit_point_total
    army_list.append(list_entry)
    
    print(army_list)
    
    print(f'Total points: {point_total}')
    
    answer = input('Would you like to add another unit to your list? ')

army_list.append(f'Total points: {point_total}')

new_list = []

for i in range(0, len(army_list)):
    new_list.append(army_list[i])

new_list = '\n'.join(new_list)


with open('./army_list.csv', 'w') as f:
    f.write(new_list)

print('Army list created. Check army_list.csv for list. ')