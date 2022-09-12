'''
Lab 2: Number to Phrase
-convert a given number into its english representation
-Handles numbers from 0-99
'''

# converting from an integer to a string????
# use the digit, as a key for a dict of digit:phrase pairs

# 0-9
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
# ask the user for a number
# convert the number user inputs to an integer
user_input_number = int(input('Input a number between 0-99: '))


tens_digit = user_input_number // 10  # prints 9
ones_digit = user_input_number % 10  # prints 7

if tens_digit > 2:
    # 20 and above
    print(f'{tens_suffix[tens_digit]}-{ones_suffix[ones_digit]}')


elif tens_digit == 1:
    # 10-19
    print(f'{teens_suffix[ones_digit]}')

else:
    # 0-9
    print(f'{ones_suffix[ones_digit]}')


'''
Version 2
-handles numbers from 100-999.
'''
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
hundreds_suffix = {
    1: 'one-hundred',
    2: 'two-hundred',
    3: 'three-hundred',
    4: 'four-hundred',
    5: 'five-hundrred',
    6: 'six-hundred',
    7: 'seven-hundred',
    8: 'eight-hundred',
    9: 'nine-hundred'
}
# ask the user for a number
# convert the number user inputs to an integer
user_input_number = int(input('Input a number between 100-999: '))

# convert digit to a string and SLICE each digit --> Exanple:'800'
hundreds_digit = str(user_input_number)[0]  # --> 8
tens_digit = str(user_input_number)[1]   # --> 0
ones_digit = str(user_input_number)[2]  # --> 0
# print(hundreds_digit)
# print(tens_digit)
# print(ones_digit)
if int(tens_digit) == 1:
    # 100-919
    # if the number in the hundreds place is greater/equal to 1
    # and hundreds place is less than/equal to 9
    print(
        f'{hundreds_suffix[int(hundreds_digit)]}-{teens_suffix[int(ones_digit)]}')

elif int(tens_digit) >= 2:

    print(
        f'{hundreds_suffix[int(hundreds_digit)]}-{tens_suffix[int(tens_digit)]}-{ones_suffix[int(ones_digit)]}')
else:
    print(
        f'{hundreds_suffix[int(hundreds_digit)]}-{ones_suffix[int(ones_digit)]}')
