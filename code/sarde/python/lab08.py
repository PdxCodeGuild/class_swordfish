'''Lab 8: Contact List
'''
'''
Version 1
-build a program to manage a list of contacts
    -build a CSV ('comma separated values'), load file
    -headers might consist of name, favorite fruit, favorite color
    -open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user.
    -the text in the header represents the keys,
    -the text in the other lines represent the values
'''
# load csv file
f = open('contacts.csv')
contents = f.read()
f.close()
print(contents)  # --> prints --> str

# convert the lines of text to a list of dictionaries
# first convert to a dictionary
