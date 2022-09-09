import random

winning_ticket = []
for num in range(6):
    winning_ticket.append(random.randint(1,99))

print(winning_ticket)

# ----------------------------------------

balance = 0
match = 0

for tries in range(1):
    player_ticket = []
    for num in range(6):
        player_ticket.append(random.randint(1,99))
        for num in range(len(player_ticket)):
            if player_ticket[num] != winning_ticket[num]:
                match += 1
            
            
    balance -= 2
    print(player_ticket)
    print(match)
    
print(balance)
