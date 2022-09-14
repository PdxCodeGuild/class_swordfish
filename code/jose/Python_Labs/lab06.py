import string

letters = string.ascii_lowercase
letters_list = list(letters)

# user_string = input('Please type in what you want encoded: ')
# user_string = (list(user_string))
user_string= input("Enter a word to encode it: ")
user_list = list(user_string)

index_numbers = []

def find_index(a):
    """finds the index number in a corresponding list"""
    for i in enumerate(index_numbers):
        index_numbers.append(i)
        print(index_numbers)
        return index_numbers

print(find_index(user_string))



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


    


