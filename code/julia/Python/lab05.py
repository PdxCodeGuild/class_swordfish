#Credit Card Validation


def credit_card_validator(orig_num):
    list_digits = list(orig_num)
    print(list_digits)
    for i in range(len(list_digits)):
        list_digits[i] = int(list_digits[i])
    check_digit = list_digits.pop()
    print(2, list_digits)    


    list_digits.reverse()
    print(3, list_digits)

    for i in range(len(list_digits)):
        if i % 2 == 0:
            list_digits[i] = list_digits[i] *2
    print(4, list_digits)

    for i in range(len(list_digits)):
        if list_digits[i] > 9:
            list_digits[i] = list_digits[i] -9
    print(5, list_digits)

    total = sum(list_digits)
    print(6, total)     
    print(7, check_digit)

    if check_digit == total %10:
        return True 
    return False
    
print(credit_card_validator("4556737586899855"))




