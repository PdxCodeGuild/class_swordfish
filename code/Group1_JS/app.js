let newItem = document.getElementById("new_item")
let addItemBtn = document.getElementById("add_item")
let todoDiv = document.getElementById("todo-div")
let completeDiv = document.getElementById("complete-div")

// pulling from browser local storage
let data_complete = localStorage.getItem('data_complete') ? JSON.parse(localStorage.getItem('data_complete')) : []
let data_incomplete = localStorage.getItem('data_incomplete') ? JSON.parse(localStorage.getItem('data_incomplete')) : []



function addForReal() {
    let newTodo = document.createElement("li")
    input_string = newItem.value // entered string
    data_incomplete.push(input_string) // add item to data storage variable
    localStorage.setItem("data_incomplete", JSON.stringify(data_incomplete)) // save to local storage
    newTodo.innerText = input_string
    newItem.value = ""

    let newItemComplete = document.createElement("button")
    newItemComplete.innerText = "✓"
    newItemComplete.addEventListener('click', function() {
        newTodo.remove()
        data_complete.push(input_string) // add item to data storage variable
        localStorage.setItem("data_complete", JSON.stringify(data_complete)) // save to local storage
        completeDiv.appendChild(newTodo)
        newItemComplete.remove()
    })

    let removeItem = document.createElement("button")
    removeItem.innerText = "x"
    removeItem.addEventListener('click', function() {
        newTodo.remove()
        removeItem.remove()
        newItemComplete.remove()
    })

    newTodo.appendChild(newItemComplete)
    todoDiv.appendChild(newTodo)
    newTodo.appendChild(removeItem)
}

addItemBtn.addEventListener('click', addForReal)
newItem.addEventListener('keyup', function(event) {
    if (event.key === "Enter") {
        addForReal()
    }
})