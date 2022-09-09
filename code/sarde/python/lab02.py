'''
Lab 2: Number to Phrase
-convert a given number into its english representation
-Handles numbers from 0-99
'''
# converting from an integer to a string????
# use the digit, as a key for a dict of digit:phrase pairs

ones_suffix = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
# 20-90
tens_suffix = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}
# 10-19
teens_suffix = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen'
}

input_number = 1


tens_digit = input_number // 10  # prints 9
ones_digit = input_number % 10  # prints 7


if tens_digit > 2:
    # do suff for 2 and above
    print(f'{tens_suffix[tens_digit]}-{ones_suffix[ones_digit]}')


elif ones_digit >= 0 and ones_digit <= 9:
    # do stuff for 10-19
    print(f'{teens_suffix[ones_digit]}')

else:
    # do stuff for 0-9
    print(f'{ones_suffix[tens_digit]}')
