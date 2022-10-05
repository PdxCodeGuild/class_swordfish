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
credit_card_number = list(input('Enter a valid credit card number: '))


def credit_card_validator(credit_card_number):
    integer_list = []  # --> list of integers

    for i in credit_card_number:
        integer_list.append(int(i))
    print(integer_list)

    # slice of last digit of the integer_list
    check_digit = integer_list.pop(-1)
    print(check_digit)
    print(integer_list)

    # reverse the digits
    integer_list.reverse()
    print(integer_list)

    # get every other element
    every_other = integer_list[0::2]
    print(every_other)
    # double every other element in the reversed list
    doubled_numbers = [i * 2 for i in every_other]
    print(doubled_numbers)
    non_doubled_numbers = integer_list[1::2]
    print(non_doubled_numbers)
    final_list = doubled_numbers + non_doubled_numbers
    print(final_list)
    # subtract nine from numbers over nine.
    # loop over the num in final_list
    # if num is greater than 9, subtract 9 from num
    # otherwise
    subtract_9 = [num - 9 if num > 9 else num for num in final_list]
    print(subtract_9)

# sum all of the values
    sum_of_values = sum(subtract_9)
    print(sum_of_values)
    # print(type(sum_of_values))

# get the second digit of that sum. --> 85
    second_digit = str(sum_of_values)
    second_digit = int(second_digit[1])
    print(second_digit)
    # print(type(second_digit))

# if second_digit matches the check digit, the whole card number is valid.
    if second_digit == check_digit:
        print('Credit Card Is Valid!')
    else:
        print('Credit Card Is Not Valid!')


credit_card_validator(credit_card_number)
