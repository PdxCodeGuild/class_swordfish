x = input('Enter a number: ')
x = int(x)
# tens_digit = x//10
# ones_digit = x%10

ones = {1: 'one',
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

if x in ones:
    print(ones[x])
elif 10 < x < 20:
    print(tens_under20[x])

elif x > 20:
    tens_digit = x//10
    ones_digit = x%10
    print(tens_digitwritten[tens_digit], ones[ones_digit])





    
        


# x = int(x)



# print(tens_digit)
# print(ones_digit)