'''
Lab 2: Number to Phrase
-convert a given number into its english representation
-Handles numbers from 0-99
'''
# converting from an integer to a string????
# use the digit, as a key for a dict of digit:phrase pairs
single_suffix = {
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
tens_suffix = {
    8: 'eighty',
    9: 'ninety'
}
# print(digits[6]+''+'-'+digits[7])

input_number = 97


tens_digit = input_number // 10
ones_digit = input_number % 10
#print(tens_digit, ones_digit)
if tens_digit >= 20:
    # do suff for 20 and above
    pass
elif tens_digit >= 10 and tens_digit <= 19:
    # do stuff for 10-19
    pass
else:
    # do stuff for 0-9
    pass
