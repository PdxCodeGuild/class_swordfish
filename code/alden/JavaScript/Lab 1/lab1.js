
let alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let code = prompt('Please type your message: ')
let rot = parseInt(prompt('Please enter rotation number(1-26): '))


let fin = []
for (let char of code) {
    if (alf.includes(char)) {
        fin.push(alf[(alf.indexOf(char) + rot) % alf.length])
    }
}



alert(fin.join(''))