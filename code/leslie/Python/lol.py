
ones_digits = ["","one","two","three","four","five","six","seven","eight","nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_digits = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", ""]
hundreds = ["", "one hundred","two hundred","three hundred", "four hundred","five hundred","six hundred", "seven hundred", "eight hundred", "nine hundred"]

num = int(input("Enter a number: "))
def convert_to_words(number):    
    if num == 0:
        return "Zero"
    elif num > 0 and num < 20:
        return ones_digits[num]
    elif num >= 20 and num < 100:
        return tens_digits[int(num/10)]+ " " + ones_digits[int(num%10)]
    
    elif num >= 100 and num < 1000:        
        return hundreds[int(num/100)] + " " + tens_digits[int(num/10)%10] + " " + ones_digits[int(num%10)]
    
# !!! Add "and"??     
        
print(convert_to_words(num))
print(num%10)
print(num%100)
     
