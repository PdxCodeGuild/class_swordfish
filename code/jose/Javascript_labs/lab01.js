let card_values = {
    'A': 1,
'K': 10,
'Q': 10,
'J': 10,
'10': 10,
'9': 9,
'8': 8,
'7': 7,
'6': 6,
'5': 5,
'4': 4,
'3': 3,
'2': 2
}

let user_card1 = prompt("Enter your first card: ")
let user_card2 = prompt("Enter your second card: ")
let user_card3 = prompt("Enter your third card: ")

let usercard1 = parseInt(card_values[user_card1])
let usercard2 = parseInt(card_values[user_card2])
let usercard3 = parseInt(card_values[user_card3])

let total_user_card = usercard1 + usercard2 + usercard3

alert("Your total is " + total_user_card)

if (total_user_card < 17) {
    alert("You should hit.")
} else if (total_user_card <= 20){
    alert("You should stay.")
} else if (total_user_card === 21){
    alert("Blackjack! You Win!")
} else if (total_user_card > 21) {
    alert("Busted, you lose =(")
}
