// code for a prompt based rot13 ciper

let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let input = prompt('Type your message to cipher: ')
let shift = parseInt(prompt('Please enter the number of places to shift the message: '))


let output = []

// this cycles through each character in the input string, and adds the shifted character the the output array
for (let i of input) {
    if (alphabet.includes(i)) {
        meters.push(alphabet[(alphabet.indexOf(i) + shift) % alphabet.length])
    }
    else {
        alert("please enter lowercase letters only, without spaces")
    }
}

alert(meters.join(''))