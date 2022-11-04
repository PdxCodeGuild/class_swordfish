let card_one = prompt("What's your first card ")

let card_two = prompt("What's your second card? ")

let card_three = prompt("What's your third card? ")

const card_values = {
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

let first_card = card_values[card_one]
let second_card = card_values[card_two]
let thrid_card = card_values[card_three]

let total = first_card + second_card + thrid_card

if (total < 17) {
    alert(total + " Hit")
} else if (total >= 17) {
    alert(total + " Stay")
} else if (total > 21) {
    alert(total + " Already Busted")
} else if (total === 21) {
    alert(total + " Blackjack!")
}