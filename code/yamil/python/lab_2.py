first_digit = {
    1 : "ten",
    2 : "twenty",
    3 : "thirty",
    4 : "forty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety"
    }

second_digit = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen"
    }

hundreds_digit = {
    1 : "one-hundred",
    2 : "two-hundred",
    3 : "three-hundred",
    4 : "four-hundred",
    5 : "five-hundred",
    6 : "six-hundred",
    7 : "seven-hundred",
    8 : "eight-hundred",
    9 : "nine-hundred",
}


x = int(input("Please enter a number: "))

hundreds = x // 100
hundreds_2 = x % 100
hundreds_3 = hundreds_2 % 10
hundreds_4 = hundreds_2 // 10
tens = x // 10
ones = x % 10


if x <= 19:
    print(f"You have entered {second_digit[x]}.")
elif 99 > x > 19 and x % 10 == 0:
    print(f"You have entered {first_digit[tens]}.")
elif 100 > x and x // 10 != 0:
    print(f"You have entered {first_digit[tens]}-{second_digit[ones]}.")
elif x > 99 and x % 100 == 0:
    print(f"You have entered {hundreds_digit[hundreds]}.")
elif x > 99 and x % 100 < 10:
    print(f"You have entered {hundreds_digit[hundreds]} and {second_digit[ones]}.")
elif x > 99 and x % 100 != 0 and isinstance(x/10,int) == True:
    print(f"You have entered {hundreds_digit[hundreds]} and {second_digit[ones]}.")
elif x > 99 and x % 100 != 0:
    print(f"You have entered {hundreds_digit[hundreds]} and {first_digit[hundreds_4]}-{second_digit[ones]}.")
else:
    print("Please enter a valid number between 0 and 999.")