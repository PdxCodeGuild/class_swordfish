#Lab 2: Number to Phrase

value_number = int(input("Enter a number from 0 to 909: "))
value_phrase = ""

tens_digit = value_number // 10
ones_digit = value_number % 10

tens_phrase = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ones_phrase = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

if value_number == 0:
    value_phrase = "zero"
elif value_number < 10:
    #call ones function, assign to value_phrase
elif value_number <= 19
    #print from unique list, assign to value_phrase
elif value_number <= 99:
    #call ones and tens functions, assign to value_phrase
elif value_number <= 999
    #call ones, tens, and hundreds functions, assign to value_phrase

#function to assign ones digit to phrase
def ones_to_phrase(x):
    for x in range(len(ones_phrase)):
        if x + 1 == ones_digit:
            return(ones_phrase[x])

#function to assign tens digit to phrase
def tens_to_phrase(x):
    for x in range(len(tens_phrase)):
        if x + 2 == tens_digit:
            return(tens_phrase[x])



print(value_phrase)