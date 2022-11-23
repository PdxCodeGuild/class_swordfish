num_cards = {'2':2,'3':3,'4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,'A':1,'J':10,'Q':10,'K':10}

def blackjack():
    first_card = input("What's your first card? ")
    second_card = input("What's your second card? ")
    third_card = input("What's your third card? ")
    
    total = num_cards[first_card] + num_cards[second_card] + num_cards[third_card]
    
    if int(total) < 17:
        print(total,"Hit")
    elif int(total) >= 17 and int(total) < 21:
        print(total,"Stay")
    elif int(total) == 21:
        print(total,"Blackjack!")
    elif int(total) > 21:
        print(total,"Already Busted")
blackjack()
