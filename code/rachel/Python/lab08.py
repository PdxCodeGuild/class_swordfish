import csv
"""Version 1: Build a program to manage a list of contacts. Build a CSV with names, colors, fruit; headers might consist of name, favorite fruit, favorite color. Open CSV, convert lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values. """
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    new_lists = [line.split(',') for line in lines] #turn those strings into their own list of things to work with: [['name', 'favorite color', 'favorite fruit'], ['bob', 'green', 'cherry'], ['julia', 'yellow', 'pineapple'], ['manny', 'red', 'apple'], ['debby', 'purple', 'kiwi']]
    #print(new_lists)
headers = new_lists.pop(0) #pop out first list
#print(headers) #['name', 'favorite color', 'favorite fruit']
#print(new_lists) #[['bob', 'green', 'cherry'], ['julia', 'yellow', 'pineapple'], ['manny', 'red', 'apple'], ['debby', 'purple', 'kiwi']]
"""Now we need a function that will pull each list out and then zip it to the first list in a loop / list comprehension. End result is a list of seperate dictionaries"""
def list_builder(funny, new_lists): #parameter names only apply to the function definition; they are simply placeholders
    local_list = []
    for list in new_lists:
        sing_dict = dict(zip(funny,list))
        local_list.append(sing_dict)
    return local_list
#print(list_builder(headers, new_lists)) #this is where I tell it to use the particular lists I want it to use
contact_list = list_builder(headers, new_lists)
#print(contact_list)
"""Version 2: Implement a CRUD REPL: 
Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered."""
decision1 = input('To enter your contact information, enter "new user". If you already have entered your information, enter "verify" to verify your information or "delete" to erase your information ')
if decision1 == 'new user':
    #local_list = list_builder()
    user_name = input("Enter your first name: ")
    fav_color = input("Enter your favorite color: ")
    fav_fruit = input("Enter your favorite fruit: ")
    new_user = {
        'name': user_name,
        'favorite color': fav_color,
        'favorite fruit': fav_fruit
        }
    contact_list.append(new_user)
    print(new_user)
    #print(contact_list)
    """Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information"""
elif decision1 == 'verify':
    user_name = input('Please verify your information. What is your first name? ')
    match = next((l for l in contact_list if l['name'] == user_name)) #match the user_name to the name value and return the entire dictionary the name was found in
    print(match)
    """Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set."""
    decision2 = input('If your information is correct enter "quit", and if not, enter "update" ')
    if decision2 == 'update':
    #while decision2 == 'update':
        update_key = input('Enter the field that needs to be updated ')
        update_value = input('Enter the correct information ')
        if update_key == 'name':
            match['name'] = update_value
        elif update_key == 'favorite color':
            match['favorite color'] = update_value
        elif update_key == 'favorite fruit':
            match['favorite fruit'] = update_value
        print(match)
        contact_list.append(match)
        #print(contact_list)
    """Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list."""
elif decision1 == 'delete':
    user_name = input('What is the first name of the record you want to delete? ')
    for i in range(len(contact_list)):
        if contact_list[i]['name'] == user_name:
            del contact_list[i]
            break
    print('Your record has been deleted')
    #print(contact_list)           
with open ('contacts.csv', 'w') as csvfile:
    writer = csv.DictWriter (csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(contact_list)


