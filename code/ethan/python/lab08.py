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