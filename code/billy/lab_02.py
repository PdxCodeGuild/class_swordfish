# '''
# program: lab_02
# author: Billy Frick
# date: 8 September 2022

# function: This program will convert any number into its English representation.

# '''


# list = {

#     'tens': ["zero", "one", "twenty-", "thirty-", "fourty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"],

#     'teens':["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],

#     'ones': ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]

# }

# x = input("\nWelcome! Please enter a number between 0 and 99 ")

# x = int(x)

# tens_digit = x//10

# ones_digit = x%10

# if tens_digit == 1: 
#     print(f"{list['teens'][ones_digit]}")

# elif tens_digit == 0:
#     print(f"{list['ones'][ones_digit]}")

# else:
#     print(f"{list['tens'][tens_digit]}{list['ones'][ones_digit]}")

list = {

    'tens': ["zero", "one", "twenty-", "thirty-", "fourty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"],

    'teens':["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],

    'ones': ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]

}

x = input("\nWelcome! Please enter a number between 0 and 999 ")

x = int(x)

if x < 100:

    list = {

    'tens': ["zero", "one", "twenty-", "thirty-", "fourty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"],

    'teens':["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],

    'ones': ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]

}

    tens_digit = x//10

    ones_digit = x%10

    if tens_digit == 1: 
        print(f"{list['teens'][ones_digit]}")

    elif tens_digit == 0:
        print(f"{list['ones'][ones_digit]}")

    else:
        print(f"{list['tens'][tens_digit]}{list['ones'][ones_digit]}")

elif x >= 100 and x <= 999:

    hundreds_digits = [-1]

    hundreds_list = {

    'hundreds': ["zero", "one-hundred", "two-hundred", "three-hundred", "four-hundred", "five-hundred", "six-hundred", "seven-hundred", "eight-hundred", "nine-hundred"],

    'tens': ["zero", "one", "twenty-", "thirty-", "fourty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"],

    'teens':["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],

    'ones': ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]
    
    }

    print(f"{list['hundreds'][hundreds_digits]}")
