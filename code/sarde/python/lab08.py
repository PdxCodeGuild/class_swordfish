'''Lab 8: Contact List
'''
'''
Version 1
-build a program to manage a list of contacts
    -build a CSV ('comma separated values'), load file
    -headers might consist of name, favorite fruit, favorite color
    -open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user.
    -the text in the header represents the keys,
    -the text in the other lines represent the values
'''
'''
with open('contacts.csv') as file:
    lines = file.read().split('\n')
    print(lines)  # --> prints a list
'''


# load csv file
f = open('contacts.csv')
contacts_list = f.read().split('\n')  # --> converted to list
print(contacts_list)  # --> prints --> list

'''
tuple_list = []
keys = contacts_list[0],
# print(keys)  # -- tuple
contact_1 = contacts_list[1],
contact_2 = contacts_list[2],
contact_3 = contacts_list[3],
values = contact_1, contact_2, contact_3
# print(values)  # -- tuple
tuple_list.append(keys)
tuple_list.append(values)
# print(tuple_list)
'''


def contacts_list_dictionary(contacts_list):
    tuple_list_keys = contacts_list[0].split(',')
    tuple_list_values = contacts_list[1], contacts_list[2], contacts_list[3]
    print(tuple_list_keys)
    print(tuple_list_values)
    name_key = tuple_list_keys[0]
    # print(name_key)
    favorite_fruit_key = tuple_list_keys[1]
    # print(favorite_fruit_key)
    favorite_color_key = tuple_list_keys[2]
    # print(favorite_color_key)
    # tuple_dictionary = dict((i) for i in tuple_list)
    # print(tuple_dictionary)
    return


contacts_list_dictionary(contacts_list)
