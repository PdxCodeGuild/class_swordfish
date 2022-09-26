#Credit Card Validation

def credit_card_validator(orig_num):
    list_digits = list(orig_num)
    for i in range(len(list_digits)):
        list_digits[i] = int(list_digits[i])
    check_digit = list_digits.pop()


    list_digits.reverse()
    for i in range(len(list_digits)):
        if i % 2 == 0:
          
            return list_digits


    
    # every_second_num = list(list_digits)
    # for i in range(1, len(), *2):
    #     every_second_num.append(list_digits[i])
        



print(credit_card_validator("4556737586899855"))


