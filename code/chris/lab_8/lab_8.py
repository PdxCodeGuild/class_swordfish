import re
from xxlimited import new

#Version 1 
with open('lab_8.csv') as file:
    contact_list_csv = file.read().split('\n')
    
cont_list = contact_list_csv
# print(cont_list[0])

contact_list = []

for index in cont_list:
    # print(index)
    delimit = (index.split(","))
    # print(delimit)
    for index_2 in delimit:
        list_row = {'name':delimit[0], 'favorite fruit':delimit[1], 'favorite color':delimit[2]}
        # name = delimit[0]
        # print(name)
        # favorite_fruit = delimit[1]
        # print(favorite_fruit)
        # favorite_color = delimit[2]
        # print(favorite_color)
        # list_row = {'name':name, 'favorite_fruit':favorite_fruit, 'favorite_color':favorite_color}
    # print(list_row)
        
    contact_list.append(list_row)
header = contact_list.pop(0)
print(header)
# del contact_list[0]
print(f'Version 1 Completed: {contact_list}')
#print(contact_list) #[{'name': 'albert', 'favorite_fruit': 'mango', 'favorite_color': 'red'}]

#Version 2

# #CREATE a RECORD
# user_name = input(f'Please give us your name: ')
# user_fruit = input(f'What is your favorite fruit? ')
# user_color = input(f'What is your favorite color? ')
# user_name = 'ron'
# user_fruit = 'grape'
# user_color = 'blue'

def new_user_func(contacts):
    user_name = input(f'Please give us your name: ')
    user_fruit = input(f'What is your favorite fruit? ')
    user_color = input(f'What is your favorite color? ')
    user_dict = {'name' : name_para, 'favorite fruit' : fruit_para, 'favorite color' : color_para}
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
print(f'Version 2 CREATE Completed: {contact_list}')

# #RETRIEVE a RECORD
# #  HOW DO I ACCESS KEYS IN A DICTIONARY IN A LIST?
# # user_name = input(f'Please give us your name: ')

user_name = 'ron'

# for x in contact_list:
#     print(x['name'])

def retrieve_func(retrieve_name):
    for x in contact_list:
        if retrieve_name == x['name']:
            # present = (x['favorite_fruit'], x['favorite_color']) #Tuple
            fruit = (x['favorite fruit']) 
            color = (x['favorite color'])
            present = f'Your favorite fruit is: {fruit}' + ' ' + 'and' + ' ' + f'Your favorite color is: {color}'
    return present

print(f'Version 2 RETRIEVE Completed: {retrieve_func(user_name)}')

# # UPDATE a RECORD

# # up_name = input('Please enter your name: ')
up_name = 'ron'
# print(contact_list)

for i, contact in enumerate(contact_list): #contact = each dictionary in list
    # print(i, contact)
    if up_name == contact['name']:
        ## print(i, contact['name'])
        # updated = input('What would you like to update? favorite fruit or favorite color')
        updated = 'favorite fruit'
        contact[updated] = input(f'Please enter your new value for {updated}: ')
        break
print(f'Version 2 UPDATE Completed: {contact_list}')

# # DELETE a RECORD

del_name = 'albert'

# print(contact_list)

for i, contact in enumerate(contact_list):
        # print(i, contact)
        if del_name == contact['name']:
            # print(i, contact['name'])
            contact_list.remove(contact)
print(f'Version 2 DELETE Completed: {contact_list}')

# # def del_func(del_para):
# #     for i, contact in enumerate(contact_list):
# #         if del_para == i['name']:
# #             contact_list.remove(contact)

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

for i in contact_list:
    # print(i)
    for key in i:
        # print(i)
        the_values = list(i.values())
        the_values_string = ', '.join(the_values)
        new_contact_list = the_values_string + '\n'
    print(new_contact_list)

# with open('lab_8.csv', 'w') as file:
#     file.write(new_contact_list)

keep_looping = True

while keep_looping:
    response = input(f'What would you like to do? (q)(c)').lower()
    if response == 'q':
        print('User is quitting')
        keep_looping = False
    elif response == 'c':
        print('User is creating')
        return


    