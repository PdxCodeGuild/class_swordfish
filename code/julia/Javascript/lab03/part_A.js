//ROT Cipher

let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

let rot = 13
let input = prompt('enter a message: ').toLowerCase();

let message_list = []
for (let char of input) {
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
alert(message)