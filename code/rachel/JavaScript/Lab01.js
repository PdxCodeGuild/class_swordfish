//Unit Converter//
// let meter = 0.3048
// let unit = prompt("Enter the number of feet: ")
// let total_meters = unit * meter

// let output = `${unit} feet is equal to ${total_meters} meters.`

// alert (output)

//Blackjack advice//
let card_values = {a: 1, Ace: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, j: 10, jack: 10, q: 10, queen: 10, k: 10, king: 10}

let first_card = prompt("What's your first card? ")
let second_card = prompt("What's your second card? ")
let third_card = prompt("What's your third card? ")

let cards_total = first_card + second_card + third_card

if (cards_total <= 16) {
    alert(cards_total + "hit")
} else if (cards_total <= 20) {
    alert(cards_total + "stay")
} else if (cards_total == 21) {
    alert(cards_total + "blackjack!")
} else if (cards_total > 21) { 
    alert(cards_total + "Busted!")
}