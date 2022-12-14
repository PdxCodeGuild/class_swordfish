import math
# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    # print(a % 2 == 0)
    # if a % 2 == 0:
    #     the_result = True
    #     #print(f'{a} is Even!')
    # else:
    #     the_result = False
    #     #print(f'{a} is Odd!')
    # return the_result

    return a % 2 == 0

def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True
    assert is_even(72) == True

# Ones Digit
# Write a function that returns the ones digit of a number

def ones_digit(num):
    ones_digit = num % 10
    return ones_digit
    
def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2

# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

def percentage(v, max):
    percentage = ((v / max) * 100)
    percentage_floor = (math.floor(percentage))
    percentage_string = str(percentage_floor) + "%"
    return percentage_string

def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'

