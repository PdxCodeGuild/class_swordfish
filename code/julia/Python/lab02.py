#Number To Phrase
 
x = int(input("Enter a number between 0 and 999: "))

tens_digit = x//10
ones_digit = x%10

tens = ["zero", "one", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"]
hundreds = ["zero", "one-hundred", "two-hundred", "three-hundred", "four-hundred", "five-hundred", 
"six-hundred", "seven-hundred", "eight-hundred", "nine-hundred", "nine-hundred and ninty-nine"]

if x < 100:
    if tens_digit == 0:
        print(f"{ones[ones_digit]} ")

    elif tens_digit == 1:
        print(f"{teens[ones_digit]} ")

    elif tens_digit > 1:
        print(f"{tens[tens_digit]} {ones[ones_digit]} ")

else:
    tens_digit = str(x)[1]
    hundreds_digit = str(x)[0]

    if int(tens_digit) == 0:
        print(f"{hundreds[int(hundreds_digit)]} {ones[ones_digit]} ")

    elif int(tens_digit) == 1:
        print(f"{hundreds[int(hundreds_digit)]} {teens[ones_digit]} ")

    elif int(tens_digit) > 1:
        print(f"{hundreds[int(hundreds_digit)]} {tens[int(tens_digit)]} {ones[ones_digit]} ")
