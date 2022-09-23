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
# load csv file

f = open('contacts.csv')
contacts_list_of_strings = f.read().split('\n')  # --> converted to list
# print(contacts_list_of_strings)  # --> prints --> list


keys = contacts_list_of_strings[0]
keys_list = keys.split(',')  # -- list of keys
# print(keys_list)
'''
contact_1 = contacts_list_of_strings[1]
contact_2 = contacts_list_of_strings[2]
contact_3 = contacts_list_of_strings[3]
contacts = contact_1 + contact_2 + contact_3
values_list = contacts.split(',')
# print(values_list)  # --> list of values
'''
# values_list = [a for a in contacts_list_of_strings[1:]]
values_list = contacts_list_of_strings[1:]
# print('values list', values_list)
# ['sarde,pineapple,pink', 'eryan,strawberries,green', 'slade,papaya,blue']


def person_dictionary(keys_list, contact_split):
    person = {}
    for i in range(len(contact_split)):
        # print(contact_split[i], keys_list[i])
        person[keys_list[i]] = contact_split[i]
    # print(person)
    return person


final_list = []
for contact in values_list:
    # print(contact)
    contact_split = contact.split(',')

    person = person_dictionary(keys_list, contact_split)
    final_list.append(person)

# print('final list', final_list)


'''Version 2
Implement a CRUD REPL
 -Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
 -Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
 -Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
 -Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
'''


def create_contact(final_list, keys_list):
    # print(keys_list)

    # create a record
    # Ask the user for name, favorite fruit , favorite color
    user_name = input(f'Enter your {keys_list[0]}: ')
    user_favorite_fruit = input('Enter your favorite fruit: ')
    user_favorite_color = input('Enter your favorite color: ')
    # add user input to contact list
    user_inputs = {
        keys_list[0]: user_name,
        keys_list[1]: user_favorite_fruit,
        keys_list[2]: user_favorite_color
    }
    final_list.append(user_inputs)
    return final_list


# new_contact = create_contact(final_list, keys_list)

# print(new_contact)


def retrieve_contact(final_list):
    # ask the user for the contact's name
    input_contact_name = input('Enter contact\'s name: ')
    # print(input_contacts_name)
    for contact in final_list:
        name = contact['name']
        if name == input_contact_name:
            # print(contact)
            # print(name)

            return contact


# retrieve_contact(final_list)
print(final_list)


def update_contact(final_list):
    # ask the user for the contact's name
    input_name = input('Enter contact\'s name: ')
    # ask which attribute they would like to update
    input_attribute = input('What do you want to update?: ')
    input_value = input('What do you want to update it to?: ')
    # print(input_value)
    for contact in final_list:

        return contact


updated_contact = update_contact(final_list)


'''
# REPL Loop
stop = False
while not stop:
    response = input('Enter a choice(q, c, r, u): ').lower()
    if response == 'q':
        print('Person wants to quit')
        stop = True
    elif response == 'c':
        print('Person wants to create')
        new_contact = create_contact(final_list, keys_list)
        print(new_contact)
    elif response == 'r':
        print('Person wants to retrieve')
        contact = retrieve_contact(final_list)
        print(contact)
    elif response == 'u'
        print('Person wants to update')
        updated_contact = update_contact(final_list)
        print(updated_contact)
'''
#
