num = {             #  Dictionatry to store all the numbers in both writen and numaric form.
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninty",
    100: "one hundred",
    200: "two hundred",
    300: "three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred"
}

x = int(input("Please select a number: "))  # Requesting number input from user and converting it to int. 

if x <= 20 or 30 or 40 or 50 or 60 or 70 or 80 or 90 or 100 or 200 or 300 or 400 or 500 or 600 or 700 or 800 or 900:                 # if statement to take care of any individual named numbers
    input_num = num[x]      # Pulls spelled out number from dic.
    print(input_num)

elif 21 <= x <= 99:                           # else statement to take care of compounded numbers
    tens_digit = x//10 * 10     # To get tens place, did floor division by 10 then multiply by 10 to get 2 digits.
    ones_digit = x%10           # To get ones place, did modulus by 10 seperating the ones spot.

    input_num = num[tens_digit] + num[ones_digit]   # Created a input to call the 2 numbers or single number from dic and add them together.
    print(input_num)                                # Print result in word form.

else:
    hun_digit = x//100 * 100
    tens_digit = x//10 * 10     # To get tens place, did floor division by 10 then multiply by 10 to get 2 digits.
    ones_digit = x%10

    input_num = num[hun_digit] + num[tens_digit] + num[ones_digit]
    print(input_num)