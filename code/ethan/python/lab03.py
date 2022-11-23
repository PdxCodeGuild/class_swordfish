# Blackjack

card_one = input("What's your first card? ")
card_two = input("What's your second card? ")
card_three = input("What's your third card? ")

card_values = {
    'A' : 1,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}


card_one = card_values[card_one]
card_one = int(card_one)
card_two = card_values[card_two]
card_two = int(card_two)
card_three = card_values[card_three]
card_three = int(card_three)

total = card_one + card_two + card_three

if total < 17:
    print(f"{total} Hit")
elif total >= 17:
    print(f"{total} Stay")
elif total > 21:
    print(f"{total} Already Busted")
elif total == 21:
    print(f"{total} Blackjack!")
