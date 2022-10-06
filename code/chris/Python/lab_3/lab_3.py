card_combos = { 
    'A':1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":10,
    "Q":10,
    "K":10,
}

card_1 = input('What is your first card? ')
card_2 = input('What is your second card? ')
card_3 = input('What is your third card? ')

card_result1 = card_combos[card_1]
card_result2 = card_combos[card_2]
card_result3 = card_combos[card_3]

card_total = card_result1 + card_result2 + card_result3

if card_total > 0 and card_total < 17:
    print(f'{card_total} Hit')
elif card_total >= 17 and card_total < 21:
    print(f'{card_total} Stay')
elif card_total == 21:
    print(f'{card_total} Blackjack!')
else:
    print('Already Busted!')



# def add(card_1, card_2, card_3):
#      print(add)
#      return

# print(card_total)