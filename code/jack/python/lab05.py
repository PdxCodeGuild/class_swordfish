#Lab 5: credit card validation

def credit_card_validator(num):
    num_list = [int(x) for x in str(num)] # convert cc number digits to list of int
    check_digit = num_list.pop(-1) # remove last digit and store as the check digit
    num_list.reverse()
    num_list = [num_list[i] * 2 if i % 2 == 0 else num_list[i] for i in range(len(num_list))] # double every other digit
    num_list = [x - 9 if x > 9 else x for x in num_list] # if digit is greater than 9, subtract 9
    num_sum = sum(num_list) 
    num_sum_digit = num_sum % 10 # get last digit of sum of all digits
    if num_sum_digit == check_digit:
        return True
    else:
        return False

test_num = 4556737586899855
print(credit_card_validator(test_num))