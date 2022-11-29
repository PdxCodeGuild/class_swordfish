//Blackjack Advice 

let cards = {
    "A": 1, "2": 2, "3":3, "4":4, "5":5 , "6":6, 
    "7":7, "8":8, "9":9, "10":10, 
    "J": 10, "Q": 10, "K":10, 
}

let card_type1 = prompt("What is your first card? (Card Type: K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A)")
let card_type2 = prompt("What is your second card? (Card Type: K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A)")
let card_type3 = prompt("what is your third card? (Card Type: K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A)")

let card_total = cards[card_type1] + cards[card_type2] + cards[card_type3]



if (card_total < 17) {
    alert("Card total: " + card_total + " Hit!")
}
else if (card_total > 17 && card_total < 21) {
    alert("Card total: " + card_total + " Stay!")
}
else if (card_total == 21) {
    alert("Card total: " + card_total + " Blackjack!")
}
else if(card_total > 21) {
    alert("Card total: " + card_total + " Busted!!!!")
}