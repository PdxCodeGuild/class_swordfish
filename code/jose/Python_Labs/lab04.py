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


def find_matching_indicies(l1, l2):  # this code block compares two lists and returns a count of how many indices match
    count = 0
    for ind, num in enumerate(l1): 
        if l2[ind] == num:
            count += 1
    return count

# print(pick6())      #checking to see if numbers generate randomly

lotto_numbers = pick6()
user_numbers = pick6()

lotto_attempt = int(find_matching_indicies(lotto_numbers, user_numbers))

winnings = {0: -2,          # #a ticket costs $2
1: 4,                       # if 1 number matches, you win $4
2: 7,                       # if 2 numbers match, you win $7
3: 100,                     # if 3 numbers match, you win $100
4: 50000,                   # if 4 numbers match, you win $50,000
5: 1000000,                 # if 5 numbers match, you win $1,000,000
6: 25000000}                # if 6 numbers match, you win $25,000,000

lotto_runs = int(0)
user_funds = int()

while lotto_runs > 1000000:
    match_counts = find_matching_indicies(lotto_numbers, user_numbers)
    earned_amounts = int(match_counts[winnings] + user_funds)
    total_earnings = earned_amounts + user_funds
    lotto_runs += 1

    
print(user_funds)













# def index_matching():
#     """checks to see if indexes match indexes in two sets of list"""
#     matched_indexes = []
#     indexes = 0
#     while indexes < len(user_tickets):
#         if lotto_tickets.count(user_tickets[indexes]):
#             matched_indexes.append(indexes)

# print(matched_indexes)

        

    



# while len(lotto_numbers) < 100000:
#     lotto_numbers.append(pick6())  #building the list of lottery numbers for both the data base and user

# user_tickets = []

# while len(user_tickets) < 100000:
#     user_tickets.append(pick6())






