#Lab 3: Blackjack advice

#define card scoring
options = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

#create list of cards from user input
cards = []
for i in range(3):
    cards.append(input(f'What is card # {i + 1}? ').upper())

#evaluate each card in cards and increment total score with respective card score
total = [0]
for x in cards:
    for i in range(len(total)): # increments each item in 'total' list by card score
        total[i] += options[x]
    if x == 'A': # if card is an ace, create another possible total score where ace score = 11 instead of 1
        total.append(total[-1] + 10)

#determine best score from all total options, where default is first item in list:
best_total = total[0]
for x in reversed(total):
    if x <= 21:
        best_total = x
        break

#evaluate best total score and return advice
if best_total < 17:
    print(best_total, 'Hit')
elif 17 <= best_total < 21:
    print(best_total, 'Stay')
elif best_total == 21:
    print(best_total, 'Blackjack!')
else:
    print(best_total, 'Already Busted')