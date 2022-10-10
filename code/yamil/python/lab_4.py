import random

def pick6():
    tickets = []
    for i in range(6):
        tickets.append(random.randint(1,99))
    return tickets

winning_ticket = pick6()
balance = 0
expenses = 0
earnings = 0

earnings_dict = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}
# ----------------------------------------

for i in range(100000):
    expenses += 2
    matches = 0
    balance -= 2
    ticket = pick6()
    for i in range(len(winning_ticket)):
        if ticket[i] == winning_ticket[i]:
            matches += 1
    earnings += earnings_dict[matches]
    balance += earnings_dict[matches]

print(winning_ticket)
print(earnings)
print(balance)
print(expenses)
print((earnings - expenses) / expenses)