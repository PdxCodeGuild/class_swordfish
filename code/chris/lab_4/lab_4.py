import random
from typing import Counter

#Version 1
numbers_range = list(range(100))

def pick6():
    counter = 0 #this is base number (can start at zero or ten or whatever)
    numbers = [] #empty list adding numbers into
    while counter < 6: #counter variable equates to counter
        counter += 1 #adds to the counter revolution until while loop is satisfied
        numbers.append(random.choice(numbers_range))
    return numbers

winning_numbers = pick6()
ticket_numbers = pick6()

def num_matching(lotto_numbers, winning_ticket):
    matching = 0
    if lotto_numbers[0] == winning_ticket[0]:
        matching += 1
    if lotto_numbers[1] == winning_ticket[1]:
        matching += 1
    if lotto_numbers[2] == winning_ticket[2]:
        matching += 1
    if lotto_numbers[3] == winning_ticket[3]:
        matching += 1
    if lotto_numbers[4] == winning_ticket[4]:
        matching += 1
    if lotto_numbers[5] == winning_ticket[5]:
        matching += 1
    return matching

loop = 0
play = 0
earnings = 0
while loop < 100000:
    loop += 1
    winning_numbers = pick6()
    ticket_numbers = pick6()
    if num_matching(winning_numbers, ticket_numbers) == 1:
        earnings += 4
    if num_matching(winning_numbers, ticket_numbers) == 2:
        earnings += 7
    if num_matching(winning_numbers, ticket_numbers) == 3:
        earnings += 100
    if num_matching(winning_numbers, ticket_numbers) == 4:
        earnings += 50000
    if num_matching(winning_numbers, ticket_numbers) == 5:
        earnings += 1000000
    if num_matching(winning_numbers, ticket_numbers) == 6:
        earnings += 25000000
    play -= 2

final_balance = earnings + play

print(f'My final balance is ${final_balance}')

#Version 2
def roi(earnings, play):
    difference = (((final_balance / play) * int(-1)))
    difference = difference * int(100)
    difference = round(difference, 2)
    difference = f'My ROI is {difference}%'
    return difference

# print('My ROI is: ')
print(roi(earnings, play))

print(f'My earnings is ${earnings}')
print(f'My expenses is ${play}')