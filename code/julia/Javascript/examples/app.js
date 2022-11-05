// unitConverter

let numberOne = prompt("Give me a number: ")
let numberTwo = prompt("Give me another number: ")

console.log("First number: " + numberOne)
console.log("Second number: " + numberTwo)


function multiply(numA, numB) {


    let result = numA * numB
    return result


}
//console.log(numA) not defined outside of function
let answer = multiply(numberOne, numberTwo)

alert("The numbers are: " + numberOne + ", " + numberTwo)
alert("The multiplication for the two numbers are: " + answer)


let wordToNumbers = {
    one: 1,
    two: 2,
    three: 3,
}
let chosenNumber = prompt("Choose a number (one, two, three): ") 
console.log(chosenNumber + ", " + wordToNumbers[chosenNumber])
alert(chosenNumber + ", " + wordToNumbers[chosenNumber])