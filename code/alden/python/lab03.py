cards = {       # Dic to store the cards and values.
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10':10,
    'J': 10,
    'Q': 10,
    'K': 10
}

def value(first, second, third):                        # Function to run the math of adding up the cards.
    totals = [0]
    selections = [first, second, third]
    for x in selections:                                # Runs through the card selections.
        for i in range(len(totals)):                    # Adds up the values of the cards
            totals[i] += cards[x]
        if x == 'A':                                    # If one of the selections is an A, adds a new value to the a list where A = 11.
            totals.append(totals[-1] + 10)
    return totals
    
   
#     return totals
first_in = input('Pick your first card: ').upper()              # Request input for 3 cards.
second_in = input('Pick your second card: ').upper()
third_in = input('Pick your third card: ').upper()

total = value(first_in, second_in, third_in)            # Creating the total for the cards.
best = list(reversed(total))                            # Reverse list to make it easier to determine which si the better option
if len(best) > 1:                                       # Checks to see if the best list is more then one index long.
    for i in range(len(best)):
        if best[i] <=21:
            best = best[i]
            break
else:
    best = best[0]                                      # If not, sets 0 index as the value.

if best < 17:                                           # if, elif, else to determine the printed outcome.
    print(f'{best} Hit')

elif 17 <= best < 21:
    print(f'{best} Stay')

elif best == 21:
    print(f'{best} Blackjack!!')

else:
    print(f'{best} Already Busted. :( ')