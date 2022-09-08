#Lab 2: Number to Phrase

number_input = input('enter integer 0-999: ') #get input from user as string for digit extraction
number_output = '' #string is initiated to prepare for concatenation

#individual digits are assigned
ones_digit = int(number_input[-1])
tens_digit = 0
hundreds_digit = 0
if int(number_input) > 9:
    tens_digit = int(number_input[-2])
if int(number_input) > 99:
    hundreds_digit = int(number_input[-3])

#user input is converted to int for comparisons
number_input = int(number_input)

#optional phrase or roman numeral output (Lab 2: v2 or v3)
output_type = input('Which output type do you want? (roman or phrase) ').lower()
if output_type == 'phrase':

    #phrase options
    ones_phrase = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    tens_phrase = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    other_phrase = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')

    #function to turn 1-9 into phrase
    def ones_to_phrase(x):
        for phrase in ones_phrase:
            if x - 1 == ones_phrase.index(phrase):
                return(phrase)

    #function to turn 2x-9x into phrase
    def tens_to_phrase(x):
        for phrase in tens_phrase:
            if x - 2 == tens_phrase.index(phrase):
                return(phrase)

    #begin concatenating phrase

    #concatenates how many hundreds if not 0
    if hundreds_digit != 0:
        number_output += ones_to_phrase(hundreds_digit) + ' hundred'
        if tens_digit != 0 or ones_digit != 0: #'and' only needed if number phrase follows hundred
            number_output += ' and '

    #concatenates how many tens if not 0 or teens (greater than 1)
    if tens_digit > 1:
        number_output += tens_to_phrase(tens_digit)
        if ones_digit != 0:
            number_output += '-'

    #concatenates if number includes teens
    if tens_digit == 1:
        for phrase in other_phrase:
            if ones_digit == other_phrase.index(phrase):
                number_output += phrase

    #concatenates if ones digit is not 0, and if not teens
    elif ones_digit > 0:
        number_output += ones_to_phrase(ones_digit)

    #assigns 'zero' phrase if number is 0
    if number_input == 0:
        number_output = 'zero'

#roman numerals output option
elif output_type == 'roman':
    
    #numeral options
    ones_roman = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens_roman = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds_roman = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

    #function to take digit and corresponding numeral options and returns numeral
    def concat_roman(digit, roman_list):
        for x in roman_list:
            if digit == roman_list.index(x):
                return x

    #function is called for each of the 3 digits
    number_output += concat_roman(hundreds_digit, hundreds_roman)
    number_output += concat_roman(tens_digit, tens_roman)
    number_output += concat_roman(ones_digit, ones_roman)
    if number_input == 0: #special case for 0 since there is no roman numeral for 0
        number_output = 'Error: no roman numeral for 0' 

#output phrase
print(f'number to {output_type}: {number_output}')