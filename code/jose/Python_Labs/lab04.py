import numbers
import string
import random

digits = string.digits

numbers = []

def pick6():
    while len(numbers) < 6:
        numbers.append(random.randint(0, 99))
        return numbers


print(numbers)
print(random.randint(0,99))