# Contact List

f = open("./contacts.csv", 'r', encoding='utf-8')

contents = f.read()

f.close()

contents = contents.split('\n')

length = len(contents)

for i in range(length):
    y = contents[i]
    y = y.split(',')
    contents[i] = y

<<<<<<< HEAD
answer = input('Would you like to alter your contact list?: ')

updated_contact = [0,1,2]

while answer == 'yes':
    choice = input('''
Type "1" to create a record.
Type "2" to retrieve a record.
Type "3" to update a record.
Type "4" to delete a record.
    ''')
    if choice == '1':
        
        name = input('Enter the name of the contact you would like to add: ')
        updated_contact[0] = name
        favorite_fruit = input('Enter their favorite fruit: ')
        updated_contact[1] = favorite_fruit
        favorite_color = input('Enter their favorite color: ')
        updated_contact[2] = favorite_color

        contents.append(updated_contact)
        answer = input('Would you like to change anything else?: ')
    elif choice == '2':
        name = input('Which contact would you like to retrieve?: ')
        p = 0
        for i in contents:
            if name in contents[p]:
                print(f'Contact name: {contents[p][0]} \nFavorite fruit: {contents[p][1]} \nFavorite color: {contents[p][2]}')
            p += 1
        answer = input('Would you like to change anything else?: ')
    elif choice == '3':
        name = input('Which contact would you like to update?: ')
        p = 0
        for i in contents:
            if name in contents[p]:
                attribute = input('Which attribute would you like to update? ')
                if attribute == 'name':
                    new_name = input('Please enter the new name.: ')
                    print(f'Contact {contents[p][0]} {attribute} changed to {new_name}.')
                    contents[p][0] = new_name
                elif attribute == 'favorite fruit':
                    new_fruit = input('Please enter the new favorite fruit: ')
                    print(f'Contact {contents[p][0]} {attribute} changed to {new_fruit}.')
                    contents[p][1] = new_fruit
                elif attribute == 'favorite color':
                    new_color = input('Please enter the new favorite color: ')
                    print(f'Contact {contents[p][0]} {attribute} changed to {new_color}.')
                    contents[p][2] = new_color

            p += 1
        answer = input('Would you like to change anything else?: ')
    elif choice == '4':
        name = input('Which contact would you like to delete?: ')
        p = 0
        for i in contents:
            if name in contents[p]:
                print(f'Contact {name} deleted.')
                del contents[p]
            p += 1
        answer = input('Would you like to change anything else?: ')

new_length = len(contents)

keys = contents[0]

key_amount = len(keys)

x = dict.fromkeys(keys, 1)

del contents[0]

y = 0

<<<<<<< HEAD
contacts = []

for i in contents:
    x = {}
    for i in range(key_amount):
        x[keys[i]] = contents[y][i]
    contacts.append(x)
    y += 1

updated_contacts = [list(_.values()) for _ in contacts]

updated_contacts.insert(0, keys)

new_contacts =[]

for i in range(0, len(updated_contacts)):            # Takes it back to a list of stings as it was when first imported for the .csv doc.
    new_contacts.append(','.join(updated_contacts[i]))

new_contacts = '\n'.join(new_contacts)

with open('./contacts.csv', 'w') as f:
    f.write(new_contacts)
