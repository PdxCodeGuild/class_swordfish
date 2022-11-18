new Vue({
    el: '#app',

    data: {
        todoText: '',
        todoArray: [
        { id: 0, text: 'walk the pugs, before they overthrow me.' },
        { id: 1, text: "give the cat treats, before he attacks from the shadows." },
      ],
        todoId: 2,
        completedTodoArray: []
    },
    methods: {
        storeTodoItem: function(){
            let todo = {id: this.todoId, text:this.todoText}
            this.todoId++
            // console.log(todo)
            this.todoArray.push(todo)
            this.todoText = ''
        },
        deleteTodoItem(index){
            this.todoArray.splice(index, 1)
        },
        completeTodoItem(index){
            this.completedTodoArray.push(this.todoArray[index])
            this.todoArray.splice(index, 1)
        },
        redoTodoItem(index){
            this.todoArray.push(this.completedTodoArray[index])
            this.completedTodoArray.splice(index, 1)
        },
        deleteCompletedTodo(index){
            this.completedTodoArray.splice(index, 1)
        }
    }
})