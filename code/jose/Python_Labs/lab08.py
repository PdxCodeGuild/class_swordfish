import re

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)
copy_of_lines = lines.copy()

start_keys = lines[0]
keys = start_keys.split(",")                        #this creates a dictionary with Keys:value of None
contact_dict = {}
split_lines = []
for line in lines[1::]:                             #splits each line into its own dictionary and itterates
    split_line = line.split(",")                    #through each line to add into its matching 'key'
    contact_dict = dict(zip(keys, split_line))
    split_lines.append(contact_dict)
# print(contact_dict)
# print(split_lines)
copy_of_split_lines = split_lines.copy()

# # # print(split_lines)
def new_user():
    create_user = input('Enter your name, favorite fruit, and favorite color: ')
    user_line = re.split('[. ]', create_user)
    user_line = ''.join(user_line)
    with open('contacts.csv', 'a') as file:
        file.write('\n')
        file.write(user_line)
        return

def get_user_info():
    retrieve_user = input('What is the name of the record you wish to retrieve?: ')

    for i, contact in enumerate(split_lines):
        if retrieve_user == contact['name']:
            print(contact)
            return

def update_user_info(): 
    update_user = input("What contact would you like to update?: ")
    update_value = input('What attribute do you want to change?: ')
    new_user_value = input("what do you want your new attribute to be?: ")

    for i, contact in enumerate(split_lines):
        if update_user == contact['name']:
            if update_value == contact ['favorite color']:
                contact['favorite color'] = new_user_value
            if update_value == contact['favorite fruit']:
                contact ['favorite fruit'] = new_user_value 
            return split_lines

def remove_user():
    delete_user = input('What user contact would you like to remove?: ')

    for i, contact in enumerate(split_lines):
        if delete_user == contact['name']:
            split_lines.pop(i)
            return


user_request = input('What would you like to do?(create new user/ retrieve user info/ update user info/ delete user):')

while True:
    if user_request == 'create new user':
        print(new_user())
        break
    elif user_request == 'retrieve user info':
        print(get_user_info())
        break
    elif user_request == 'update user info':
        print(update_user_info())
        break
    elif user_request == 'delete user':
        print(remove_user())
        break
    elif user_request == 'exit':
        break
    else:
        print('Invalid option, please try again')
        break
        
print(copy_of_split_lines)

lines = [','.join(split_lines)]
for contact in split_lines: # loop over contacts
    row = ','.join(contact.values()) # turn contact values into comma separated string
    lines.append(row)  # add row to lines

    csv = '\n'.join(lines) # turn lines list into string
# new_lines = []
# print(split_lines)
# for i, dict in enumerate(split_lines):
#     new_lines.append(dict)
    

  
# print(new_lines)
    








    

