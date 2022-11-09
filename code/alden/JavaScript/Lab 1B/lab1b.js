
let alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let code = document.getElementById('code')
let rot = document.getElementById('rot')
console.log(code.value)
rotate.addEventListener("click", function() {
    let fin = []
    for (let char of code.value) {
        if (alf.includes(char)) {
            fin.push(alf[(alf.indexOf(char) + parseFloat(rot.value)) % alf.length])
        }
    }
    result.innerText = fin.join('')
})
// alert(fin.join(''))