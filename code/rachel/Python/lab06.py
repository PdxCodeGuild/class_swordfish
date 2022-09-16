#ROT Cipher
#ask the user to input a string of characters
#create an index to encrypt / decrypt input
    #make a list of each character & add 13 to index (since there are 26 letters, encryption is same as decryption)
        # turn input into list? indexes seem to work on both lists and strings but IDK about every method / tool works the same
            #use print(input[#]) to get a character at a certain index (see Strings doc)
            #create def so that all the returned letters can be printed out together
        # for every inputted letter from string, add 13 and output that letter
    # make a loop that goes thru every element in the string:
        # while i in input_string != 0, do this
    # make a loop that ensures index / numbers do not go over 26
        # if i > 26, loop back to beginning of index

cipher_key = "abcdefghijklmnopqrstuvwxyz"
input_phrase = input("Enter a string of letters to encypher: ")
key = 13

#this returns each index position on a seperate line:
# for ind in input_phrase:
#     answer = cipher_key.index(ind)
#     print(answer)
###########
#this also returns each index position on a seperate line:
# for ind in input_phrase:
#     answer = []
#     for char in input_phrase:
#         answer += [cipher_key.index(char)]
#     print(answer)
##########
#this returns [0, 1] on two rows (when input = ab)
# for ind in input_phrase:
#     answer = [cipher_key.index(char) for char in input_phrase]
#     print(answer)
#########
#this also returns [0, 1] (when input = ab)
def rot_cypher():
    for ind in range(len(input_phrase)):
        position = [cipher_key.index(char) for char in input_phrase]
        return position
        #output_letter = cipher_key.index(cipher_key[i] + key) #cipher_key returns letter in cipher_key
        #output_letter = 'input_phrase'.find[i]
        #print(input_phrase.find[i])
print(rot_cypher())
##########
def encryption(position):
    position = rot_cypher() 
    position2 = []
    for i in range(len(position)):
        position2 = i + 13 
    return position2
print(encryption()) #repeated TypeError: encryption() missing 1 required positional argument: 'position' no matter where I put position - maybe it's just when creating functions and not really running them yet beyond print
for i in encryption():
    position = rot_cypher()
    position2 = encryption(position)
print(position2)
#   conversions = cipher_key[i]
    

# def ROT13():
#     encrypted_phrase= " "
#     for i in range(len(input_phrase)):
#        char = input_phrase(i) 
#     encrypted_phrase += cipher_key(ord(char) + key)
#     return encrypted_phrase




 
