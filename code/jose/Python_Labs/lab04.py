import string
import random

digits = string.digits

def pick6():
    """
    generates a list of six numbers
    """
    numbers = []
    while len(numbers) < 6:
        numbers.append(random.randint(0, 99))
    return numbers


def find_matching_indicies(l1, l2):
    """matches the indexes from one list to the other, returns a count of how many indices match"""
      # this code block compares two lists and returns a count of how many indices match
    count = 0
    for ind, num in enumerate(l1): 
        if l2[ind] == num:
            count += 1
    return count

# print(pick6())      #checking to see if numbers generate randomly

lotto_numbers = pick6()
# lotto_attempt = int(find_matching_indicies(lotto_numbers, user_numbers))

winnings = {
    0: 0,                       # #a ticket costs $2
    1: 4,                       # if 1 number matches, you win $4
    2: 7,                       # if 2 numbers match, you win $7
    3: 100,                     # if 3 numbers match, you win $100
    4: 50000,                   # if 4 numbers match, you win $50,000
    5: 1000000,                 # if 5 numbers match, you win $1,000,000
    6: 25000000                 # if 6 numbers match, you win $25,000,000
}                           

lotto_runs = 0
earned_amount = 0
expenses = 0
while lotto_runs < 100000:
    user_numbers = pick6()                      #This code block runs the possibility of winning against the lottery
    match_counts = find_matching_indicies(lotto_numbers, user_numbers)
    earned_amount += winnings[match_counts]
    lotto_runs += 1
    expenses += 2

roi = (earned_amount - expenses)/expenses
print('Your return on investment is ', roi)







