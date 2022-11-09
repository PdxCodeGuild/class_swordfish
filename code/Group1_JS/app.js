let newItem = document.getElementById("new_item")
let addItemBtn = document.getElementById("add_item")
let todoDiv = document.getElementById("todo-div")
let completeDiv = document.getElementById("complete-div")


addItemBtn.addEventListener('click', function() {
    let newTodo = document.createElement("li")
    newTodo.innerText = newItem.value
    todoDiv.appendChild(newTodo)
})