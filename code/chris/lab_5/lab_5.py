#write a function call cc_validator which returns whether a string containing a cc number is valid in a boolean.
#must return T or F and can use function in IF Statemnt later
#1. Input String and convert into list of integers
#2. slice off last digit (check digit and save it)
#3. reverse remaining order aka flip order
#4. double every other in the list
#5. subtract 9 from any number over 9
#6. add all remaining values up
#7. take the "ones" digit and make sure this matches check digit
#8. if matches, then True and valid CC

#Lab5 
cc_number = input('Please input your credit card number to be validated? ')
cc_list = list(cc_number)
check_digit = str(cc_list[-1])
print(check_digit)
del cc_list[-1]
print(cc_list)
cc_list.reverse() 
cc_newlist = []
for num in cc_list:
    cc_newlist.append(int(num))
print(cc_newlist)
new_list_doubled = [n*2 for n in cc_newlist[::2]] 
new_remaining_list = [n for n in cc_newlist[1::2]] 
print(new_list_doubled)
print(new_remaining_list)
combined_list = new_list_doubled + new_remaining_list
print(combined_list)
new_list_subtracted = [n-9 if n > 9 else n for n in combined_list]
print(new_list_subtracted)
new_summed_list = sum(new_list_subtracted)
print(new_summed_list)
new_summed_list = str(new_summed_list)
new_summed_list2 = list(new_summed_list)
print(new_summed_list2)
if new_summed_list2[-1] == check_digit:
    print('Valid!')
else:
    print('Invalid!')


# def cc_validator(cc_number):
#     check_digit = cc_list[-1]
#     del cc_list[-1]
# cc_list.reverse() 
# cc_newlist = []
# for num in cc_list:
#     cc_newlist.append(int(num))
    

