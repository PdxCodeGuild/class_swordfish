let card_one = document.getElementById('card_one')

let card_two = document.getElementById('card_two')

let card_three = document.getElementById('card_three')
blackjack.addEventListener('click', function() {

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

    let first_card = card_values[card_one.value]
    let second_card = card_values[card_two.value]
    let thrid_card = card_values[card_three.value]


    let total = first_card + second_card + thrid_card

    let answer

    if (total < 17) {
        answer = "Hit"
    } else if (total >= 17 && total < 21) {
        answer = "Stay"
    } else if (total > 21) {
        answer = "Busted"
    } else if (total === 21) {
        answer = "Blackjack!"
    }
    result.innerText = answer
})