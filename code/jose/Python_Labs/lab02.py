


x = input('Enter a number: ')
x = int(x)
# tens_digit = x//10
# ones_digit = x%10
# hundreds_digit = x//100
# print(hundreds_digit)

random_numbers = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',70: 'seventy',80: 'eighty',90: 'ninety',100: 'one hundred',200: 'two hundred',300: 'three hundred',
400: 'four hundred',500: 'five hundred',600: 'six hundred',700: 'seven hundred',800: 'eight hundred',900: 'nine hundred',999 : 'nine hundred ninety nine'}

ones = {0 : 'zero',1: 'one',2: 'two',3: 'three',4: 'four',5: 'five',6: 'six',7: 'seven',8: 'eight',9: 'nine'}
tens_under20 = {10: 'ten',11: 'eleven',12: 'twelve',13: 'thirteen',14: 'fourteen',15: 'fifteen',16: 'sixteen',17: 'seventeen',18: 'eighteen',19: 'nineteen'}
tens_digitwritten = {2: 'twenty',3: 'thirty',4: 'forty',5: 'fifty',6: 'sixty',7: 'seventy',8: 'eighty',9: 'ninety'}

if x in random_numbers:
    print (random_numbers[x])

elif 100<=x < 109 or 200 <= x <= 209 or 300 <= x <= 309 or 400 <= x <= 409 or 500 <= x <= 509 or 600 <= x <= 609 or 700 <= x <= 709 or 800 <= x <= 809 or 900 <= x <= 909:
    hundreds_digit = x//100
    lst = []
    x = str(x)                                  #added these lines to fix the in between spaces where the input would have been missed
    lst.extend(x)
    last_digit = lst.pop(0)
    last_digit = lst.pop(1)
    print(ones[hundreds_digit]+' hundred', ones[int(last_digit)])

elif 110<=x <= 119 or 210 <= x <= 219 or 310 <= x <= 319 or 410 <= x <= 419 or 510 <= x <= 519 or 610 <= x <= 619 or 710 <= x <= 719 or 810 <= x <= 819 or 910 <= x <= 919:
    hundreds_digit = x//100
    lst = []
    x = str(x)
    lst.extend(x)
    tens_digits =lst.pop(0)
    last_two_nums = ''.join(lst)
    last_two_nums = int(last_two_nums)
    print(ones[hundreds_digit] + ' hundred ' + tens_under20[last_two_nums])

elif x in ones:
    print(ones[x])
elif 10 < x < 20:
    print(tens_under20[x])

elif x >= 20 and x < 100:
    tens_digit = x//10
    ones_digit = x%10
    print(tens_digitwritten[tens_digit], ones[ones_digit])  


elif 100 <= x < 999:
    hundreds_digit = x//100
    x = str(x)
    lst = []
    lst.extend(x)           #here I am simply taking the string, turning it into a string, then using the previous
    lst.pop(0)              #code to take the seperate numbers and concatenating them at the end
    last_two_nums = ''.join(lst)
    last_two_nums = int(last_two_nums)
    hundreds_digit = ones[hundreds_digit]
    tens_digit = last_two_nums//10
    ones_digit = last_two_nums%10 
    draft_output = hundreds_digit + ' hundred',tens_digitwritten[tens_digit],ones[ones_digit]
    if 'zero' in draft_output:
        draft_output = list(draft_output)
        darft_output = draft_output.remove('zero')
    final_output = " ".join(draft_output)
    
    print(final_output)


