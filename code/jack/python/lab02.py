#Lab 2: Number to Phrase

value_number = int(input("Enter a number from 0 to 999: "))
value_phrase = ""

ones_digit = value_number % 10 #needs to be revised to accomdate hundreds
tens_digit = value_number // 10 #needs to be revised to accomdate hundreds

ones_phrase = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens_phrase = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#function to assign ones digit to phrase
def ones_to_phrase(x):
    for x in range(len(ones_phrase)):
        if x + 1 == ones_digit:
            return(ones_phrase[x])
            

#function to assign tens digit to phrase
def tens_to_phrase(x):
    for x in range(len(tens_phrase)):
        if x + 2 == tens_digit:
            if ones_digit != 0: #if ones digit is 0, no ones phrase needed. if not 0, must specify in phrase
                return(tens_phrase[x] + '-' + ones_to_phrase(ones_digit))
            else:
                return(tens_phrase[x])


if value_number == 0:
    value_phrase = "zero"
elif value_number < 10:
    value_phrase = ones_to_phrase(value_number)
elif value_number <= 19:
    value_phrase = ()
elif value_number <= 99:
    value_phrase = (tens_to_phrase(tens_digit))
elif value_number <= 999:
    value_phrase = (ones_to_phrase(value_number) + " hundred and " + str(tens_to_phrase(tens_digit)))



print(value_phrase)