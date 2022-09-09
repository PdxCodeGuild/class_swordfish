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
    return cards[first] + cards[second] + cards[third]
     
first_in = input('Pick your first card: ')              # Request input for 3 cards.
second_in = input('Pick your second card: ')
third_in = input('Pick your third card: ')

total = value(first_in, second_in, third_in)            # Creating the total for the cards.

if total < 17:                                          # if, elif, else to determine the printed outcome.
    print(f'{total} Hit')

elif 17 <= total < 21:
    print(f'{total} Stay')

elif total == 21:
    print(f'{total} Blackjack!!')

else:
    print(f'{total} Already Busted. :( ')