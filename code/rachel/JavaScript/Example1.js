// let a = document.getElementById('mydiv');
// let bs = document.getElementsByTagName('div');
// console.log(bs.length); // 3
// let cs = document.getElementsByName('adiv');
// console.log(cs.length); // 2
// let d = document.querySelector('#mydiv');
// let es = document.querySelectorAll('.myclass');
// console.log(es.length); // 2

// let mydiv = document.getElementById('mydiv')
// let thisdiv = document.getElementById('thisdiv')
// let thatdiv = document.getElementById('thatdiv')
// let myClass = document.getElementsByClassName('myclass')


// thisdiv.innerText = "Hello world!"
// mydiv.innerText = "I'm a div!"
// thatdiv.innerText = "I'm a cool div!"

// mydiv.innerHTML += "<p><strong><em>Some text!!!</em></strong></p>"

// // mydiv.style.color = "whitesmoke"
// // thisdiv.style.color = "whitesmoke"
// // thatdiv.style.color = "whitesmoke"

// for (let i=0; i<myClass.length; i++) {
//     myClass[i].style.color = "whitesmoke"
// }

// let newUl = document.createElement('ul')

// let li1 = document.createElement('li')
// li1.innerText = "thing 1"

// let li2 = document.createElement('li')
// li2.innerText = "thing 2"

// let li3 = document.createElement('li')
// li3.innerText = "thing 3"

// newUl.appendChild(li1)
// newUl.appendChild(li2)
// newUl.appendChild(li3)

// thatdiv.appendChild(newUl)

let num1 = document.getElementById('num1')
let num2 = document.getElementById('num2')
let operation = document.getElementById('operation')
let calculate = document.getElementById('calculate')
let result = document.getElementById('result')

calculate.addEventListener('click', function() {
    let answer
    if (operation.value === 'add') {
        answer = parseFloat(num1.value) + parseFloat(num2.value)
    } else if (operation.value === 'sub') {
        answer = parseFloat(num1.value) - parseFloat(num2.value)
    } else if (operation.value === 'mul') {
        answer = parseFloat(num1.value) * parseFloat(num2.value)
    } else if (operation.value === 'div') {
        answer = parseFloat(num1.value) / parseFloat(num2.value)
    }
    result.innerText = answer
})