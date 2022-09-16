import re
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

# Split each row of info into a list stored in a list
contacts = []                           
for i in range(len(lines)):
    contacts.append(re.split('[,]', lines[i]))

keys = contacts.pop(0)  # Popped the first row out to use as the keys for the dict.

cont_list=[]            # List place holder for the end product of list of dicts.

# Loop through contact list and zip together with keys to create tuples, turn them to a dict, and append them to the cont_list.
for sublist in contacts:
    cont = dict(list(zip(keys, sublist)))
    cont_list.append(cont)

# Function for Create part of CRUD
def create():
    name = input('Please input name you would like to add: ')
    city = input('Please input city you would like to add: ')
    country = input('Please input country you would like to add: ')
    add = {'name': name, 'city': city, 'country': country}
    cont_list.append(add)

# Functino for Retrieve part of CRUD
def retrieve():
    while 'name' != name:
        name = input('Please enter the name of the person you would like to look up: ')
        if cont_list('name') == name:
            print(cont_list.get('city', 'country'))
            break
    else:
        name = input('Name is not in our files.  Please enter another: ')


retrieve()
# create()
print(cont_list)