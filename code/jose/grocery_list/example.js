let newUl = document.createElement('ul')

let li1 = document.createElement('li')
li1.innerText = "thing 1"

let li2 = document.createElement('li')
li2.innerText = "thing 2"

let li3 = document.createElement('li')
li3.innerText = "thing 3"

newUl.appendChild(li1)
newUl.appendChild(li2)
newUl.appendChild(li3)

thatdiv.appendChild(newUl)