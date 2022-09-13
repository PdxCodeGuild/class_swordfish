# ROT Cipher

word = input('Enter a word to encrypt: ')

word = list(word)

letters = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25
    }

element_number = len(word)

code = []

for x in range(element_number):
    x = 0
    letter = word.pop(x)
    number = letters.get(letter)
    number = number + 13
    if number > 25:
        number = number - 26
        code.append(number)
        x += 1
    else:
        code.append(number)
        x += 1

letters = list(letters)

for x in range(element_number):
    x = 0
    letter = code.pop(x)
    letter = letters[letter]
    code.append(letter)
    x += 1

encrypted_word = ''.join(code)

print(f'Your encrypted word is: {encrypted_word}')
