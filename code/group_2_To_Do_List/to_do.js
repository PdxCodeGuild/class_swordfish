let toDoList = document.getElementById('todo')
let addTask = document.getElementById('add_task')
let taskList = document.getElementById('task_list')
let completed = document.getElementById("completed")
let task = document.getElementById('task')


addTask.addEventListener('click', function() {
    let newTask = document.createElement('li')
    newTask.innerText = task.value
    console.log(newTask)
    console.log(task)
    taskList.append(newTask)
    
    
    let newTaskStatus = document.createElement("button")
    newTaskStatus.innerText = "delete"
    newTaskStatus.addEventListener('click', function() {
        newTask.previousSibling.remove()
        newTask.remove()
        newTaskStatus.remove()
    })
    
    taskList.append(newTaskStatus)


    let completedStatus = document.createElement("button")
    completedStatus.innerText = "complete"
    completedStatus.addEventListener('click', function() {
        let completeTask = document.createElement('s')
        console.log(task.value)
        completeTask.innerText = task.value
        console.log(completeTask)
        let listItem = document.createElement("li")
        console.log("List Item ",listItem)
        listItem.append(completeTask)
        completed.append(listItem)

        // newTask.previousSibling.remove()
        newTask.remove()
        newTaskStatus.remove()
        completedStatus.remove()
    
    })

    
    taskList.append(completedStatus)
})
