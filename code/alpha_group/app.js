let adds = document.getElementById("add_list")
let addButton = document.getElementById("add")
let textDiv = document.getElementById("text-div")
let todoUL = document.getElementById("element")
let completedTask = document.getElementById("completed")

addButton.addEventListener('click', function() {
    let listElement = document.createElement("li")
    listElement.innerText = adds.value
    todoUL.append(listElement)
    // for (let i=0; i < todoList.length; i++) {
    //     todoList[i].innerText = adds.value
    //     }
    let listInnertext = listElement.innerText


    let newTextRemove = document.createElement("button")
    newTextRemove.innerText = "x"
    newTextRemove.addEventListener('click', function() {
        // listElement.previousSibling.remove()
        listElement.remove()
        newTextRemove.remove()
    })

    listElement.appendChild(newTextRemove)
    // console.log(listElement)
    // console.log(listElement.innerText)
    let completeButton = document.createElement("button")
    completeButton.innerText = "C"
    completeButton.addEventListener('click', function() {
        
        let completedList = document.createElement("li")
        // completedList.innerText = listInnertext
        let strike = document.createElement("s")
        strike.innerText = listInnertext
        completedList.append(strike)
        completedTask.append(completedList)
        listElement.remove()
        newTextRemove.remove()
    })
    
    listElement.appendChild(completeButton)
    
})
