# Number to phrase

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['void', 'void', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

num = input('Type a number between 1-999. ')
num = int(num)

if num < 20:
    print(numbers[num])
elif num > 20 and num < 100:
    num = str(num)
    num = list(num)
    digit_one = num[0]
    digit_one = int(digit_one)
    digit_two = num[1]
    digit_two = int(digit_two)
    print(tens[digit_one] + numbers[digit_two])
elif num > 99 and num < 1000:
    num = str(num)
    num = list(num)
    digit_one = num[0]
    digit_one = int(digit_one)
    digit_two = num[1]
    digit_two = int(digit_two)
    digit_three = num[2]
    digit_three = int(digit_three)
    print(f"{numbers[digit_one]}hundred and {tens[digit_two] + numbers[digit_three]}")
