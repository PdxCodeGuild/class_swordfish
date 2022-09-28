import string

# letters = string.ascii_lowercase
letters_dict = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 
'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}

# # print(letters_list)
# user_string= input("Enter a word to encode it: ")
# user_list = list(user_string)



    
# print(index_numbers)
def encrypt_string (user_string):
    """function encrypts works by iterating through each value in a string and changes it with a dictionary of encrypting letters"""
    letters_dict = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 
    'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
    'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}
    encrypted_word = ''
    for char in user_string:
        if char in letters_dict.keys():
            encrypted_word += letters_dict[char]

    return encrypted_word
print(encrypt_string(input('Please enter a word to encrypt or decrypt: ')))
# print(encoded_word)






    


