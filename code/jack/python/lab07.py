import math
import string

file_name = 'gettysburg_address.txt'

with open(file_name, 'r') as f:
    book_lines = f.read().split('\n')

sentances = 0
characters = 0
words = 0

for line in book_lines:
    for character in line:
        if character in string.ascii_letters:
            characters += 1
        if character == ' ':
            words += 1 #each word is followed by a space, except if the word is at the end of the string
        elif character == '.' or character == '?' or character == '!':
            sentances += 1

words += len(book_lines) # accounts for words at end of strings not counted by the space

ari = math.ceil((4.71 * (characters / words)) + (0.5 * (words / sentances)) - 21.43)
print(ari)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

age = ari_scale[ari]['ages']
grade = ari_scale[ari]['grade_level']

print(f'The ARI for {file_name} is {ari}\nThis corresponds to a {grade} Grade level of difficulty\nthat is suitable for an average person {age} years old.')

# print(f'characters: {characters}')
# print(f'words: {words}')
# print(f'sentances: {sentances}')