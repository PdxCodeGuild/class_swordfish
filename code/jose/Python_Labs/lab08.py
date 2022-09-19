
import re


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

start_keys = lines[0]
keys = start_keys.split(",")                        #this creates a dictionary with Keys:value of None
contact_dict = {}
split_lines = []
for line in lines[1::]:                             #splits each line into its own dictionary and itterates
    split_line = line.split(",")                    #through each line to add into its matching 'key'
    contact_dict = dict(zip(keys, split_line))
    split_lines.append(contact_dict)

# print(split_lines)


# # print(split_lines)
create_user = input('Enter your name, favorite fruit, and favorite color: ')
user_line = re.split('[. ]', create_user)
user_line = ''.join(user_line)
with open('contacts.csv', 'a') as file:
    file.write('\n')
    file.write(user_line)

retrieve_user = input('What is the name of the record you wish to retrieve?: ')

for i, contact in enumerate(split_lines):
    if retrieve_user == contact['name']:
        print(contact)

update_user = input("What would you like to update?: ")
new_user_value = input("what do you want your new attribute to be?: ")

for i, contact in enumerate(split_lines):
    if update_user == contact['favorite fruit']:
        contact['favorite fruit']= new_user_value
    if update_user == contact['favorite color']:
        contact['favorite color']= new_user_value
print(new_user_value)
print(contact)
       


        # contact['favorite fruit'] = update_user
        # print(contact)
    
    


# if retrieve_user == split_lines(retrieve_user):
    
    # print(split_lines[{retrieve_user}])

    








    

