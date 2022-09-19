# Contact List

f = open("./contacts.csv", 'r', encoding='utf-8')

contents = f.read()

# f.close()

contents = contents.split('\n')

length = len(contents)

for i in range(length):
    y = contents[i]
    y = y.split(',')
    contents[i] = y

keys = contents[0]
key_amount = len(keys)

x = dict.fromkeys(keys, 1)

del contents[0]

y = 0

for i in contents:
    contacts = []
    for i in range(key_amount):
        x[keys[i]] = contents[y][i]
        contacts.append(x)
    y += 1

print(contacts)

choice = input('''Welcome to your contact list.
Type "1" to create a record.
Type "2" to retrieve a record.
Type "3" to update a record.
Type "4" to delete a record.
 ''')

updated_contents = []

if choice == '1':
    
    name = input('Enter the name of the contact you would like to add: ')
    favorite_fruit = input('Enter their favortire fruit: ')
    favorite_color = input('Enter their favorite color: ')
    updated_contact = name + ' ' + favorite_fruit + ' ' + favorite_color
    updated_contact = list(updated_contact)
    print(updated_contact)

    contents = contents.append(name)

print(contents)