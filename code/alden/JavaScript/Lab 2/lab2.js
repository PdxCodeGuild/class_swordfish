let cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10':10,
    'J': 10,
    'Q': 10,
    'K': 10
}

let first = prompt('Pick first card: ').toUpperCase()
let second = prompt('Pick second card: ').toUpperCase()
let third = prompt('Pick third card: ').toUpperCase()

// console.log(first, second, third)

function value(first, second, third) {
    let totals = [0]
    let selections = [first, second, third]
    for (let key of selections){
        for ( let i=0; i<totals.length; i++){
             totals[i] += cards[key]
        } 
        if (key === 'A') {
            totals.push(totals[totals.length-1] + 10)
        }
    }
    return totals
}

let total = value(first, second, third)

console.log(total)

// let best = total.reverse()
function blackjack(top){
    top = total.reverse()
    for (let i=0; i<top.length; ++i){
        if (top[i] <= 21){
            top = top[i]
            break
        }
    }
    return top
}
let best = blackjack(total)

console.log(best)

if (best < 17) {
    alert(best + ' Hit')

} else if (best < 21) {
    alert(best + ' Stay')

} else if (best === 21) {
    alert(best + ' BlackJack!!')
    
} else if (best > 21) {
    alert(best + ' Already Busted. :(')
}