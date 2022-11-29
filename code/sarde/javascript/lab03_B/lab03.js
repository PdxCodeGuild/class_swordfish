let first_card = document.querySelector('#first_card')
let second_card = document.querySelector('#second_card')
let third_card = document.querySelector('#third_card')
let total_bt = document.querySelector('#total_bt')
let output_div = document.querySelector('#output_div')

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
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}
// console.log(cards)
total_bt.onclick = function () {

    let firstCard = first_card.value
    // let firstCardValue = first_card.value;
    console.log(typeof firstCard)//number
    // let secondCard = parseInt(second_card.value)
    //console.log(secondCard)
    let secondCard = second_card.value
    let thirdCard = third_card.value
    //console.log(thirdCard);
    // let total = firstCard + secondCard + thirdCard
    // console.log(typeof total)//string

    let totalOne = cards[firstCard]
    let totalTwo = cards[secondCard]
    let totalThree = cards[thirdCard]
    let runningTotal = totalOne + totalTwo + totalThree
    console.log(runningTotal)
    output_div.innerText = runningTotal;
    if (runningTotal < 17) {
        // console.log(`${runningTotal} "Hit"`)
        output_div.innerText = `${runningTotal} "Hit"`
    } else if (runningTotal >= 17 & runningTotal < 21) {
        // console.log(`${runningTotal} "Stay"`)
        output_div.innerText = `${runningTotal} "Stay"`
    } else if (runningTotal == 21) {
        // console.log(`${runningTotal} "Blackjack!"`)
        output_div.innerText = `${runningTotal} "Blackjack!"`
    } else {
        // console.log(`${runningTotal} "Already Busteed"`)
        output_div.innerText = `${runningTotal} "Already Busteed"`

    }

}