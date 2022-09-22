import string

letters = string.ascii_lowercase
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',]

# print(letters_list)
user_string= input("Enter a word to encode it: ")
user_list = list(user_string)

index_numbers = []
encoded_word =[]
def encoding_index(a):
    """finds the index number in a corresponding list"""
    for i, char in enumerate(user_list):
        if user_list[::] in enumerate(letters_list):
            encoded_letter = letters_list[[i +13]]
            print(encoded_letter)
            encoded_word.append(encoded_letter)
            return encoded_word

encoded_word = encoding_index(user_string)
print(encoded_word)




# def finding_indexes_in_list(working_list, new_list):
#     for i in range(len(working_list)):
#          # print(working_list[i])
#         for j in range(len(new_list)):
#             # print(new_list[j])                                           
#             if new_list[j] == working_list[i]:
#                 the_letter = working_list[i]
#                 the_index = j
#                 return index_numbers
#                 encoded_string = letters[the_index]
         
#                 print(the_index, the_letter, encoded_string)

# print(finding_indexes_in_list(user_string, letters))






    # for indx in range(len(letters)):
    #     if letters[indx] == working_list:
    #         matched_indicies.append()
    #         return matched_indicies

# finding_indexes_in_list(user_list, letters_list)

# print(finding_indexes_in_list(user_string, letters))


    


