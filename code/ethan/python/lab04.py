# Pick 6

import random

balance = 0

def pick6():
    numbers = []
    for x in range(6):
        lot_number = random.randint(1, 99)
        numbers.append(lot_number)
    return numbers

winning_ticket = pick6()
ticket = pick6()

def num_matches(x):
    balance = 0
    for x in range(100000):
        ticket = pick6()
        if ticket[0] == winning_ticket[0]:
            balance -= 2
            if ticket[1] == winning_ticket[1]:
                balance += 0
                if ticket[2] == winning_ticket[2]:
                    balance += 0
                    if ticket[3] == winning_ticket[3]:
                        balance += 0
                        if ticket[4] == winning_ticket[4]:
                            balance += 0
                            if ticket[5] == winning_ticket[5]:
                                balance += 25000000
        elif ticket[1] == winning_ticket[1]:
            balance -= 2
            if ticket[2] == winning_ticket[2]:
                balance += 0
                if ticket[3] == winning_ticket[3]:
                    balance += 0
                    if ticket[4] == winning_ticket[4]:
                        balance += 0
                        if f in winning_ticket[5]:
                            balance += 1000000
        elif ticket[2] == winning_ticket[2]:
            balance -= 2
            if ticket[3] == winning_ticket[3]:
                balance += 0
                if ticket[4] == winning_ticket[4]:
                    balance += 0
                    if ticket[5] == winning_ticket[5]:
                        balance += 50000
        elif ticket[3] == winning_ticket[3]:
            balance -= 2
            if ticket[4] == winning_ticket[4]:
                balance += 0
                if ticket[5] == winning_ticket[5]:
                    balance +=100
        elif ticket[4] == winning_ticket[4]:
            balance -= 2
            if ticket[5] == winning_ticket[5]:
                balance += 7
        elif ticket[5] == winning_ticket[5]:
            balance += 4
    return balance

balance = num_matches(1)
roi = (balance - 200000)/200000

print(f"Your remaining balance after playing Pick 6 100000 times is ${balance}.00.")
print(f'Your return on investment is {roi} for every ticket bought.')