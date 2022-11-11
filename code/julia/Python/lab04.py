#Pick6
import random 

balance = 0
earnings = 0
cost = 0 

def pick6(): 
    ticket = []
    for x in range(6):
        ran_num = random.randint(1, 99)
        ticket.append(ran_num)
    return ticket

def num_matches(winning, ticket): 
    number_of_matches = 0
    for win,tix in zip(winning, ticket):
        if win == tix:
            number_of_matches += 1
    return number_of_matches  

winnings = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}
winning_nums = pick6()
number_of_matches = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(100000): #the amount of times it loops
    ticket = pick6() # accesses the pick6() ticket 
    balance -= 2 #subtracts from the balance with each purchase of the ticket
    cost += 2 #Adds to the cost of the purchase
    matches = num_matches(winning_nums, ticket) 

    balance += winnings[matches]
    earnings += winnings[matches]
    number_of_matches[matches] += 1

    
print('balance', balance)
print('earnings', earnings)
print('cost', cost)
print('roi', (earnings - cost)/cost)
print('matches', number_of_matches)
print("This is the ticket", ticket)
