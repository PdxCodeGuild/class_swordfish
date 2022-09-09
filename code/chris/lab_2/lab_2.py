import numbers

number = input(f'Please input a numeric number to be converted to a numeric phrase: ')
number = int(number)

hundreds_num_list = [' ', 'hundred', 'two-hundred', 'three-hundred', 'four-hundred', 'five-hundred', 'six-hundred', 'seven-hundred', 'eight-hundred', 'nine-hundred']
tens_num_list = [' ', ' ', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'] #don't forget the ' ' space to account for gaps in list
ones_num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

x = number
hundred_digit = x//100
tens_digit = x%100//10  #make sure you remember this - modulus to take off the 100s place and then floor divide with what is left
ones_digit = x%10

hundred_word = hundreds_num_list[hundred_digit]

tens_word = tens_num_list[tens_digit]

ones_word = ones_num_list[ones_digit]

result_string = hundred_word + ' ' + tens_word + '-' + ones_word

if hundred_digit == 0 and tens_digit == 0 and ones_digit == 0:
    print('Zero')
elif hundred_digit == 0 and tens_digit == 0 and ones_digit == 1:
    print('One')
elif hundred_digit == 0 and tens_digit == 0 and ones_digit == 2:
    print('Two')
elif hundred_digit == 0 and tens_digit == 0 and ones_digit == 3:
    print('Three')
elif hundred_digit == 0 and tens_digit == 0 and ones_digit == 4:
    print('Four')
elif hundred_digit == 0 and tens_digit == 0 and ones_digit == 5:
    print('Five')
elif hundred_digit == 0 and tens_digit == 0 and ones_digit == 6:
    print('Six')
elif hundred_digit == 0 and tens_digit == 0 and ones_digit == 7:
    print('Seven')
elif hundred_digit == 0 and tens_digit == 0 and ones_digit == 8:
    print('Eight')
elif hundred_digit == 0 and tens_digit == 0 and tens_digit == 0 and ones_digit == 9:
    print('Nine')
elif hundred_digit == 0 and tens_digit == 1 and ones_digit == 0:
    print('Ten')
elif hundred_digit == 0 and tens_digit >= 1 and tens_digit < 2 and ones_digit == 1:
    print('Eleven')
elif hundred_digit == 0 and tens_digit >= 1 and tens_digit < 2 and ones_digit == 2:
    print('Twelve')
elif hundred_digit == 0 and tens_digit >= 1 and tens_digit < 2 and ones_digit == 3:
    print('Thirteen')
elif hundred_digit == 0 and tens_digit >= 1 and tens_digit < 2 and ones_digit == 4:
    print('Fourteen')
elif hundred_digit == 0 and tens_digit >= 1 and tens_digit < 2 and ones_digit == 5:
    print('Fifteen')
elif hundred_digit == 0 and tens_digit >= 1 and tens_digit < 2 and ones_digit == 6:
    print('Sixteen')
elif hundred_digit == 0 and tens_digit >= 1 and tens_digit < 2 and ones_digit == 7:
    print('Seventeen')
elif hundred_digit == 0 and tens_digit >= 1 and tens_digit < 2 and ones_digit == 8:
    print('Eighteen')
elif hundred_digit == 0 and tens_digit >= 1 and tens_digit < 2 and ones_digit == 9:
    print('Nineteen')
else:  
    print(result_string)

# if hundred_digit == 9:
#     hundred_word = hundreds_num_list[8]
# elif hundred_digit == 8:
#     hundred_word = hundreds_num_list[7]
# elif hundred_digit == 7:
#     hundred_word = hundreds_num_list[6]
# elif hundred_digit == 6:
#     hundred_word = hundreds_num_list[5]
# elif hundred_digit == 5:
#     hundred_word = hundreds_num_list[4]
# elif hundred_digit == 4:
#     hundred_word = hundreds_num_list[3]
# elif hundred_digit == 3:
#     hundred_word = hundreds_num_list[2]
# elif hundred_digit == 2:
#     hundred_word = hundreds_num_list[1]
# elif hundred_digit == 1:
#     hundred_word = hundreds_num_list[0]

# if ones_digit == 9:
#     ones_word = ones_num_list[9]
# elif ones_digit == 8:
#     ones_word = ones_num_list[8]
# elif ones_digit == 7:
#     ones_word = ones_num_list[7]
# elif ones_digit == 6:
#     ones_word = ones_num_list[6]
# elif ones_digit == 5:
#     ones_word = ones_num_list[5]
# elif ones_digit == 4:
#     ones_word = ones_num_list[4]
# elif ones_digit == 3:
#     ones_word = ones_num_list[3]
# elif ones_digit == 2:
#     ones_word = ones_num_list[1]
# elif ones_digit == 1:
#     ones_word = ones_num_list[1]
# elif ones_digit == 0:
#     ones_word = ones_num_list[0]

# while True:
#     if tens_digit == 0 and ones_digit == 0:
#         print('Zero')
#     elif tens_digit == 0 and ones_digit == 1:
#         print('One')
#     elif tens_digit == 0 and ones_digit == 2:
#         print('Two')
#     elif tens_digit == 0 and ones_digit == 3:
#         print('Three')
#     elif tens_digit == 0 and ones_digit == 4:
#         print('Four')
#     elif tens_digit == 0 and ones_digit == 5:
#         print('Five')
#     elif tens_digit == 0 and ones_digit == 6:
#         print('Six')
#     elif tens_digit == 0 and ones_digit == 7:
#         print('Seven')
#     elif tens_digit == 0 and ones_digit == 8:
#         print('Eight')
#     elif tens_digit == 0 and ones_digit == 9:
#         print('Nine')
#     elif tens_digit == 1 and ones_digit == 0:
#         print('Ten')
#     elif tens_digit == 1 and ones_digit == 1:
#         print('Eleven')
#     elif tens_digit == 1 and ones_digit == 2:
#         print('Twelve')
#     elif tens_digit == 1 and ones_digit == 3:
#         print('Thirteen')
#     elif tens_digit == 1 and ones_digit == 1:
#         print('Fourteen')
#     elif tens_digit == 1 and ones_digit == 5:
#         print('Fifteen')
#     elif tens_digit == 1 and ones_digit == 6:
#         print('Sixteen')
#     elif tens_digit == 1 and ones_digit == 7:
#         print('Seventeen')
#     elif tens_digit == 1 and ones_digit == 8:
#         print('Eighteen')
#     else:
#         print('Nineteen')
#         break
