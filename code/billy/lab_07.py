'''
program: lab_07
author: billy frick
date: 15 september 2022

function:

'''

# imports #
import re
import math

# variables #
words = 0

sentences = 0

# this dictionary will allow the variable 'automated_readability_index' to grab the age and grade level. #
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

# this will open the text file, and assign it to a variable. #
# The character count, number of sentences and words will also be assigned to variables. #
# The ARI will then be calculated using the formula seen on line 54, and rounded up on line 56. #
with open(r'advanced_reading.txt', 'r') as file:

    book_title = file.name

    book = file.read()

    book_lines = book.split()

    words += len(book_lines)

    characters = len(book)

    sentences += book.count('.')

    automated_readability_index = 4.71 * (characters // words) + 0.5 * (words // sentences) - 21.43

    automated_readability_index = math.ceil(automated_readability_index)

# Ensures any ari greater than 14 will be accounted for. #
if automated_readability_index > 14:

    automated_readability_index = 14

# grabs age and grade level from dict, based on the ari. #
ari_grade_level = ari_scale[automated_readability_index]['grade_level']

ari_age = ari_scale[automated_readability_index]['ages']

# prints ari, ghrade level and age in a format that is readable for the user. #
print("\n----------------------------------------------------")

print("> The ARI for", book_title , "is", automated_readability_index)

print("> This corresponds to a(n)", ari_grade_level, "level of difficulty.")

print("> That is suitable for for an average person", ari_age, "years old.")

print("----------------------------------------------------\n")

# end #