'''
program: lab_08
author: billy frick
date: 28 september 2022

function:   > this program will pull a 'contacts list' from a CSV file.
            > the program will open the file and create a dictionary based on the information given.
            > the user can then update, add or delete a contact; as well as print a specific contact and their related information.
            > when the user inputs 'exit' as a command, the program will exit and the contact CSV will be updated by writing (w) to it.
'''
from numpy import ubyte
import pytest

# this function will open the csv file and split the headers and contacts.
# the contacts will be seperated by using '\n', and the information of each contact will be seperated using ','.
def open_csv(file):
    
    with open(file) as contact_csv:

        lines = contact_csv.read().split('\n')

    contacts = []

    headers = lines[0].split(',')


    for words in range(1, len(lines)):

        rows = lines[words].split(',')

        contact = dict(zip(headers, rows))

        contacts.append(contact)

    return headers, contacts

# this will properly print a contact and its related information.
# the 'items' are the name, favorite color and favorite fruit.
def print_contact(contact):

    if type(contact) is str:

        print(contact)

    else:

        for k, v in contact.items():

            print(f'{k}: {v}')

# this will create a contact and append it to the already existing contacts dict.
# the contact will NOT be written to the CSV until the user 'exits' the program.
def create_contact(contacts, contact):

    contacts.append(contact)

    return contact

# this will find a specific contact and return it's values.
# the enumerate function will return the contact with its values and properties.
def find_specific_contact(contacts, name):

    for index, contact in enumerate(contacts):

        # this ensures that only a contact with a matching name will be returned.
        if contact['name'] == name:

            return index

# this will utilize the find_specific_contact function.
# this will allow the program to search all of the contacts, and return the users search.
def retrieve_contacts(contacts, name): 

    # finds the specific contact within the entire dict.
    index = find_specific_contact(contacts, name)

    if index > -1:

        return contacts[index]

    else:

        return ("\n> the contact you are looking for does not exist.")

# this will allow the user to update an already existing contact.
def update_contact(contacts, name, updated_contact):

    name_index = find_specific_contact(contacts, name)

    # ensures all elements will be accounted for and properly updated.
    if name_index > -1:

        # updates the existing contact with
        contacts[name_index].update(updated_contact)

        print(contacts[name_index])

    return contacts

# this function will find a specific contact with the function of the same name.
def delete_contact(contacts, name):

    name_index = find_specific_contact(contacts, name)

    # this will ensure all elements of the contact is deleted.
    if name_index > -1:

        # deletes the contact
        return contacts.pop(name_index)

    else:

        return(f'\n{name} is not in the contacts list. It may have been deleted already...')


def save_contact(contacts, file, header):

    lines = [','.join(header)]

    for contact in contacts:

        row = ','.join(contact.values())
        
        lines.append(row)
    
    csv = '\n'.join(lines)

    with open(file, 'w') as write_file:

        write_file.write(csv)

# main body for CRUD REPL.
def main():

    file = 'contacts.csv'

    headers, contacts = open_csv(file)

        #loops will run the program until the user inputs 'exit', to end the program/
    while True:
            
        print('\nWelcome! please refer to the list of commands below:')

        print('\n*----------------COMMAND LIST----------------*'
                '\n> update - (updates contact) \t> retrieve - (retrieves contact)'
                '\n> delete - (deletes a contact) \t> create - (creates contact)'
                '\n> exit - (exits the program)')

        # this will determine what command is executed.
        user_input = input()
        
        # this will update a contact already in the folder.
        # this if statement will list their name, favorite fruit, favorite color.
        # the user will then determine the new values or each one (or keep some the same).
        if user_input == 'update':

            contact = {}

            name = input('\n> please enter the name of the contact you would like to update: ')
            
            print('\n> you will be updating the following contact:')

            print_contact(retrieve_contacts(contacts, name))

            print('\n> only enter in values for the information you want updated, otherwise enter what was previously there.\n')

            for key in headers:

                value = input(f'{key}: ')

                contact[key] = value

            # this will properly create a new version of the contact by iterating over the previous values.
            contact = {k:v for k,v in contact.items()}

            contacts = update_contact(contacts, name, contact)

        # this will use the retrieve_contacts
        # and print_contact functions.
        # the user input will determine the contact that will be printed.
        # the contacts name, favorite fruit and color will be displayed.
        elif user_input == 'retrieve':

            name = input('\nWhat is the contacts name? ')

            print_contact(retrieve_contacts(contacts, name))

        # this will delete a contact by utilizing the delete_contact function.
        # the user will input the name of the contact they wish to delete.
        elif user_input == 'delete':

            name = input('\n> please enter the name of the contact you would like to delete: ')

            print(f'\n> the contact {name} will be deleted.')

            print_contact(delete_contact(contacts, name))

        # this command will utilize the create_contact function.
        # a contact's name, favorite fruit and color will be grabbed via the 'for' loop.
        elif user_input == 'create':

            contact = {}

            for words in headers:

                input_value = input(f'{words}: ')

                contact[words] = input_value

            create_contact(contacts, contact)     

        # this will end the program, and save any changes made to the contact list.
        # uses save_contact function to write to the csv file.
        elif user_input == 'exit':

            save_contact(contacts, file, headers)

            exit()
main()


    

    

    
        



