//Lab02:ROT Cipher
/*
-Write a program that prompts the user for a string, and encodes it with ROT13
-For each character, find the corresponding character
-add it to an output string.
NOTE: ROT13-replaces a letter with the 13th letter after it in the alphabet
*/
let alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}
// console.log(alphabet)

let rotAlphabet = {
    0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd',
    5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
    10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
    15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
    20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
    25: 'y'
}
// console.log(rotAlphabet)

function rotateBy13(alphabet, rotAlphabet) {
    let inputString = prompt('Enter a word')
    let rotate13 = 13
    // let inputLetters = []
    let numbers = []
    // let outputNumbers = []
    let outputLetters = []



    //iterate over the keys in the alphabet object
    for (let char of inputString) {
        numbers.push(alphabet[char])
        // inputLetters.push(char)
        let outputNumber = (alphabet[char] - rotate13 + 26) % 26
        // outputNumbers.push(outputNumber)
        let outputLetter = rotAlphabet[outputNumber]
        outputLetters.push(outputLetter)
    }
    // alert(inputLetters)
    // console.log(inputLetters)
    // alert(numbers)
    // console.log(numbers)
    // alert(outputNumbers)
    // console.log(outputNumbers)
    // alert(outputLetters)
    // console.log(outputLetters)

    let ciphered = outputLetters.join('')
    return ciphered
}
let ciphered = rotateBy13(alphabet, rotAlphabet)
alert(ciphered)




