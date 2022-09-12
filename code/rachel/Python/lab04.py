#generate random numbers using random.randint(x,y)
#create pick6 function to generate 6 random numbers and run it once to generate winning_ticket
#loop pick6 function 100,000 times (for loop?)
    #for every instance of the loop running, subtract 2 from balance
#create function that compares winning_ticket to random_ticket(s)
    #if random_ticket index 1
    #if random_ticket == winning ticket add 25 million
    #add to money_balance in each loop 

import random

winning_ticket = [random.randint(1, 99) for i in range(6)]

print(winning_ticket)
balance = 0
balance = int(balance)

def pick6(random_ticket):
     random_ticket = [random.randint(1, 99) for i in range(6)]
     return('random_ticket')

def number_matches(winning_ticket, random_ticket):
    for i in i, j in zip(winning_ticket, random_ticket) if i == j