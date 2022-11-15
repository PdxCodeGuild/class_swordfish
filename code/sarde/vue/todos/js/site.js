// cd todos
// python3.10 -m http.server 8000
// python3.10 -m http.server 8010



const vm = new Vue({
    el: '#app',
    data: {
        newToDoText: '',
        newToDo: {
            id: '',
            text: '',
        },
        newToDoId: 5,

        message: 'Sarde\'s To-do List',
        todos: [
            { id: 1, text: 'Walk the Dog', completed: true },
            { id: 2, text: 'Change Cat Litter', completed: false },
            { id: 3, text: 'Organize Lego\'s', completed: true }
        ]
    },
    methods: {
        addToDo: function () {
            let lengthOfToDos = this.todos.length
            let newId = this.newToDoId
            let newText = this.newToDoText
            // this.newToDo.id = newId
            // this.newToDo.text = newText
            // console.log(lengthOfToDos)//3
            // console.log(newId)//4
            // this.todos.push(this.newToDo)
            this.todos.push(
                {
                    id: newId,
                    text: newText,
                    completed: false,
                }
            )
            this.newToDoId++
            this.newToDoText = ''
            console.log(`${newText} was added to todos with an Id of ${newId}`)
        },
        removeToDo: function (todo) {
            console.log(todo.text)
            let currentIndex = this.todos.indexOf(todo)
            this.todos.splice(currentIndex, 1)

            // this.todos.splice(this.todos.indexOf(todo), 1)
            console.log(`${todo.text} was removed from todos`)

        },
        toggleToDo: function (todo) {
            console.log(todo.text)
            todo.completed = !todo.completed
        }
    },
    computed: {
        completeTodos: function () {
            // Return list of todos where isCompleted == true.
            return this.todos.filter(function (theObject) {
                return theObject.completed === true
            })
        },
        incompleteTodos: function () {
            return this.todos.filter(function (theObject) {
                return theObject.completed === false
            })
        },
    }
})











