

import numbers


credit_card_number = input('What is the credit card number?: ')
cc_split = list(credit_card_number)                         #turned str into list of individual strings
check_value = cc_split.pop()                                #popped last value and created check value for later
cc_split.reverse()                                             #reversed list
cc_split = [int(nums) for nums in cc_split]                 #turned each individual string in the list into integer
cc_split[::2] = [x*2 for x in cc_split[::2]]                #multiplied every other number by 2 starting at index 0 and slicing by 2
cc_split =  [x-9 if x > 9 else x for x in cc_split[::]]     #subtracted by 9 ever number above 9 and retained previous list
cc_split_sum = str(sum(cc_split))                           #added the sum of the list of integers and converted to string
cc_split_sum = list(cc_split_sum)                           #created string into list

if cc_split_sum.pop() == check_value:
    print('Valid')
elif cc_split.pop() != check_value:                         #checked to see if popped value of sum of list was equal to check value
    print('Invalid')                                               #returned bool with if/elif both situations

# print(cc_split)
# print(cc_split_sum)