new Vue({
    el: '#app',

    data: {
        selectedTodoIndex: null,
        isEditing: false,
        todo: '',
        todoListArray: [],
        todoCompleteArray: []
    },

    methods: {
        storeTodoItem(){
            this.todoListArray.push(this.todo) // pushes users todo into todos
            this.todo = '' // this will reset the input box to be blank when a todo is added.
        },

        editTodoItem(index, todo) {
            this.todo = todo
            this.selectedTodoIndex = index // replaces null index with the user selected todo task.
            this.isEditing = true
        },

        updateTodoItem(){
            this.todoListArray.splice(this.selectedTodoIndex, 1, this.todo) // splices selected index when the user wants to update a todo item.
            this.isEditing = false
        },

        deleteTodoItem(index){
            this.todoListArray.splice(index) // passes index and removes 1 item.
        },

        completeTodoItem(index){
            this.selectedTodoIndex = index
            this.isComplete = true
            this.todoCompleteArray.push(this.selectedTodoIndex)
            this.todoListArray.splice(this.selectedTodoIndex, 1)

             
        },

        deleteCompletedTodo(index) {
            this.todoCompleteArray.splice(index, 1)
        }
    }
})