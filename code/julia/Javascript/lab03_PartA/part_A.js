// Blackjack Advice 

let dict = {"A": 1, "2": 2, "3":3, "4":4, "5":5 , "6":6, "7":7, "8":8, "9":9, "10":10, "J": 10, "Q": 10, "K":10}

let card_type1 = prompt("What is your first card? ")
let card_type2 = prompt("What is your second card? ")
let card_type3 = prompt("what is your third card? ")

// alert(dict[card_type1] + [card_type2] + [card_type3])
// alert(dict[card_type2])
// alert(dict[card_type3])

let type_one = dict[card_type1]
let type_two = dict[card_type2]
let type_three = dict[card_type3]

let results = type_one + type_two + type_three
alert("Your results are: " + results)

if (results < 17){
    alert(results + " Hit");

}else if(results >= 17){
    alert(results + " Stay");

}else if (results == 21, results < 21){
    alert(results + " Blackjack!");

}else{
    alert(results + " Already Busted!");   
}
