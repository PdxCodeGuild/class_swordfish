'''
program: lab_05
author: billy frick
date: 13 september 2022

function: This program will tka e acredit card number and validtate it by returning a Boolean.

'''


user_input = input("\nPlease enter a 16-digit credit card number to validate: ")

credit_card_numbers = list(user_input)

credit_card_numbers.reverse()

check_digit = credit_card_numbers[-1]

doubled_card_numbers = []

# This for loop doubles and appends everyn other number into double_card_numbers. Also -9 for every number above 9.
for digit in credit_card_numbers[0::2]:

    doubled_numbers = int(digit) * 2

    if doubled_numbers > 9:

        doubled_numbers -= 9

    doubled_card_numbers.append(doubled_numbers)

# creates a list for all numbers not taken in for loop.
credit_card_numbers = credit_card_numbers[1::2]

credit_card_list = []

# creates variable "numbers", and appends the converted "num" to the list credit_card_list.
for num in credit_card_numbers:
    
    numbers = int(num)

    credit_card_list.append(numbers)
    
# create a new variable and determine its sum value.
numbers_sum = sum(doubled_card_numbers) + sum(credit_card_list)

# create a new variable and convert numbers_sum into a string so we can isolate the last digit of the sum.
last_digit = str(numbers_sum)[-1]

# determines whether the card is valid or invalid.
if int(last_digit) == int(check_digit):

    print("\nCard is valid!")

else:

    print("\nThe card is not valid!")









