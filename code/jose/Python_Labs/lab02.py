x = input('Enter a number: ')
x = int(x)
# tens_digit = x//10
# ones_digit = x%10
# hundreds_digit = x//100
# print(hundreds_digit)

random_numbers = {20: 'twenty',
30: 'thirty',
40: 'forty',
50: 'fifty',
60: 'sixty',
70: 'seventy',
80: 'eighty',
90: 'ninety',
100: 'onehundred',
200: 'twohundred',
300: 'threehundred',
400: 'fourhundred',
500: 'fivehundred',
600: 'sixhundred',
700: 'sevenhundred',
800: 'eighthundred',
900: 'ninehundred'
}

ones = {0 : 'zero',
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine'
}
tens_under20 = {10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thirteen',
14: 'fourteen',
15: 'fifteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'nineteen'
}
tens_digitwritten = {2: 'twenty',
3: 'thirty',
4: 'forty',
5: 'fifty',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'ninety'}

if x in random_numbers:
    print (random_numbers[x])


if 110<=x < 119 or 220 <= x < 229 or 330 <= x < 339 or 440 <= x < 449 or 550 <= x < 559 or 660 <= x < 669 or 770 <= x < 779 or 880 <= x < 889 or 990 <= x < 999:
    hundreds_digit = x//100
    lst = []
    lst.extend(x)
    tens_digits =lst.pop(0)
    print(tens_digits)
    print(ones[hundreds_digit + tens_under20[tens_digits]])
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
    print(hundreds_digit + 'hundred',tens_digitwritten[tens_digit],ones[ones_digit])


elif x in ones:
    print(ones[x])
elif 10 < x < 20:
    print(tens_under20[x])

elif x >= 20 and x < 100:
    tens_digit = x//10
    ones_digit = x%10
    print(tens_digitwritten[tens_digit], ones[ones_digit])  

elif 100<=x < 109 or 200 <= x < 209 or 300 <= x < 309 or 400 <= x < 409 or 500 <= x < 509 or 600 <= x < 609 or 700 <= x < 709 or 800 <= x < 809 or 900 <= x < 909:
    hundreds_digit = x//100
    lst = []
    x = str(x)                                  #added these lines to fix the in between spaces where the input would have been missed
    lst.extend(x)
    last_digit = lst.pop(0)
    last_digit = lst.pop(1)
    print(ones[hundreds_digit]+'hundred', ones[int(last_digit)])

# elif 100 <= x < 999:
#     hundreds_digit = x//100
#     x = str(x)
#     lst = []
#     lst.extend(x)           #here I am simply taking the string, turning it into a string, then using the previous
#     lst.pop(0)              #code to take the seperate numbers and concatenating them at the end
#     last_two_nums = ''.join(lst)
#     last_two_nums = int(last_two_nums)
#     hundreds_digit = ones[hundreds_digit]
#     tens_digit = last_two_nums//10
#     ones_digit = last_two_nums%10 
#     print(hundreds_digit + 'hundred',tens_digitwritten[tens_digit],ones[ones_digit])


    # firstwrd = num_ls(ones[0])
    # secondwrd= num_ls(tens_digitwritten[1])
    # thirdwrd = num_ls(ones[2])
    # print(firstwrd + secondwrd + thirdwrd)






    
        


# x = int(x)



# print(tens_digit)
# print(ones_digit)