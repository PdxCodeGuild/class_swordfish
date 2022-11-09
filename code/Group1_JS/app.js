let newItem = document.getElementById("new_item")
let addItemBtn = document.getElementById("add_item")
let todoDiv = document.getElementById("todo-div")
let completeDiv = document.getElementById("complete-div")

// pulling from browser local storage, the ? is the ternary operator to say if data exists use, or the : is to set it as an empty array
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
        data_incomplete = removeData(data_incomplete, input_string, 'data_incomplete') 
        completeDiv.appendChild(newTodo)
        newItemComplete.remove()
    })

    let removeItem = document.createElement("button")
    removeItem.innerText = "x"
    removeItem.addEventListener('click', function() {
        removeItem.remove()
        newItemComplete.remove()
        category = newTodo.parentElement.id
        console.log(newTodo)
        if (category == 'complete-div') {
            removeData(data_complete, input_string, 'data_complete')
        }
        else if (category == 'todo-div') {
            removeData(data_incomplete, input_string, 'data_incomplete')
        }
        newTodo.remove()
    })

    newTodo.appendChild(newItemComplete)
    todoDiv.appendChild(newTodo)
    newTodo.appendChild(removeItem)
}

function removeData(array, data, name) {
    varIndex = array.indexOf(data)
    array.splice(varIndex, 1)
    localStorage.setItem(name, JSON.stringify(array)) // this line added to update local storage every run
    return array
}

addItemBtn.addEventListener('click', addForReal)
newItem.addEventListener('keyup', function(event) {
    if (event.key === "Enter") {
        addForReal()
    }
})