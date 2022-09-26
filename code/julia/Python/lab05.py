#Credit Card Validation

def credit_card_validator(orig_num):
    list_digits = list(orig_num)
    for i in range(len(list_digits)):
        list_digits[i] = int(list_digits[i])
    check_digit = list_digits.pop()


    list_digits.reverse()
    for i in range(len(list_digits)):
        if i % 2 == 0:
            list_digits[i] = list_digits[i] *2
    

    for i in range(len(list_digits)):
        if list_digits[i] > 9:
            list_digits[i] = list_digits[i] -9
    

    print(list_digits)
    print(list_digits[-2])
    return list_digits       
print(sum(credit_card_validator("4556737586899855")))


