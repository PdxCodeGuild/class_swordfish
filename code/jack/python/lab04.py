#Lab 4: pick6

import random

repeat = 100000
total_winnings = 0
total_cost = 0
winnings_breakdown = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

#found this on the internet but dont fully understand what it does, but cleaner than for loop below
#ticket = [random.randint(1, 99) for iter in range(6)]


#function to generate ticket
def pick6():
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

#create winning combination
winning_ticket = pick6()

#function to check a ticket agains the winning ticket and return respective prize money
def num_matches(winning, ticket):
    matches = 0
    for i in range(6):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

for i in range(100000):
    ticket = pick6()
    matches = num_matches(winning_ticket, ticket)
    total_winnings += winnings_breakdown[matches]
    total_cost += 2

roi = (total_winnings - total_cost) / total_cost

print(f'total winnings: ${total_winnings}, total expenses: ${total_cost}, ROI: {roi}')


