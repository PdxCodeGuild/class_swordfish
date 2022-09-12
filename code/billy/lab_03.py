'''
program: lab_03.py
author: Billy Frick
date: 12 September 2022

function: this program will allow the user to enter 3 cards, and total the overall score.
'''

# dictionary of all card values. This will be used after the user enters their cards.
face_cards_dict = {

    'king': 10,
    'queen': 10,
    'jack':  10,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'ace': 1,
}


# This function will refer to face_cards_dict and add up the total value of the 3 cards.
def card_counter(first_card, second_card, third_card):

    card_values = face_cards_dict[first_card] + face_cards_dict[second_card] + face_cards_dict[third_card]

    return card_values

# Determines the value of the first card.
card_one = input("\n> What's your first card? ")

# Determines the value of the second card.
card_two = input("\n> What's your second card? ")

# Determines the value of the third card.
card_three = input("\n> What's your third card? ") 

# takes user input and uses card_counter function to determine total score.
card_total = (card_counter(card_one, card_two, card_three))


# if and elif statements that will determine if the user should hit or stay, or if they get a black jack or bust.
if card_total < 17:
    print("\nCard total:",card_total, "\nAdvised action: Hit!")

elif card_total > 17 and card_total < 21:
    print("\nCard total:",card_total, "\nAdvised action: Stay!")

elif card_total == 21:
    print("\nCard total:",card_total, "\nBlack Jack! \nWinner!" )

elif card_total > 21:
    print("\nCard total:",card_total, "\nAdvised action: Bust! \nLoser!" )
