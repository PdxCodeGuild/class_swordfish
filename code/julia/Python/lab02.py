#Number To Phrase
 
x = int(input("Enter a number between 0 and 99: "))

tens_digit = x//10
ones_digit = x%10

tens = ["zero", "one", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
ones =["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens =["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"]

if tens_digit < 0:

 print(f"{tens[tens_digit]} {ones[ones_digit]} ")

elif tens_digit == 1:
    print(f"{teens[ones_digit]}")

else:
    print(f"{ones[ones_digit]}")   