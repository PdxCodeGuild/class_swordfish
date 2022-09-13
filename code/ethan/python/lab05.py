# Credit Card Validator

# 4556737586899855

numbers = input('Type in a credit card number: ')
numbers = list(numbers)

numbers = [int(x) for x in numbers]

last_digit = numbers[15]

del numbers[15]

numbers.reverse()

numbers = [numbers[i] * 2 if i % 2 == 0 else numbers[i] for i in range(15)]

numbers = [numbers[i] - 9 if numbers[i] > 9 else numbers[i] for i in range(15)]

numbers = sum(numbers)

numbers = str(numbers)
numbers = list(numbers)
numbers = [int(x) for x in numbers]

check_number = numbers[1]

if last_digit == check_number:
    print('Valid!')
else:
    print('Invalid card number!')