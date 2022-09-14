#Credit Card Validator
#ask user for credit card number input
#convert input into a list (seperate each number with comma) & remove last digit (aka check digit) with pop()
#reverse the list with reverse()
#convert list items to integers
#double every other element
#make a list that includes both the doubled numbers and the numbers that didn't get doubled (add back in every other number starting w/ second number)
#subtract 9 from numbers greater than 9 (if i > 9: i - 9)
#sum all the values
#take the second digit of the sum and compare it to the check digit
    #if the numbers match, the card is valid (boolean)

credit_card = input("Enter the credit card number: ")
credit_card = list(credit_card)
#print(len(credit_card))
credit_card.pop(15)
#print(credit_card)
credit_card.reverse()
#print(credit_card)
cc_numbers = [int(x) for x in credit_card] #convert list items to integers cause math
#print(cc_numbers)
doubled_numbers = [2*x for x in cc_numbers[::2]]#double every other number
#print(doubled_numbers)
for i in doubled_numbers:
    

