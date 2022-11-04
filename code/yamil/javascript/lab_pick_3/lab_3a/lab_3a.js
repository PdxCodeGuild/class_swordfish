let card_values = {
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

let first_card = prompt("What is your first card?:").toUpperCase()
let second_card = prompt("What is your second card?:").toUpperCase()
let third_card = prompt("What is your third card?:").toUpperCase()
let total = card_values[first_card]+card_values[second_card]+card_values[third_card]

if (total < 17) {
    alert(`${total}, Hit.`)
} else if (21 > total > 17) {
    alert(`${total}, Stand.`)
} else if (total === 21) {
alert(`${total}, Winner winner chicken dinner!`)
} else if (21 < total) {
alert(`${total}, You have busted.`)
}
