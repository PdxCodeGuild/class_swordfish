let card_values = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 1
}
let advice = document.getElementById('advice')

advice.addEventListener('click', function() {
    let first_card = document.getElementById('card_1') // prompt("What is your first card?:").toUpperCase()
    first_card = first_card.value
    let second_card = document.getElementById('card_2') // prompt("What is your second card?:").toUpperCase()
    second_card = second_card.value
    let third_card = document.getElementById('card_3') // prompt("What is your third card?:").toUpperCase()
    third_card = third_card.value
    let total = card_values[first_card]+card_values[second_card]+card_values[third_card]
    let answer


    if (total < 17) {
        answer = `${total}, Hit.`
    } else if (21 > total > 17) {
        answer = `${total}, Stand.`
    } else if (total === 21) {
        answer = `${total}, Winner winner chicken dinner!`
    } else if (21 < total) {
        answer = `${total}, You have busted.`
    }
    result.innerText = answer
})

let text = "hello world".strike()