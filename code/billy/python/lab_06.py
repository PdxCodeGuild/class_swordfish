'''
program: lab_06
author: billy frick
date: 13 september 2022

function: this program will prompt a user for a string, and encode it with ROT13. An output string will then be displayed.

'''

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# function for ROT13 encryption
def rot_encryption(decrypt, encrypt):
    
    rot_text = ''

    # takes the each letter that was entered and uses variable "alphabet" to have a list of strings to convert with.
    for letters in decrypt:

        if letters in alphabet:
            
            # creates index based off of alphabet variable and the users input.
            # modulus (%) 26 will account for all 26 letters, and take the remainder of anything above 26, and loops around the alphabet.
            rot_cypher_index = (alphabet.index(letters) + encrypt) % 26

            # creates variable 'rot_text' which recieves the converted strings from rot_cypher_index.
            rot_text = rot_text + alphabet[rot_cypher_index]

    # returns so 'None' appears
    return rot_text

decrypt = input("\n> please enter a message to have encrypted: ")

# changes users input to all lower case strings so there are no errors.
decrypt = decrypt.lower()

# determines the amount that each letter will be encryoted by.
encrypt = input("\n> how many letters would you like to encrypt by? (please enter a number): ")

# converts str to int so it can be encrypted properly.
encrypt = int(encrypt)

print(rot_encryption(decrypt, encrypt))