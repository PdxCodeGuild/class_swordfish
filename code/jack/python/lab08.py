# Lab 08: Contact List


# load csv file and save contents as a list of strings
with open('./contacts.csv', 'r') as file:
    lines = file.read().split('\n') # each line of data is stored as a string in a list


# removes and stores csv headers
# used to generate dictionary keys
keys = lines.pop(0)
keys = keys.split(',') # string of headers to list of headers


# converts 'lines' variable from strings to dictionaries
# each line is converted to a dictionary
contacts = [] # main list of dictionaries containing all data
for x in lines:
    split_line = x.split(',') # string of data converted to list of data
    dict_x = {} 
    for i in range(len(keys)): # creates a key from 'keys' and matches index to the data for each line and column
        dict_x[keys[i]] = split_line[i]
    contacts.append(dict_x) # adds dictionary to main contacts list


# data is now processed for use in program


# function to return list of contact dictionaries with given name
def contacts_name(name):
    ret_contacts = []
    for x in contacts: # finds all contacts with retrieved name, appends contact dictionary to retrieved contacts list
        if x['name'] == name:
            ret_contacts.append(x)
    return ret_contacts


# contact create function
# returns the new contact dictionary
def create():
    print('Creating new contact...\n')
    new_line = [input(f'Enter the {x}:\n>').capitalize() for x in keys] # creates a list of user inputs for each key
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = new_line[i] # adds each item in new_line list as a value to its respective key
    contacts.append(new_dict)
    print('Contact created.\n')


#function to return contact info as a string
def retrieve(name = None):
    if name == None:
        name = input('Enter a the contact name:\n>').capitalize()
    ret_contacts = contacts_name(name) # function returns list of contact dictionaries with given name
    
    output = '' # empty string to append to
    output_num = 0 # used to track number of contacts returned
    for contact in ret_contacts: # runs through each contact in the list
        output += f'Contact #{ret_contacts.index(contact) + 1}: ' # contact info prefixed by temporary contact ID
        for i in range(len(keys)):
            output += (f'{keys[i]}: {contact[keys[i]]}')
            if i != len(keys) - 1: # if statement checks for following info to append commas for
                output += ', '
        output += '\n'
        output_num += 1
    s = 's' # weird error if variable isn't used
    n = '' # weird error if variable isn't used
    print(f'\n{output_num} contact{s if output_num != 1 else n} with \'{name}\' name found:')
    print(output)


#function to select which contact to work with when multiple with same name exist
#returns
#to be called when user inputs a name with multiple associated contact dictionaries
def contact_select(name, ret_contacts):
    retrieve(name) # function prints found contacts with given name
    
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
        print(f'No contacts with \'{name}\' name found.\n')
        return None
    elif len(ret_contacts) > 1: # if multiple contacts with requested name, runs contact select function
        contacts_i = contact_select(name, ret_contacts) 
    else:
        contacts_i = contacts.index(ret_contacts[0])

    return contacts_i


# function to update contact
def update(): 
    name = input('Enter a contact name to update:\n>').capitalize()
    contacts_i = contacts_index(name) # function returns correct 'contacts' index to work with
    
    #only runs update function body if valid contact is found
    if contacts_i in range(len(contacts)):
        update_contact = contacts[contacts_i] # pulls dictionary associated with above index
        print('\nUpdating contact...')
        print('Note: press return to skip the field.')
        
        for x in update_contact: # for loop runs through each attribute in the contact
            updated_info = input(f'Enter new value for {x}:\n>').capitalize()
            if updated_info != '': # if nothing entered, field is not updated
                update_contact[x] = updated_info
        print('Contact updated.\n')

    else:
        print('No contact updated.\n')
    

# function to delete contact
def delete():
    name = input('Enter name to delete:\n>').capitalize()
    contacts_i = contacts_index(name) # function returns correct 'contacts' index to work with
    if contacts_i in range(len(contacts)):
        contacts.pop(contacts_i) # removes contact from main 'contacts' list
        print('Contact removed.\n')
    else:
        print('No contact removed.\n')


# function to save edits
def save():
    updated_contents = ','.join(keys) # start of string to save into csv
   
    for dictionary in contacts: # appends to string with a new line for each contact data
        updated_contents += '\n'
        attributes = [dictionary[i] for i in dictionary.keys()]
        updated_contents += ','.join(attributes)

    with open('./contacts.csv', 'w') as f:
        f.write(updated_contents)


input_options = ['e', 'c', 'r', 'u', 'd']
print('\n\n')

#REPL to make CRUD actions
while True:
    
    while True: # while loop to ensure input is allowed
        action = input('Choose one of the following:\n\tCreate a record (c)\n\tRetrieve a record (r)\n\tUpdate a record (u)\n\tDelete a record (d)\n\tExit (e)\n>').lower()
        if action in input_options:
            break
        else:
            print('Invalid input.\n')

    if action == 'e': # exits the program by breaking REPL
        print('Program terminated.')
        break

    if action == 'c':
        create()
        save()
    elif action == 'r':
        retrieve()
    elif action == 'u':
        update()
        save()
    elif action == 'd':
        delete()
        save()
    
    #REPL done, user is notified program will run again
    cont = input('Press enter to continue')
    print('\n\n')
