card_values = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 1
}


first_card = input("What is your first card?: ").upper()
second_card = input("What is your second card?: ").upper()
third_card = input("What is your third card?: ").upper()

if card_values[first_card]+card_values[second_card]+card_values[third_card] < 17:
    print("Hit.")
elif 21 > card_values[first_card]+card_values[second_card]+card_values[third_card] >= 17:
    print("Stand.")
elif card_values[first_card]+card_values[second_card]+card_values[third_card] == 21:
    print("Winner winner chicken dinner!")
else:
    print("You have busted.")

