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

let first_card = document.getElementById('first_card')
let second_card = document.getElementById('second_card')
let third_card = document.getElementById('third_card')

totalBtn.addEventListener('click', function() {
    let advice
    let total = values[first_card.value] + values[second_card.value] + values[third_card.value]
        console.log(total)
        if (total === 21) {
            // alert('Blackjack! You win!')
            advice = 'Blackjack! You win!'
            let pTag = document.getElementById('advice')
            pTag.innerText = advice
        }
        else if (total < 21 && total >= 17) {
            // alert('Your total is ' + total + ". Stay.")
            advice = 'Your total is ' + total + '. Stay.'
            let pTag = document.getElementById('advice')
            pTag.innerText = advice
        }
        else if (total < 17 && total > 0) {
            // alert('Your total is ' + total + ". Hit.")
            advice = 'Your total is ' + total + '. Hit.'
            let pTag = document.getElementById('advice')
            pTag.innerText = advice
        }
        else {
            // alert('You bust!')
            advice = 'You bust!'
            let pTag = document.getElementById('advice')
            pTag.innerText = advice
        }
})