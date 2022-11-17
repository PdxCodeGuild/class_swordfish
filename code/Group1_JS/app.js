let newItem = document.getElementById("new_item")
let addItemBtn = document.getElementById("add_item")
let todoDiv = document.getElementById("todo-div")
let completeDiv = document.getElementById("complete-div")


function addForReal() {
    let newTodo = document.createElement("li")
    newTodo.innerText = newItem.value
    newItem.value = ""

    let newItemComplete = document.createElement("button")
    newItemComplete.innerText = "✓"
    newItemComplete.addEventListener('click', function() {
        newTodo.remove()
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