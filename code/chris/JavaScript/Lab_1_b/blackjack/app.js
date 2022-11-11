let card_1 = document.getElementById('card_1')
let card_2 = document.getElementById('card_2')
let card_3 = document.getElementById('card_3')

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

hit_me.addEventListener('click', function() {
    let card_total = card_combos[card_1.value] + card_combos[card_2.value] + card_combos[card_3.value]
    console.log(card_total)
        if (card_total > 0 && card_total < 17) {
            alert(card_total + "-" + 'Hit')
        } else if (card_total >= 17 && card_total < 21) {
            alert(card_total + "-" + 'Stay')
        } else if (card_total === 21) {
            alert(card_total + "-" + 'Blackjack!!!')
        } else {
            alert('Busted!')
        }
})