# '''
# program: lab_02
# author: Billy Frick
# date: 8 September 2022

# function: This program will convert any number into its English representation.

# '''

list = {

    'tens': ["zero", "one", "twenty-", "thirty-", "fourty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"],

    'teens':["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],

    'ones': ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]

}

#grabs users input to determine value of x
x = input("\nWelcome! Please enter a number between 0 and 999 ")

#converts x into an integer
x = int(x)

#This will be executed if x is less than 100. The value of x will then be converted to the English phrase.
if x < 100:

    list = {

    'tens': ["zero", "one", "twenty-", "thirty-", "fourty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"],

    'teens':["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],

    'ones': ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]

}
    #floor division to get the digit in the tens place.
    tens_digit = x // 10

    #modulus will to grab the single digit left over.
    ones_digit = x % 10

    if tens_digit == 1: 
        print(f"{list['teens'][ones_digit]}")

    elif tens_digit == 0:
        print(f"{list['ones'][ones_digit]}")

    else:
        print(f"{list['tens'][tens_digit]}{list['ones'][ones_digit]}")

elif x >= 100 and x <= 999:

    hundreds_digit = x // 100

    tens_digit = x  % 100 // 10

    ones_digit = x % 10

    hundreds_dict = {

    'hundreds': 
            ["zero", 
            "one-hundred-", 
            "two-hundred-", 
            "three-hundred-", 
            "four-hundred-", 
            "five-hundred-", 
            "six-hundred-", 
            "seven-hundred-", 
            "eight-hundred-", 
            "nine-hundred-"],
    
    }

    hundreds_dict['tens'] = list['tens']

    hundreds_dict['teens'] = list['teens']

    hundreds_dict['ones'] = list['ones']

    hundreds_word = hundreds_dict['hundreds'][hundreds_digit]

    if tens_digit == 1: 
        print(f"{hundreds_word}{hundreds_dict['teens'][ones_digit]}")

    elif tens_digit == 0:
        print(f"{hundreds_word}{hundreds_dict['ones'][ones_digit]}")

    else:
        print(f"{hundreds_word}{hundreds_dict['tens'][tens_digit]}{list['ones'][ones_digit]}")