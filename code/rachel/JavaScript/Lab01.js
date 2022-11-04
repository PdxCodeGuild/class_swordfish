//Unit Converter//
// let meter = 0.3048
// let unit = prompt("Enter the number of feet: ")
// let total_meters = unit * meter

// let output = `${unit} feet is equal to ${total_meters} meters.`

// alert (output)

//Blackjack advice//

//adding or removing quotes around keys doesn't seem to affect anything:
// let card_values = {a: 1, ace: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, j: 10, jack: 10, q: 10, queen: 10, k: 10, king: 10} 

let card_values = {a: 1, Ace: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, j: 10, jack: 10, q: 10, queen: 10, k: 10, king: 10}

var first_card = prompt("What's your first card? ")
var second_card = prompt("What's your second card? ")
var third_card = prompt("What's your third card? ")

//after asking for the 3 card values, didn't return anything:
let value_1 = card_values.first_card
let value_2  = card_values.second_card
let value_3 = card_values.third_card

//after asking for the 3 card values, didn't return anything:
// value_1 = parseInt(value_1)
// value_2 = parseInt(value_2)
// value_3 = parseInt(value_3)
//after asking for the 3 card values, didn't return anything:
// let cards_total = card_values.first_card + card_values.second_card + card_values.third_card 

//neither seems to make a distance - can't move past entering numbers
let cards_total = value_1 + parseInt + parseInt
//let cards_total = parseInt(value_1) + parseInt(value_2) + parseInt(value_3)

//adding ${} around card_totals for each alert: program wouldn't even run
if (cards_total <= 16) {
    alert(cards_total + " hit")
} else if (cards_total <= 20) {
    alert(cards_total + " stay")
} else if (cards_total == 21) {
    alert(cards_total + " blackjack!")
} else if (cards_total > 21) { 
    alert(cards_total + " Busted!")
}