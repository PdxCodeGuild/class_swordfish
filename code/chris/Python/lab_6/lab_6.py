import string
from typing import final
string.ascii_lowercase
alphabet_list = list(string.ascii_lowercase)
# alphabet_list = list['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(alphabet_list)

rot_13 = input('Please enter an alphabet in for ROT13: ')
# rot_13 = 'snoop'
rot_13_list = list(rot_13)

#print(rot_13_list) #['s', 'n', 'o', 'o', 'p']

def str_index(rot_13_list, lower_case_alphabets):
    index_list = []
    for i, input_letter in enumerate(rot_13_list):
        #print(str(i) + ' ' + letter) #0 s 1 n 2 o 3 o 4 p
        for j, rot_letter in enumerate(lower_case_alphabets): 
            #print(str(i) + ' ' + lower) #for every time snoop appears, the entire alphabet list is printed off
            if input_letter == rot_letter: #will execute remaining if input_letter is same as rot_letter
                the_index_number = j
                index_list.append(the_index_number)
    return index_list

#print(str_index(rot_13_list, alphabet_list)) #[18, 13, 14, 14, 15]

new_index_list = str_index(rot_13_list, alphabet_list) #storing function in new_index_list variable

def shift_list(new_index_list, ROT = 13):
    for i in range(len(new_index_list)):
        new_index_list[i] = new_index_list[i] - ROT
    return new_index_list

#print(shift_list(new_index_list)) #[5, 0, 1, 1, 2]

converted_rot_list = shift_list(new_index_list, ROT = 13)

#print(converted_rot_list) #[5, 0, 1, 1, 2]

rot13_converted = [alphabet_list[i] for i in converted_rot_list]
rot_13_joined = "".join(rot13_converted)
print(rot_13_joined) #fabbc

one_liner = ""

for a in converted_rot_list:
    one_liner += alphabet_list[a]
    
#print(one_liner) #fabbc

v = 1
max = 3
percentage = str((v / max) * 100) + "%"
print(percentage)