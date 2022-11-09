let toDoList = document.getElementById('todo')
let addTask = document.getElementById('add_task')
let taskList = document.getElementById('task_list')
let task = document.getElementById('task')


addTask.addEventListener('click', function() {
    let newTask = document.createElement('li')
    newTask.innerText = task
    console.log(newTask)
    console.log(task)
})
