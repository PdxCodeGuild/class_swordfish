// blackjack advice lab in js

let options = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

let cards = [...Array(3).keys()] // spread expands keys into array

let total = [0]
for (let i of cards) {
    cards[i] = prompt('what is card #' + (i + 1)).toUpperCase()
    
    for (let option of Object.getOwnPropertyNames(options)) { // cycles through all options to try to match
        if (option == cards[i]) {
            for (let j in total) { // increments each total score scenario, aka number in list
                total[j] += options[option]
            }
        }
    }

    if (cards[i] == 'A') { // if card is ace, create another total score scenario where ace score = 11 instead of 1
        total.push(total[total.length - 1] + 10)
    }
}

let best_total
for (let score of total) {
    if (score <= 21) {
        best_total = score
    }
}

if (best_total < 17) {
    alert('Hit')
}
else if (best_total < 21) {
    alert('Stay')
}
else if (best_total == 21) {
    alert('Blackjack!')
}
else {
    alert('Busted!')
}