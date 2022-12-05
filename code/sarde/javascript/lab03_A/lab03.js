//Lab 3: Blackjack Advice
/*
Write a program to give basic blackjack playing advice
during a game by asking the player for cards
    -First, ask the user for three playing cards
            (A,2,3,4,5,6,7,8,9,10,J,Q,K)
    -Second, figure point of value of each card
            (number cards = worth their number)
            (face cards = 10)
            (A = 1)

-less than 17 -->'Hit'
-greater than or equal to 17 BUT less than 21 --> 'Stay'
-21 --> 'Blackjack'
-greater than 21 --> 'Already Busteed
*/

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
console.log(cards)

function addInputCards(cards) {
    //ask the user for first, second and third card
    let firstCard = prompt('What\'s your first card?')
    let secondCard = prompt('What\'s your second card?')
    let thirdCard = prompt('What\'s your third card?')

    let firstCardValue = cards[firstCard]
    // console.log(firstCardValue)
    let secondCardValue = cards[secondCard]
    let thirdCardValue = cards[thirdCard]

    let cardsTotal = firstCardValue + secondCardValue + thirdCardValue
    // console.log(cardsTotal)
    if (cardsTotal < 17) {
        console.log(`${cardsTotal} "Hit"`)
    } else if (cardsTotal >= 17 & cardsTotal < 21) {
        console.log(`${cardsTotal} "Stay"`)
    } else if (cardsTotal == 21) {
        console.log(`${cardsTotal} "Blackjack!"`)
    } else {
        console.log(`${cardsTotal} "Already Busteed"`)

    }
    return


}
addInputCards(cards)