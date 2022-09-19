import re

#Version 1 
with open('/Users/ckeego/code-guild/class_swordfish/code/chris/lab_8/lab_8.csv') as file:
    contact_list_csv = file.read().split('\n')
    
cont_list = contact_list_csv
# print(cont_list[0])

contact_list = []

for index in cont_list:
    # print(index)
    delimit = (index.split(","))
    # print(delimit)
    for index_2 in delimit:
        list_row = {'name':delimit[0], 'favorite_fruit':delimit[1], 'favorite_color':delimit[2]}
        # name = delimit[0]
        # print(name)
        # favorite_fruit = delimit[1]
        # print(favorite_fruit)
        # favorite_color = delimit[2]
        # print(favorite_color)
        # list_row = {'name':name, 'favorite_fruit':favorite_fruit, 'favorite_color':favorite_color}
    # print(list_row)
        
    contact_list.append(list_row)
del contact_list[0]
#print(contact_list) #[{'name': 'albert', 'favorite_fruit': 'mango', 'favorite_color': 'red'}]

#Version 2

# #CREATE a RECORD
# user_name = input(f'Please give us your name: ')
# user_fruit = input(f'What is your favorite fruit? ')
# user_color = input(f'What is your favorite color? ')
user_name = 'ron'
user_fruit = 'grape'
user_color = 'blue'

def new_user_func(contacts, name_para, color_para, fruit_para):
    # user_name = input(f'Please give us your name: ')
    # user_fruit = input(f'What is your favorite fruit? ')
    # user_color = input(f'What is your favorite color? ')
    user_dict = {'name' : name_para, 'favorite_fruit' : fruit_para, 'favorite_color' : color_para}
    # for k in user_dict:
    #     if k == user_name:
    #         user_dict['name'] = user_name
    #     elif k == user_fruit:
    #         user_dict['favorite_fruit'] = user_fruit
    #     elif k == user_color:
    #         user_dict['favorite_color'] = user_color
    contacts.append(user_dict)
    return contacts
contact_list = new_user_func(contact_list, user_name, user_color, user_fruit)
# print(contact_list)

#RETRIEVE a RECORD
#  HOW DO I ACCESS KEYS IN A DICTIONARY IN A LIST?
# user_name = input(f'Please give us your name: ')

user_name = 'ron'

# for x in contact_list:
#     print(x['name'])

def retrieve_func(retrieve_name):
    for x in contact_list:
        if retrieve_name == x['name']:
            # present = (x['favorite_fruit'], x['favorite_color']) #Tuple
            fruit = (x['favorite_fruit']) 
            color = (x['favorite_color'])
            present = f'Your favorite fruit is: {fruit}' + ' ' + 'and' + ' ' + f'Your favorite color is: {color}'
    return present

# print(retrieve_func(user_name))

# UPDATE a RECORD

# up_name = input('Please enter your name: ')
up_name = 'ron'

for i, contact in enumerate(contact_list): #contact = each dictionary in list
    # print(i, contact)
    if up_name == contact['name']:
        #print(i, contact['name'])
        updated = input('What would you like to update? fruit or color')

up_fc = updated 

def fruit_func(fruit_update):
    for i, contact in enumerate(contact_list):
        if up_name == contact['name']:







# def update_func(name_para):
    # for x in contact_list:
    #     if up_name == x['name']:
    #         print('Would you like to update fruit or color?')
    #     elif up_name != x['name']:
    #         print('Try Again!')

# def update_fruit(n_fruit):

# fruit_up = input('Would you like to update your favorite fruit? Y/N')
# fruit_new = input('What would you like your new fruit to be ')
# color_up = input('Would you like to update your favorite color? Y/N')
# color_new = input('What would you like your new color to be ')
        
#         if updated == 'fruit':
#             new_fruit = input('What would you like your new fruit to be? ')
#             new_fruit_latest = x[new_fruit]
#             present_fruit = f'Your new color is: {new_fruit_latest}'
#             print(present_fruit)
#         if updated == 'color':
#             new_color = input('What would you like your new color to be? ')
#             new_color_latest = x[new_color]
#             present_color = f'Your new color is: {new_color_latest}'
#             print(present_color)
#     return update_func

# print(up_name)
