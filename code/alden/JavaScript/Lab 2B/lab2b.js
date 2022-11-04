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

let first = document.getElementById('first')
let second = document.getElementById('second')
let third = document.getElementById('third')

// console.log(first, second, third)

function values(first, second, third) {
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


// console.log(total)

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


// console.log(best)
result.addEventListener('click', function())
let total = values(first.value, second.value, third.value)
let best = blackjack(total)
if (best < 17) {
    alert(best + ' Hit')

} else if (best < 21) {
    alert(best + ' Stay')

} else if (best === 21) {
    alert(best + ' BlackJack!!')
    
} else if (best > 21) {
    alert(best + ' Already Busted. :(')
}