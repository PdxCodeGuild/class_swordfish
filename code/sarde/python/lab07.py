'''Lab 7: Compute Automated Readability Index
'''
'''
-Compute the ARI for a given body of text loaded in from a file
-the automated readability index (ARI) is a formula
    for computing the U.S. grade level for a given block of text
'''
'''
4.71(characters) + 0.5 (words) - 21.43
     --------           -----
      words             sentences
-The score is computed by multiplying the number of characters
    -divided by the number of words by 4.71,
    -adding the number of words
    -divided by the number of sentences multiplied by 0.5,
    -and subtracting 21.43
-If the result is a decimal, always round up.
-Scores greater than 14 should be presented
    as having the same age and grade level as scores of 14.
'''

import re
import math
f = open('gettysburg-address.txt')  # --> open the file
contents = f.read()  # --> read the file
# -- print the contents of the file to the console
print(contents)
# print(type(contents))
f.close()  # --> close the file


# Splitting: re.split(pattern, text)
characters_list = list(contents)
# print(characters_list)
# print(type(characters_list))
characters_to_remove = [',', '.', '-', '_', '\n', ' ']
words = contents.split(' ')
number_of_words = len(words)
#print('number of words:', number_of_words)
sentences = contents.split('\n')
number_of_sentences = len(sentences)
# print(sentences)
#print('number of sentences:', number_of_sentences)

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
# print(ari_scale)


def remove_chars(characters_list, characters_to_remove):
    working_list = []
    for i in range(len(characters_list)):
        if characters_list[i] not in characters_to_remove:
            # print(characters_list[i])
            working_list.append(characters_list[i])
    return working_list


single_char_list = remove_chars(characters_list, characters_to_remove)
# print(single_char_list)


def computeARI(single_char_list, number_of_words, number_of_sentences):
    score = 4.17 * len(single_char_list) / number_of_words + \
        0.5 * number_of_words / number_of_sentences - 21.43
    rounded_score = math.ceil(score)
    # print(score)
    # print(rounded_score)
    # scores greater than 14 should be presented as having the same age and grade level as scores of 14.
    if rounded_score >= 14:
        rounded_score = ari_scale[14]
    rounded_score_grade = ari_scale[rounded_score]['grade_level']
    rounded_score_ages = ari_scale[rounded_score]['ages']
    # print(rounded_score_grade)
    # print(rounded_score_ages)
    print(f'The ARI for the gettysburg-address.txt is {rounded_score}')
    print(f'This corresponds to a {rounded_score_grade} level of difficulty')
    print(
        f'that is suitable for an average person {rounded_score_ages} years old.')

    return score


final_scores = computeARI(
    single_char_list, number_of_words, number_of_sentences)
