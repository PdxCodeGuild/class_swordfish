let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let input = document.getElementById('input')
let shift = document.getElementById('shift')
let output = []

cipherBtn.addEventListener('click', function(){
    let answer
    for (let i of input.value) {
        if (alphabet.includes(i)) {
            output.push(alphabet[(alphabet.indexOf(i) + parseFloat(shift.value)) % alphabet.length])
        }
        else {
            alert("please enter lowercase letters only, without spaces")
        }
    }
    answer = output.join('')
    // console.log(answer)
    let pTag = document.getElementById('answer')
    pTag.innerText = answer
    // alert(output.join(''))
})