'''Lab 6: ROT Cipher
'''
'''
-Write a program that prompts the user for a string, and encodes it with ROT13
-For each character, find the corresponding character
-add it to an output string.
NOTE: ROT13-replaces a letter with the 13th letter after it in the alphabet
'''

alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}
# print(alphabet)
rot_13_alphabet = {
    0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd',
    5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
    10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
    15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
    20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
    25: 'y'
}
# print(rot_13_alpahabet)


def rotate_by_13(alphabet, rot_13_alphabet):
    input_string = input('Enter a word:')
    rotate_13 = 13
    # iterate over letters in the alphabet list
    for letter in input_string:
        # checks for spaces
        if (letter != ' '):
            # adds + 13 to the current index
            number = (alphabet[letter] - rotate_13 + 26) % 26
            print(number)


rotate_by_13(alphabet, rot_13_alphabet)
