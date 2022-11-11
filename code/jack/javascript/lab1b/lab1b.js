// ROT 13 python lab in js

let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
let rot = 13
let code = document.getElementById('code')
let result = document.getElementById('result')


code.addEventListener('click', function() {
    let message = document.getElementById('message') // had to put this within function to get it to work repeatedly
    let message_list = []
    for (let char of message.value) {
        if (alphabet.includes(char)) { // rotates character if it's a letter
            let char_i = alphabet.indexOf(char) // index of character in alphabet
            char_i = (char_i + rot) % alphabet.length // rotate by 13
            char_rot = alphabet[char_i]
            message_list.push(char_rot)
        }
        else { // handles non-letter characters
            message_list.push(char)
        }
    }
    message = message_list.join('')
    result.innerText = message
})