const values = {
    'A':1,
    'a':1,
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
    'j':10,
    'Q':10,
    'q':10,
    'K':10,
    'k':10,
}


let first_card = prompt('What is your first card? ')
let second_card = prompt('What is your second card? ')
let third_card = prompt('What is your third card? ')

let total = values[first_card] + values[second_card] + values[third_card]

// alert('Your total is ' + total)

if (total === 21) {
    alert('Blackjack! You win!')
}
else if (total < 21 && total >= 17) {
    alert('Your total is ' + total + ". Stay.")
}
else if (total < 17 && total > 0) {
    alert('Your total is ' + total + ". Hit.")
}
else {
    alert('You bust!')
}