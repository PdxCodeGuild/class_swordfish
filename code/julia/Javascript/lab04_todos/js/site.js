// run this command: python -m http.server
new Vue({
    el: '#app',
    data: {
        todoText: "",
        todos: [
            {id: 1, text: "Clean the bedroom", completed: true, createdDate: new Date()},
            {id: 2, text: "Go grocery shopping", completed: false, createdDate: new Date()},
            {id: 3, text: "Wash the car", completed: false, createdDate: new Date()},
            {id: 4, text: "Do homework", completed: false, createdDate: new Date() },
        ],
        nextTodoId: 5
    },
    methods:{
        addTodo: function(){
          let newTodo = {
            id: this.nextTodoId,
            text: this.todoText,
            completed: false,
            createdDate: new Date()
          }
          this.todos.push(newTodo)
          this.nextTodoId++
          this.todoText = ""
        },
        
        toggleTodo: function (todo) {
          console.log("before toggle", todo.completed)
          todo.completed = !todo.completed
          console.log("After toggle", todo.completed)
        },

        removeTodo: function (todo){
          this.todos = this.todos.filter(function(oldTodo) {
            return oldTodo.id !== todo.id
          })
        }
      },
      computed: {
        incompleteTodos: function(){
          return this.todos.filter(function(todo){
            return todo.completed === false
          })
        },

        completedTodos: function () {
          return this.todos.filter(function(todo){
            return todo.completed === true
          })
        }
      }
    
})