cards = {"A": 1, "2":2, "3":3, "4":4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,'J':10,'Q':10, 'K':10}
def blackjack():
    first_card = int(input("What's your first card?"))
    second_card = int(input("What's your second card?"))
    third_card = int(input("What's your third card?"))
    
    total = first_card + second_card + third_card
    
    if total < 17:
        print("Hit")
    elif total >= 17 and total < 21:
        print("Stay")
    elif total == 21:
        print("Blackjack!")
    elif total > 21:
        print("Already Busted")
blackjack()