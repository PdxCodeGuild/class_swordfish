#Blackjack Advice 

dict = {"A": 1, "2": 2, "3":3, "4":4, "5":5 , "6":6, "7":7, "8":8, "9":9, "10":10, "J": 10, "Q": 10, "K":10}

card_type1 = input("What is your first card? ")
card_type2 = input("What is your second card? ")
card_type3 = input("what is your third card? ")

print(dict[card_type1])
print(dict[card_type2])
print(dict[card_type3])

results = dict[card_type1] + dict[card_type2] + dict[card_type3]


if results < 17:
    print(results, "Hit")

elif results >= 17 and results < 21: 
    print(results, "Stay")

elif results == 21:
    print(results, "Blackjack!")

else:
    print(results, "Already Busted!")   