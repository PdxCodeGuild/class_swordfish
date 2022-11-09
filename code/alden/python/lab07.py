import math
import re
from xml.dom.pulldom import CHARACTERS
# Automated Readability index dictionary reference.
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

# Input of my text document.
with open('Gatsby.txt', 'r') as f:
    cont = f.read()

# Splits out at punctuations to get number of sentances.
cont = re.split('[.]', cont)
sentences = int(len(cont) -1)   
cont = ''.join(cont)            # Joins back to a string

# removes commas
cont = re.split(",", cont)      

# Splits out number of words
cont = ''.join(cont)
cont = cont.split()             
words = len(cont)

# Splits in to letters
cont = ''.join(cont)
cont = re.split('[a-zA-Z]', cont)
characters = len(cont)

# Does the math for these variables before puting them into the formula.
x = (characters/words)
y = (words/sentences)

# ARI formula
ari = math.ceil(4.71 * x + 0.5 * y  - 21.43)

# Recalls the info from ari_scale dictionary.
grade = ari_scale[ari]['grade_level']
age = ari_scale[ari]['ages']

print(f'The ARI for Gatsby.txt is {ari}.')
print(f'This corresponds to a {grade} of difficulty.')
print(f'That is suitable for an average person {age}')
