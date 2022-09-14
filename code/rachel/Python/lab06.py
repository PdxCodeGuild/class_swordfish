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

cipher_key = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

input_phrase = input("Enter a string of letters to encypher: ")

def rot_cypher():
    for i in input_phrase: 
        output_letter = cipher_key[i + 13]
        return (output_letter)

while i in input_phrase != 0:
    rot_cypher()
 
