#Lab 3: Blackjack advice

options = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

cards = {}
total = 0

for i in range(3):
    cards[i] = input(f'What is card # {i + 1}? ').upper()
    if cards[i] == 'A':#placeholder for version 2
        total += options[cards[i]]
    else:
        total += options[cards[i]]

if total < 17:
    print(total, 'Hit')
elif 17 <= total < 21:
    print(total, 'Stay')
elif total == 21:
    print(total, 'Blackjack!')
else:
    print(total, 'Already Busted')