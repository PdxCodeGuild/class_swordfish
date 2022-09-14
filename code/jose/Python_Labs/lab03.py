card_values = {'A': 1,
'K': 10,
'Q': 10,
'J': 10,
'10': 10,
'9': 9,
'8': 8,
'7': 7,
'6': 6,
'5': 5,
'4': 4,
'3': 3,
'2': 2
}

# cards_chosen = []
user_card1 = input('Please enter your first card: ')
user_card2 = input('Please enter your second card: ')
user_card3 = input('Please enter your final card: ')

user_card1 = card_values[user_card1]
user_card2 = card_values[user_card2]
user_card3 = card_values[user_card3]

total_user_card = user_card1 + user_card2 + user_card3

if total_user_card < 17:
    total_user_card = str(total_user_card)
    print(total_user_card + ' Hit')
elif 17 < total_user_card <= 20:
    total_user_card = str(total_user_card)
    print(total_user_card + ' Stay')
elif total_user_card == 21:
    total_user_card = str(total_user_card)
    print(total_user_card + ' Blackjack!')
elif total_user_card > 21:
    total_user_card = str(total_user_card)
    print(total_user_card + ' Busted :P')