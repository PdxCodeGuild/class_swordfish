// code for a prompt based rot13 ciper

let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let input = prompt('Type your message to cipher: ')
let shift = parseInt(prompt('Please enter the number of places to shift the message: '))


let output = []

for (let i of input) {
    if (alphabet.includes(i)) {
        output.push(alphabet[(alphabet.indexOf(i) + shift) % alphabet.length])
    }
    else {
        alert("please enter lowercase letters only, without spaces")
    }
}

alert(output.join(''))