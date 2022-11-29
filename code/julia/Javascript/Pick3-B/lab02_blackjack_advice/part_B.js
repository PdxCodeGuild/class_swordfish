// Blackjack advice Part B


let submit = document.querySelector("#submit")


submit.addEventListener('click', function(){
    
    let cardOne = document.querySelector("#card-one").value
    let cardTwo = document.querySelector("#card-two").value
    let cardThree = document.querySelector("#card-three").value
    let gameAdvice = document.querySelector("#advice")
    
    
    
    let cards = {
        "A": 1, "2": 2, "3":3, "4":4, "5":5 , "6":6, 
        "7":7, "8":8, "9":9, "10":10, 
        "J": 10, "Q": 10, "K":10, 
    }

    let firstCard = cards[cardOne]
    let secondCard = cards[cardTwo]
    let thirdCard = cards[cardThree]
    let cardType = firstCard + secondCard + thirdCard
    console.log(cardType)
    

    
  

    // let cardTotal = advice
    if (cardType < 17) {
        advice = " Blackjack advice: Hit!"
    }
    else if (cardType > 17 && cardType < 21) {
        advice = " Blackjack advice: Stay!"
    }
    else if (cardType == 21) {
        advice = " Blackjack!"
    }
    else if(cardType > 21) {
        advice = " Busted!!!!"
    }
    gameAdvice.innerHTML = advice
    console.log(advice)
})


