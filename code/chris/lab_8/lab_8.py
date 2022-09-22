import re

#All Three Versions

#Version 1
with open('lab_8.csv') as file:
    contact_list_csv = file.read().split('\n')

contact_list = []

for index in contact_list_csv:
    
    delimit = (index.split(","))
 
    for index_2 in delimit:
        list_row = {'name':delimit[0], 'favorite fruit':delimit[1], 'favorite color':delimit[2]}
        
    contact_list.append(list_row)
header = ','.join(contact_list.pop(0).values())
print(contact_list)
# Version 2a
def new_user_func(contacts):
    user_name = input(f'Please give us your name: ')
    favorite_fruit = input(f'What is your favorite fruit? ')
    favorite_color = input(f'What is your favorite color? ')
    user_dict = {'name' : user_name, 'favorite fruit' : favorite_fruit, 'favorite color' : favorite_color}
    contacts.append(user_dict)
    return contacts

# Version 2b
def retrieve_func(contact_list):
    user_name = input(f'Please give us your name: ')
    for x in contact_list:
        if user_name == x['name']:
            fruit = (x['favorite fruit']) 
            color = (x['favorite color'])
            present = f'Your favorite fruit is: {fruit}' + ' ' + 'and' + ' ' + f'Your favorite color is: {color}'
    return present

#Version 2c

def update_func(contact_list):
    up_name = input('Please give us your name: ')
    for i, contact in enumerate(contact_list): #contact = each dictionary in list
        if up_name == i['name']:
            fruit_color = input('What would you like to update? Your choices are, favorite fruit or favorite color: ')
            fruit_update = 'favorite fruit'
            color_update = 'favorite color'
            if fruit_color == fruit_update:
                contact[fruit_color] = input(f'Please enter your new value for {fruit_update}: ')
            elif fruit_color == color_update:   
                contact[fruit_color] = input(f'Please enter your new value for {color_update}: ')
            break
    return contact_list

#Version 2d

def del_update(contact_list):
    del_name = input('Please give us your name: ')
    for i, contact in enumerate(contact_list):
        # print(i, contact)
        if del_name == contact['name']:
            # print(i, contact['name'])
            contact_list.remove(contact)
    return contact_list

def write_func(contact_list):
    output_list = []
    for contact in contact_list:
        the_values = list(contact.values())
        the_values_string = ','.join(the_values)
        output_list.append(the_values_string)
    return output_list
# print(write_func(contact_list))


keep_looping = True

while keep_looping:
    response = input(f'What would you like to do? (create)(retrieve)(update)(delete)(quit): ').lower()
    if response == 'quit':
        print('User is quitting')
        keep_looping = False
    elif response == 'create':
        print('User is creating')
        contact_list = new_user_func(contact_list)
    elif response == 'retrieve':
        print('User is retrieving')
        retrieve_string_fruit_color = retrieve_func(contact_list)
        print(retrieve_string_fruit_color)
    elif response == 'update':
        print('User wants to update')
        contact_list = update_func(contact_list)
    elif response == 'delete':
        print('User wants to delete')
        contact_list = del_update(contact_list)

#Version 3
with open('lab_8_backup.csv', 'w') as file:
    file.write(header + '\n')
    for i in write_func(contact_list):
        file.write(i + '\n')




# Version 3 - Write an updated CSV file to be saved

# practice_dict = {'name': 'albert', 'favorite fruit': 'mango', 'favorite color': 'red'}
# #going to add back commas
# the_keys = list(practice_dict.keys())
# print(the_keys)
# print('.................')
# key_string = ','.join(the_keys)
# print(key_string)
# #going to add back new line
# contacts_string = key_string + '\n'
# print(contacts_string)


# print(contact_list)

# for i in contact_list:
#     # print(i)
#     for key in i:
#         # print(i)
#         the_values = list(i.values())
#         the_values_string = ', '.join(the_values)
#         new_contact_list = the_values_string + '\n'
#     print(new_contact_list)

#THE CSV
# name,favorite fruit,favorite color
# albert,mango,red
# bob,strawberry,yellow
# cecil,grapes,green
# debbie,banana,blue
# elizabeth,blueberry,violet
# frederick,apple,black
# george,watermelon,white

# #Version 1 
# with open('lab_8.csv') as file:
#     contact_list_csv = file.read().split('\n')
    
# # cont_list = contact_list_csv
# # # print(cont_list[0])

# contact_list = []
# # print(cont_list)
# for index in contact_list_csv:
#     # print(index)
#     delimit = (index.split(","))
#     # print(delimit)
#     for index_2 in delimit:
#         list_row = {'name':delimit[0], 'favorite fruit':delimit[1], 'favorite color':delimit[2]}
#         # name = delimit[0]
#         # print(name)
#         # favorite_fruit = delimit[1]
#         # print(favorite_fruit)
#         # favorite_color = delimit[2]
#         # print(favorite_color)
#         # list_row = {'name':name, 'favorite_fruit':favorite_fruit, 'favorite_color':favorite_color}
#     # print(list_row)
        
#     contact_list.append(list_row)
# header = ','.join(contact_list.pop(0).values())

# print(header)
# # # del contact_list[0]
# # print(f'Version 1 Completed: {contact_list}')
# #print(contact_list) #[{'name': 'albert', 'favorite_fruit': 'mango', 'favorite_color': 'red'}]

# #Version 2

# # #CREATE a RECORD
# # user_name = input(f'Please give us your name: ')
# # user_fruit = input(f'What is your favorite fruit? ')
# # user_color = input(f'What is your favorite color? ')
# # user_name = 'ron'
# # user_fruit = 'grape'
# # user_color = 'blue'

# def new_user_func(contacts):
#     user_name = input(f'Please give us your name: ')
#     favorite_fruit = input(f'What is your favorite fruit? ')
#     favorite_color = input(f'What is your favorite color? ')
#     user_dict = {'name' : user_name, 'favorite fruit' : favorite_fruit, 'favorite color' : favorite_color}
#     # for k in user_dict:
#     #     if k == user_name:
#     #         user_dict['name'] = user_name
#     #     elif k == user_fruit:
#     #         user_dict['favorite_fruit'] = user_fruit
#     #     elif k == user_color:
#     #         user_dict['favorite_color'] = user_color
#     contacts.append(user_dict)
#     return contacts
# # contact_list = new_user_func(contact_list)
# # print(f'Version 2 CREATE Completed: {contact_list}')

# # #RETRIEVE a RECORD
# # #  HOW DO I ACCESS KEYS IN A DICTIONARY IN A LIST?


# # user_name = 'ron'

# # for x in contact_list:
# #     print(x['name'])

# def retrieve_func(contact_list):
#     user_name = input(f'Please give us your name: ')
#     for x in contact_list:
#         if user_name == x['name']:
#             # present = (x['favorite_fruit'], x['favorite_color']) #Tuple
#             fruit = (x['favorite fruit']) 
#             color = (x['favorite color'])
#             present = f'Your favorite fruit is: {fruit}' + ' ' + 'and' + ' ' + f'Your favorite color is: {color}'
#     return present

# # print(f'Version 2 RETRIEVE Completed: {retrieve_func(user_name)}')

# # # UPDATE a RECORD

# # # up_name = input('Please enter your name: ')
# # up_name = 'ron'
# # print(contact_list)

# def update_func(contact_list):
#     up_name = input('Please enter your name: ')
#     for i, contact in enumerate(contact_list): #contact = each dictionary in list
#         # print(i, contact)
#         if up_name == contact['name']:
#         ## print(i, contact['name'])
#         # updated = input('What would you like to update? favorite fruit or favorite color')
#             updated = 'favorite fruit'
#             contact[updated] = input(f'Please enter your new value for {updated}: ')
#             break
#     return contact_list
# # print(f'Version 2 UPDATE Completed: {contact_list}')

# # # DELETE a RECORD

# del_name = 'albert'

# # print(contact_list)
# def del_update(contact_list):
#     del_name = input('Please enter your name: ')
#     for i, contact in enumerate(contact_list):
#         # print(i, contact)
#         if del_name == contact['name']:
#             # print(i, contact['name'])
#             contact_list.remove(contact)
#     return contact_list
# # print(f'Version 2 DELETE Completed: {contact_list}')

# # # def del_func(del_para):
# # #     for i, contact in enumerate(contact_list):
# # #         if del_para == i['name']:
# # #             contact_list.remove(contact)
# def write_func(contact_list):
#     output_list = []
#     for contact in contact_list:
#     # print(i)
#         # for key in contact:
#         # print(i)
#         the_values = list(contact.values())
#         the_values_string = ','.join(the_values)
#         output_list.append(the_values_string)
#     return output_list
# print(write_func(contact_list))


# keep_looping = True

# while keep_looping:
#     response = input(f'What would you like to do? (q)(c)(r)(u)(d)').lower()
#     if response == 'q':
#         print('User is quitting')
#         keep_looping = False
#     elif response == 'c':
#         print('User is creating')
#         contact_list = new_user_func(contact_list)
#     elif response == 'r':
#         print('User is retrieving')
#         retrieve_string_fruit_color = retrieve_func(contact_list)
#         print(retrieve_string_fruit_color)
#     elif response == 'u':
#         print('User wants to update')
#         contact_list = update_func(contact_list)
#     elif response == 'd':
#         print('User wants to delete')
#         contact_list = del_update(contact_list)
# # print(contact_list)

# # contact_list = write_func(contact_list)

# with open('lab_8_backup.csv', 'w') as file:
#     file.write(header + '\n')
#     for i in write_func(contact_list):
#         file.write(i + '\n')
#         # file.write()