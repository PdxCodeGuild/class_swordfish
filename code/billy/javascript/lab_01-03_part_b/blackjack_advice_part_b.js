const cardValues = {
    king: 10,
    queen: 10,
    jack: 10,
    10: 10,
    9: 9,
    8: 8,
    7: 7,
    6: 6,
    5: 5,
    4: 4,
    3: 3,
    2: 2,
    ace: 1,
}
let submit = document.getElementById('submit')
let advice = document.getElementById('advice')

submit.addEventListener('click', function() {
    let cardOne = document.getElementById('cardOne').value.toLowerCase()
    let cardTwo = document.getElementById('cardTwo').value.toLowerCase()
    let cardThree = document.getElementById('cardThree').value.toLowerCase()
    let cardSelection = [cardOne, cardTwo, cardThree]
    let cardScore = [0]
    for (let card of cardSelection) {     
        for (let key of Object.getOwnPropertyNames(cardValues)) {
            if (key == card) {
                for (let i in cardScore) {
                    cardScore[i] += cardValues[key]
                }
            }
        }
    }

    console.log(cardScore)
    
    let totalCardScore
    for(let score of cardScore) {
        if (score <= 21) {
            totalCardScore = score
        }
    }
    if (totalCardScore <= 17){
        blackJackAdvice = 'Advice for your next move: Hit!'
    }
    else if (totalCardScore > 17 && cardScore < 21){
        blackJackAdvice = 'Advice for your next move: Stay!'
    }
    else if (totalCardScore <= 21){
        blackJackAdvice = 'Winner!!!'
    }
    else if(totalCardScore > 21){
        blackJackAdvice = 'Bust! LOSER!!'
    }
    advice.innerText = blackJackAdvice
})
