let word_input = document.querySelector('#word_input');
let cipher_bt = document.querySelector('#cipher_bt');
let output_div = document.querySelector('#output_div');
cipher_bt.onclick = function () {
    let alphabet = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26
    }
    console.log(alphabet)
    let rotAlphabet = {
        0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd',
        5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
        10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
        15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
        20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
        25: 'y'
    }
    console.log(rotAlphabet)
    let word = word_input.value;
    console.log(word);
    let rotate13 = 13
    let numbers = []
    let outputLetters = []
    for (let char of word) {
        numbers.push(alphabet[char])
        // output_div.innerText = ;
        let outputNumber = (alphabet[char] - rotate13 + 26) % 26
        console.log(outputNumber)
        let outputLetter = rotAlphabet[outputNumber]
        outputLetters.push(outputLetter)

    }
    let ciphered = outputLetters.join('')
    console.log(ciphered)
    output_div.innerText = ciphered
    return ciphered
}