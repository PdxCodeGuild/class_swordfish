cc_string = input("What is the credit card number?: ")
cc_list = [int(x) for x in cc_string]

last_digit = cc_list.pop()
cc_list.reverse()

for x in range(0, len(cc_list), 2):
    cc_list[x] = cc_list[x] * 2

for x in range (0, len(cc_list)):
    if cc_list[x] > 9:
        cc_list[x] = cc_list[x] - 9

cc_sum = sum(cc_list)

final_check_digit = cc_sum % 10

if final_check_digit == last_digit:
    print("It works!")
else:
    print("Failed.")