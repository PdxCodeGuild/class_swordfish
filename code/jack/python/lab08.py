#lab 08: contact list


#load csv file and save contents as list of strings
csvfile = 'contacts.csv'
with open(csvfile, 'r') as file:
    lines = file.read().split('\n')


#pulls csv headers out and converts to list
keys = lines.pop(0)
keys = keys.split(',')


#converts csv data from strings to dictionaries stored in contacts list
contacts = []
for x in lines:
    dict_x = {}
    split_line = x.split(',')
    for i in range(len(keys)):
        dict_x[keys[i]] = split_line[i]
    contacts.append(dict_x)


# contact create function returns the new contact dictionary
def create():
    print('Creating new contact...\n')
    name = input('Enter the contact name:\n>').capitalize()
    fruit = input('Enter the favorite fruit:\n>').capitalize()
    color = input('Enter the favorite color:\n>').capitalize()
    new_line = [name, fruit, color]
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = new_line[i]
    return new_dict


#function to return list of contact dictionaries with given name
def contacts_name(name):
    ret_contacts = []
    for x in contacts: # finds all contacts with retrieved name, appends contact dictionary to retrieved contacts list
        if x['name'] == name:
            ret_contacts.append(x)
    return ret_contacts


#function to return contact info as a string
def retrieve(name):
    ret_contacts = contacts_name(name) # function returns list of contact dictionaries with given name
    req_output = ''
    req_output_num = 0 # used to output number of contacts found
    for contact in ret_contacts: # runs through each contact in the list
        req_output += f'Contact #{ret_contacts.index(contact) + 1}: '
        for i in range(len(keys)):
            req_output += (f'{keys[i]}: {contact[keys[i]]}')
            if i != len(keys) - 1: # if statement checks for following info to append commas for
                req_output += ', '
        req_output += '\n'
        req_output_num += 1
    s = 's' # weird error if variable isn't used
    n = '' # weird error if variable isn't used
    print(f'\n{req_output_num} contact{s if req_output_num > 1 else n} with \'{name}\' name found:')
    return req_output


#function to select which contact to work with when multiple with same name exist
#returns
#to be called when user inputs a name with multiple associated contact dictionaries
def contact_select(name, ret_contacts):
    print(retrieve(name)) # prints all contacts with given name
    while True:
        try:
            ret_contacts_i = input(f'Select target contact (1-{len(ret_contacts)}):\n>')
            ret_contacts_i = int(ret_contacts_i) - 1
            if 0 <= ret_contacts_i < len(ret_contacts):
                break
            else:
                raise ValueError
        except:
            print('Invalid input')
    select_dict = ret_contacts[ret_contacts_i] # selected contact dictionary is the selected dict from retrieved dicts (ret_contacts)
    contacts_i = contacts.index(select_dict) # index of selected dictionary in main 'contacts' list
    return contacts_i


# function returns the main 'contacts' list index of selected contact dictionary 
def contacts_index(name):
    ret_contacts = contacts_name(name) # retrieves list of contact dictionaries with given name
    if len(ret_contacts) == 0:
        print(f'No contacts with {name} name found.\n')
        return None
    elif len(ret_contacts) > 1: # if multiple contacts with requested name, runs contact select function
        contacts_i = contact_select(name, ret_contacts) ### see below
    else:
        for x in contacts:
            if x['name'] == name:
                contacts_i = contacts.index(x)
    return contacts_i


# UPDATE 
def update(name): 
    contacts_i = contacts_index(name) # function returns correct 'contacts' index to work with
    update_contact = contacts[contacts_i] # dictionary associated with aforementioned index
    print('\nUpdating contact...')
    print('Note: press return to skip the field.')
    for x in update_contact: # for loop runs through each attribute in the contact
        updated_info = input(f'Enter new value for {x}:\n>').capitalize()
        if updated_info != '': # if nothing entered, field is not updated
            update_contact[x] = updated_info

#function to delete contact
def delete(name):
    contacts_i = contacts_index(name) # function returns correct 'contacts' index to work with
    contacts.pop(contacts_i)



input_options = ['e', 'c', 'r', 'u', 'd']

#REPL to make CRUD actions
while True:
    while True: # while loop to ensure input is allowed
        action = input('Choose one of the following:\n\tCreate a record (c)\n\tRetrieve a record (r)\n\tUpdate a record (u)\n\tDelete a record (d)\n\tExit (e)\n>').lower()
        if action in input_options:
            break
        else:
            print('Invalid input.\n')
    if action == 'e':
        break

    if action == 'c':
        contacts.append(create())
        print('Contact created.\n')
    elif action == 'r':
        name_input = input('Enter a the contact name:\n>').capitalize()
        print(retrieve(name_input))
    elif action == 'u':
        name_input = input('Enter a contact name to update:\n>').capitalize()
        update(name_input)
        print('\nContact updated.\n')
    elif action == 'd':
        name_input = input('Enter a contact name to remove:\n>').capitalize()
        delete(name_input)
        print('\nContact removed.\n')
    
    cont = input('Press enter to continue')
    print('\n\n')

updated_contents = ','.join(keys) + '\n'
for dictionary in contacts:
    attributes = [dictionary[i] for i in dictionary.keys()]
    updated_contents += ','.join(attributes)
    if contacts.index(dictionary) + 1 != len(contacts):
        updated_contents += '\n'

with open(csvfile, 'w') as f:
    f.write(updated_contents)