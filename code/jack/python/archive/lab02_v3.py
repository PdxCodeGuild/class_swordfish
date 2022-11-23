number_input = input('enter integer 0-999: ') #get input from user as string for digit extraction
number_output = '' #string is initiated to prepare for concatenation

#individual digits are assigned
ones_digit = int(number_input[-1])
tens_digit = 0
hundreds_digit = 0
if int(number_input) > 9:
    tens_digit = int(number_input[-2])
if int(number_input) > 99:
    hundreds_digit = int(number_input[-3])

#user input is converted to int for comparisons
number_input = int(number_input)

ones_roman = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
tens_roman = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
hundreds_roman = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

def concat_roman(digit, roman_list):
    for x in roman_list:
        if digit == roman_list.index(x):
            return x

number_output += concat_roman(hundreds_digit, hundreds_roman)
number_output += concat_roman(tens_digit, tens_roman)
number_output += concat_roman(ones_digit, ones_roman)

print(number_output)