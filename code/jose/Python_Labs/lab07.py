import re

with open('gettysbergaddress.txt', 'r') as f:
    contents = f.read()

sentences = contents.split('. ')           #splits the sentences by a period, added +1 since it wont count the final sentence
num_of_sentences = len(sentences)

words_list = re.split('[,. ]', contents)   #splits the contents by the puntuacion and spaces between words

for i, char in enumerate(words_list):      #removing the spaces in between words since the list is currently including them
    if words_list[i] == '':               #inflating my score
        words_list.pop(i)

character_list = []                         #splits the whole text to a list of individual characters
character_list.extend(contents)

for i, char in enumerate(character_list):   #same as words_list comment on line 11, removing extra spaces between characters
    if character_list[i] == ' ':
        character_list.pop(i)

amount_of_char = len(character_list)
amount_of_words = len(words_list)

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

ari = 4.71*(amount_of_char/amount_of_words) + 0.5*(amount_of_words/num_of_sentences) - 21.43

response_ari = round(ari)

if response_ari in ari_scale:
    print("The ARI for the gettysburg-adress.txt is " + str(response_ari))
    print('This corresponds to a ' + (ari_scale[response_ari]['grade_level']) +' level of dificulty')  #printing out while looking
    print("That is suitable for a person between ages " + ari_scale[response_ari]['ages'])             #though the dict. using 
                                                                                                         #key index values




# output_response = "The ARI for the gettysburg-adress.txt is" + str(response_ari) + "\nThis corresponds to an"+ ari_scale([response_ari['grade level']] +' level of dificulty' + "\nThat is suitable for a person between ages" + ari_scale([response_ari['ages']]))

# print(output_response)
# print(response_ari)

# The ARI for gettysburg-address.txt is 12
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.

# print(amount_of_char, "number of characters")
# print(amount_of_words, "number of words")
# print(num_of_sentences, "number of sentences")
# print(sentences)