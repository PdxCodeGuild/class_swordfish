#Version1
ones_digits = ["","one","two","three","four","five","six","seven","eight","nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_digits = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "one hundred"]
num = 67
def convert_to_words(num):    
    if num == 0:
        return "Zero"
    elif num > 0 and num < 20:
        return ones_digits[num]
    elif num >= 20:
        return tens_digits[int(num/10)]+ " " + ones_digits[int(num%10)]
print(convert_to_words(99))
     
