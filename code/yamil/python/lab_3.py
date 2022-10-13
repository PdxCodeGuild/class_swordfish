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
total = card_values[first_card]+card_values[second_card]+card_values[third_card]

if total < 17:
    print(f"{total}, Hit.")
elif 21 > total >= 17:
    print(f"{total}, Stand.")
elif total == 21:
    print(f"{total}! Winner winner chicken dinner!")
elif 21 < total:
    print(f"{total} You have busted.")