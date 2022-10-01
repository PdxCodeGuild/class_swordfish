#ARI
import math
import pprint
#number of characters
file = open("myfile.txt", "r")
myfile = file.read().replace(" ","")
characters = len(myfile)
#print('Number of characters in text file: ', characters)

#number of words
file = open("myfile.txt", "r")
myfile = file.read()
words = myfile.split()
#print('Number of words in text file: ', len(words))

#number of sentences
with open("myfile.txt") as f:
    data = f.read()
    #print ("total stops: ", data.count("."))

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

#===================================================================================
# pprint.pprint(ari_scale)
# print(ari_scale[1])
# print(ari_scale[1]['ages'])
# print(ari_scale[1].keys())
# print(ari_scale[1].values())
print(ari_scale[1].items())

# print(ari_scale[9]['grade_level'])
#===================================================================================
words = 280
characters = 1359
sentences = 11
x = 4.71
y = 21.43
z = .5

score = math.ceil(x * (characters / words) + z * (words / sentences) - y)

if score > 14:
    score = 14

# print("The age range is", ari_scale[score]['ages'], "for the",ari_scale[score]['grade_level'])
# print(ari_scale[score]['grade_level'])

# print("Score: ", score)

ages = ari_scale[score]['ages']
level = ari_scale[score]['grade_level']


ari_string = f'The age range is {ages} for the {level} level'
print(ari_string)