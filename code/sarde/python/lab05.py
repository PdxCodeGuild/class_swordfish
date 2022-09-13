'''Lab 5: Credit Card Validation
'''
'''
Write a function credit_card_validator which
returns whether a string containing a credit card number is valid as a boolean.
'''
'''
1.Convert the input string into a list of ints
2.Slice off the last digit. That is the check digit.
3.Reverse the digits.
4.Double every other element in the reversed list (starting with the first number in the list).
5.Subtract nine from numbers over nine.
6.Sum all values.
7.Take the second digit of that sum.
8.if that matches the check digit, the whole card number is valid.
'''


# def credit_card_validator():
integer_list = []  # --> list of integers
credit_card_number = int(input('Enter a valid credit card number: '))
integer_list.append(credit_card_number)
# print(integer_list)

# slice of last digit of the integer_list
check_digit = integer_list[-1]
print(check_digit)
