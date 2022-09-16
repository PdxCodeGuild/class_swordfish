'''Lab 6: ROT Cipher
'''
'''
-Write a program that prompts the user for a string, and encodes it with ROT13
-For each character, find the corresponding character
-add it to an output string.
NOTE: ROT13-replaces a letter with the 13th letter after it in the alphabet 
'''

alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
    'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}
print(alphabet)
rot_13_alpahabet_start = alphabet[13]  # -->??
print(rot_13_alpahabet_start)
input_string = input('Enter a word:')


def rotate_by_13(input_string, alphabet):
    # iterate over the alphabet list
    # if the current letter in the input_string is equal to the letter in the alphabet list
    # subtract by 13 to get letter
    rotate_13 = 13
    for i in alphabet:
        if i == alphabet[i]:
            print(alphabet[0] + rotate_13)


rotate_by_13(input_string)
