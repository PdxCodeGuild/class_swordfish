

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

import string

def loud_text(text):
    text_list = list(text.upper())
    text_str = '-'.join(text_list)
    return text_str

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'



# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    word_list = []
    for i in word:
        word_list.append(i + i)
    word_doubled = ''.join(word_list)
    return word_doubled

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):
    total = 0
    for i in word:
        if i == letter:
            total += 1
    return total

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word): #uppercase kind of breaks this
    chr_num = 0
    for i in word:
        if ord(i) > chr_num:
            chr_num = ord(i)
    chr_str = chr(chr_num)
    return chr_str

def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    count = 0
    for i in range(len(text)):
        if text[i] == 'h':
            if text[i + 1] == 'i':
                count += 1
    return count

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    text_lower = text.lower()
    text_list = list(text_lower)
    for x in list(text_list):
        if x in string.punctuation:
            text_list.remove(x)
    text_str = ''.join(text_list)
    text_underscore = text_str.replace(' ', '_')
    return text_underscore

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    text_lower = text.lower()
    text_list = list(text_lower)
    for i in range(len(text_list)):
        if text_list[i] == ' ':
            text_list[i + 1] = text_list[i + 1].upper()
            text_list[i] = '_'
    for x in list(text_list):
        if x in string.punctuation:
            text_list.remove(x)
    text_complete = ''.join(text_list)
    return text_complete

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    text_list = []
    toggle = True
    for x in text:
        if toggle == True:
            toggle = False
            text_list.append(x.upper())
        else:
            toggle = True
            text_list.append(x.lower())
    text = ''.join(text_list)
    return text


def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'