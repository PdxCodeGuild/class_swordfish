import re
with open('contacts.csv', 'r') as file: # Retrieves .csv file, reads it, and splits it into lists.
    lines = file.read().split('\n')

contacts = []       # Split each row of info into a list stored in a list  
for i in range(len(lines)):
    contacts.append(re.split('[,]', lines[i]))

keys = contacts.pop(0)  # Popped the first row out to use as the keys for the dict.

cont_list=[]            # List place holder for the end product of list of dicts.

# Loop through contact list and zip together with keys to create tuples, turn them to a dict, and append them to the cont_list.
for sublist in contacts:
    cont = dict(list(zip(keys, sublist)))
    cont_list.append(cont)

def check(name):                # Name check to ensure name is in database.
    check = [1 for i in range(len(cont_list)) if cont_list[i]['name'] == name]
    while len(check) == 0:
        name = input('Name does not match anything in our records. Please enter a new name: ').title()
        check = [1 for i in range(len(cont_list)) if cont_list[i]['name'] == name]
    return name

def create():       # Function for Create part of CRUD.
    name = input('Please input name you would like to add: ').title()
    city = input('Please input city you would like to add: ').title()
    country = input('Please input country you would like to add: ').title()
    add = {'name': name, 'city': city, 'country': country}
    cont_list.append(add)

def retrieve():     # Function for Retrieve part of CRUD.
    name = input('Please enter the name of the person you would like to look up: ').title()
    name = check(name) 
    info = [(f"{cont_list[i].get('city')}, {cont_list[i]['country']}") for i in range(len(cont_list)) if cont_list[i]['name'] == name] # Pulls all info from the name entered.
    return info[0]

def update():       # Function for Update part of CRUD.
    name = input('Please enter the name you would like to update: ').title()
    name = check(name)
    attr = input('Which attribute would you like to update? City or Country?: ').lower()
    while attr != 'city' and attr != 'country':     # Attribute check to make sure it is the proper input.
        attr = input('Invalid selection. Please select City or Country: ').lower()
    change = input('What would you like the new value to be: ').title()
    for i in range(len(cont_list)):                 # Making the attribute change.
        if cont_list[i]['name'] == name:
            cont_list[i][attr] = change
            break
    return cont_list

def delete():
    name = input('Please enter the name associated with the record you would like to remove: ').title()
    name = check(name)
    for i in range(len(cont_list)):
        if cont_list[i]['name'] == name:
            cont_list.pop(i)
            break


# update()
create()
print(cont_list)
delete()
# print(retrieve())
print(cont_list)