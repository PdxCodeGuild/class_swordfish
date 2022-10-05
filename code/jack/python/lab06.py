# lab 6: ROT13 cipher

import string

letters = string.ascii_lowercase
input_string = input('Enter a string: ').lower()
rot = int(input('Enter rotation (1-26): '))

def encode(x):
    message = [letters[(letters.index(i) + rot) % len(letters)] if i in letters else i for i in x] # is this too dense?
    message = ''.join(message)
    return message

print(encode(input_string))