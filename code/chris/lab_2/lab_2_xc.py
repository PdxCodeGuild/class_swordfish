#Version3

number = input(f'Please input a numeric number to be converted to a Roman numeral: ')
number = int(number)

tens_num_list = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C'] 
ones_num_list = [' ', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

x = number
tens_digit = x//10  
ones_digit = x%10

roman_tens = tens_num_list[tens_digit]
roman_ones = ones_num_list[ones_digit]

roman_time = roman_tens + roman_ones
print(roman_time)

#Version4

