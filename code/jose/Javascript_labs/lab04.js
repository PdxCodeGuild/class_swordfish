let card_values = {
    'A': 1,
'K': 10,
'Q': 10,
'J': 10,
'10': 10,
'9': 9,
'8': 8,
'7': 7,
'6': 6,
'5': 5,
'4': 4,
'3': 3,
'2': 2
}

let user_card1 = document.getElementById('card1')
let user_card2 = document.getElementById('card2')
let user_card3 = document.getElementById('card3')

let usercard1 = parseInt(card_values[user_card1])
let usercard2 = parseInt(card_values[user_card2])
let usercard3 = parseInt(card_values[user_card3])

let calculate = document.getElementById("calculate")
let result= document.getElementById("result")


calculate.addEventListener('click', function(){
    let total_user_card = usercard1 + usercard2 + usercard3
    let advice
    // for (let i=0 ; i < nums.lenght; i++){
    //     answer =+ parseFloat(nums[i].value)
    // }
    if (total_user_card < 17) {
        advice = "You should Hit."
    }  else if (total_user_card <= 20) {
        advice = "You should stay."
    } else if (total_user_card === 21){
        advice = "Blackjack! You Win!"
    } else if (total_user_card > 21){
        advice = "Busted =( You Lose."
    }
    result.innerText = advice
})


// alert("Your total is " + total_user_card)

// if (total_user_card < 17) {
//     alert("You should hit.")
// } else if (total_user_card <= 20){
//     alert("You should stay.")
// } else if (total_user_card === 21){
//     alert("Blackjack! You Win!")
// } else if (total_user_card > 21) {
//     alert("Busted, you lose =(")}