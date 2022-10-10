# Compute Automated Readability Index

import re
import math

    # Score  Ages     Grade Level
    #  1       5-6    Kindergarten
    #  2       6-7    First Grade
    #  3       7-8    Second Grade
    #  4       8-9    Third Grade
    #  5      9-10    Fourth Grade
    #  6     10-11    Fifth Grade
    #  7     11-12    Sixth Grade
    #  8     12-13    Seventh Grade
    #  9     13-14    Eighth Grade
    # 10     14-15    Ninth Grade
    # 11     15-16    Tenth Grade
    # 12     16-17    Eleventh grade
    # 13     17-18    Twelfth grade
    # 14     18-22    College

f = open("./we-shall-fight-on-the-beaches.txt", 'r', encoding='utf-8')

contents = f.read()

f.close()

all_characters = len(list(contents))

spaces = len(re.findall(r' ', contents))

character_count = all_characters - spaces

word_count = len((re.split('[ ]', contents)))

sentence_count = len((re.split('[.?!]', contents)))

# print(character_count)
# print(word_count)
# print(sentence_count)

ari = 4.71 * (character_count/word_count) + 0.5 * (word_count/sentence_count) - 21.43

ari = float(ari)
ari = math.ceil(ari)

# print(ari)

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

gradelevel = ari_scale[ari]['grade_level']
age = ari_scale[ari]['ages']


print(f'''The ARI for we-shall-fight-on-the-beaches.txt is {ari}.
This cooresponds to a {gradelevel} level of difficulty
that is suitable for an average person {age} years old.''')