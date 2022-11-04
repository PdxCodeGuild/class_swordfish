const face_cards = {
    king: 10,
    queen: 10,
    jack: 10,
    10: 10,
    9: 9,
    8: 8,
    7: 7,
    6: 6,
    5: 5,
    4: 4,
    3: 3,
    2: 2,
    ace: 1,
}

let card_one = prompt("what is your first card?")

let card_two = prompt("what is your second card?")

let card_three = prompt("what is your third card?")

let card_total = face_cards[card_one] + face_cards[card_two] + face_cards[card_three]

alert(card_total)

if (card_total < 17) {
    alert("Card total: " + card_total + " Advised action: Hit!")
}
else if (card_total > 17 && card_total < 21) {
    alert("Card total: " + card_total + " Advised action: Stay!")
}
else if (card_total == 21) {
    alert("Card total: " + card_total + " Advised action: Winner!")
}
else if(card_total > 21) {
    alert("Card total: " + card_total + " Advised action: Bust! You LOSE!!!!!!!!")
}
