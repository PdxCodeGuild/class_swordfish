'''Lab 3: Blackjack Advice
'''
'''
Write a program to give basic blackjack playing advice
during a game by asking the player for cards
    -First, ask the user for three playing cards
            (A,2,3,4,5,6,7,8,9,10,J,Q,K)
    -Second, figure point of value of each card
            (number cards = worth their number)
            (face cards = 10)
            (A = 1)
'''
'''
-less than 17 -->'Hit'
-greater than or equal to 17 BUT less than 21 --> 'Stay'
-21 --> 'Blackjack'
-greater than 21 --> 'Already Busteed
'''
cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}
# print(cards)

# ask the user for first card
first_card = input('What\'s your first card?: ')
# ask the user for second card
second_card = input('What\'s your second card?: ')
# ask the user for third card
third_card = input('What\'s your third card?: ')


def basic_blackjack():
    if
