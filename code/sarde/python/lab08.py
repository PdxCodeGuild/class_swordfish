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
# print(contacts_list)  # --> prints --> list


keys = contacts_list[0]
keys_list = keys.split(',')  # -- list of keys
# print(keys_list)
contact_1 = contacts_list[1]
contact_2 = contacts_list[2]
contact_3 = contacts_list[3]
contacts = contact_1 + contact_2 + contact_3
values_list = contacts.split(',')
# print(values_list)  # --> list of values


def contacts_list_dictionary(keys_list, values_list):

    # create an empty list
    list_dict = []
    # iterate over the elements
    for i in range(len(keys)):
        contacts_list_dict = (
            {keys_list[0]: values_list[0], keys_list[1]
                : values_list[1], keys_list[2]: values_list[2]},
            {keys_list[0]: values_list[3], keys_list[1]: values_list[4],  keys_list[2]: values_list[5]},
            {keys_list[0]: values_list[6], keys_list[1]: values_list[7],  keys_list[2]: values_list[8]},)
    list_dict.append(contacts_list_dict)
    final_list = list(contacts_list_dict)
    print(final_list)

    return final_list


contacts_list_dictionary(keys_list, values_list)
