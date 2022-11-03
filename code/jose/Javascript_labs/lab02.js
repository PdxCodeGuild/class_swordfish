let x = parseInt(prompt("Enter a number: "))

let random_numbers = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',70: 'seventy',80: 'eighty',90: 'ninety',100: 'one hundred',200: 'two hundred',300: 'three hundred',
400: 'four hundred',500: 'five hundred',600: 'six hundred',700: 'seven hundred',800: 'eight hundred',900: 'nine hundred',999 : 'nine hundred ninety nine'}

let ones = {0 : 'zero',1: 'one',2: 'two',3: 'three',4: 'four',5: 'five',6: 'six',7: 'seven',8: 'eight',9: 'nine'}
let tens_under20 = {10: 'ten',11: 'eleven',12: 'twelve',13: 'thirteen',14: 'fourteen',15: 'fifteen',16: 'sixteen',17: 'seventeen',18: 'eighteen',19: 'nineteen'}
let tens_digitwritten = {2: 'twenty',3: 'thirty',4: 'forty',5: 'fifty',6: 'sixty',7: 'seventy',8: 'eighty',9: 'ninety'}

 
var input = ''+x
var intArr = [...input].reduce((int, n)=> int.concat(+n), [] ); // turning the input into an array of numbers
// alert(intArr)

let length_of_array = intArr.length

if (x in random_numbers) {
    alert(random_numbers[x])    
} 
if (x in tens_under20){
    alert[tens_under20[x]]
} else if (length_of_array >= 2 && x >= 20 && x <100){
    let first_word = ones[intArr[0]]
    let second_word = tens_digitwritten[intArr[1]]
    alert(second_word+first_word)
}  else if (length_of_array >= 3 && x >= 100){
    let first_word = ones[intArr[0]]
    let second_word = tens_digitwritten[intArr[1]]
    let third_word = ones[intArr[2]]
    alert(first_word + "hundred "+ second_word+" "+ third_word)
}

// let xlist = Array.from(x)
// var size = Object.keys(xlist).length;
