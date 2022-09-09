import string
import random

digits = string.digits

def pick6():
    """
    generates a list of six numbers
    """
    numbers = []
    while len(numbers) < 6:
        numbers.append(random.randint(0, 99))
    return numbers

print(pick6())


while 

