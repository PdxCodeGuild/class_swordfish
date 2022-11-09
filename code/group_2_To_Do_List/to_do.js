let toDoList = document.getElementById('todo')
let addTask = document.getElementById('add_task')
let taskList = document.getElementById('task_list')
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

    let completedStatus = document.createElement("input")
    completedStatus.type = "checkbox"
    
    completedStatus.addEventListener('click', function() {
        completedStatus.value = True
    })
    
    taskList.append(completedStatus)
})
