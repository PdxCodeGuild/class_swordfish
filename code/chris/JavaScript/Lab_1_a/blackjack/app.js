const card_combos = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,
}

let card_1 = prompt('What is your first card? ')
let card_2 = prompt('What is your second card? ')
let card_3 = prompt('What is your third card? ')

let card_total = card_combos[card_1] + card_combos[card_2] + card_combos[card_3]
// alert(card_total)

if (card_total > 0 && card_total < 17) {
    alert(card_total + "-" + 'Hit')
} else if (card_total >= 17 && card_total < 21) {
    alert(card_total + "-" + 'Stay')
} else if (card_total === 21) {
    alert(card_total + "-" + 'Blackjack!!!')
} else {
    alert('Busted!')
}

