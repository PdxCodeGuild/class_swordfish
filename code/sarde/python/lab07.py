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
f = open('lab07.txt')  # --> open the file
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
# print(words)
sentences = contents.split('\n')
number_of_sentences = len(sentences)
# print(sentences)


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
    score = len(single_char_list) / number_of_words / 4.17 + \
        number_of_words / number_of_sentences * 0.5 - 21.43
    rounded_score = math.ceil(score)
    print(score)
    print(rounded_score)
    return score


final_scores = computeARI(
    single_char_list, number_of_words, number_of_sentences)
