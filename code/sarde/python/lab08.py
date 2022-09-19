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


from optparse import Values
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
#values_list = [a for a in contacts_list_of_strings[1:]]
values_list = contacts_list_of_strings[1:]
#print('values list', values_list)
#['sarde,pineapple,pink', 'eryan,strawberries,green', 'slade,papaya,blue']


def person_dictionary(keys_list, contact_split):
    person = {}
    for i in range(len(contact_split)):
        #print(contact_split[i], keys_list[i])
        person[keys_list[i]] = contact_split[i]
    # print(person)
    return person


final_list = []
for contact in values_list:
    # print(contact)
    contact_split = contact.split(',')

    person = person_dictionary(keys_list, contact_split)
    final_list.append(person)

print('final list', final_list)


'''Version 2
Implement a CRUD REPL
 -Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
 -Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
 -Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
 -Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
'''


def create_contacts(final_list, keys_list):
    print(keys_list)

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


new_contacts = create_contacts(final_list, keys_list)

# print(new_contacts)


# def retrieve_contacts(final_list):
# ask the user for the contact's name
input_contacts_name = input('Enter contact\'s name: ')
# convert input to int
converted_input = int(input_contacts_name)
#print("contact's name", input_contacts_name)
print(final_list)

'''
    # find the user with the given name
    # iterate over the final list
    for i in final_list:
        # if the input name is equal to
        if final_list[1] == input_contacts_name:
            print(contact)
    # display their information
    return input_contacts_name


retrieve_contacts(final_list)
'''
