import re

with open('gettysburg_addy.txt') as f:
    getty = f.read()

# print(getty)

#[a-zA-Z]+\w+[.?!$] #letters, words and sentences

letters = re.split('[a-zA-Z]', getty)
# print(letters)
words = re.split('\s+', getty)
# print(words)
sentences = re.split('[.]', getty)
# print(sentences)

letters_count = (len(letters))
# letters_count = float(letters_count)
# print(letters_count)
words_count = (len(words))
# words_count = float(words_count)
# print(words_count)
sentence_count = (len(sentences))
# sentence_count = float(sentence_count)
# print(sentence_count)


ari = int((4.71 * (letters_count / words_count)) + ((0.5) * (words_count / sentence_count)) - 21.43)

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

age = ari_scale[ari]['ages']
# print(age)
grade_level = ari_scale[ari]['grade_level']
# print(grade_level)

# ari_ages = list(ari_scale.keys())
# print(ari_ages)

# while ari == ari_scale:
#     print((ari_scale.values()))

print(f'''The ARI for gettysburg_address.txt is {ari} 
This corresponds to a {grade_level} Level of difficulty 
that is suitable for an average person of {age} years old.''')