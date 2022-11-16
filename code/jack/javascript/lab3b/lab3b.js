// blackjack advice lab in js

let options = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
let submit = document.getElementById('submit')
let result = document.getElementById('result')
let card1 = document.getElementById('card1').value.toUpperCase()
    let card2 = document.getElementById('card2').value.toUpperCase()
    let card3 = document.getElementById('card3').value.toUpperCase()

submit.addEventListener('click', function() {
    
    let cards = [card1, card2, card3]

    let total = [0]
    for (let card of cards) {     
        for (let option of Object.getOwnPropertyNames(options)) { // cycles through all options to try to match
            if (option == card) {
                for (let j in total) { // increments each total score scenario, aka number in list
                    total[j] += options[option]
                }
            }
        }
        if (card == 'A') { // if card is ace, create another total score scenario where ace score = 11 instead of 1
            total.push(total[total.length - 1] + 10)
            
        }
    }

    console.log(total)

    let best_total
    for (let score of total) {
        if (score <= 21) {
            best_total = score
        }
    }

    if (best_total < 17) {
        advice = 'Hit'
    }
    else if (best_total < 21) {
        advice = 'Stay'
    }
    else if (best_total == 21) {
        advice = 'Blackjack!'
    }
    else {
        advice = 'Busted!'
    }
    result.innerText = advice
})
