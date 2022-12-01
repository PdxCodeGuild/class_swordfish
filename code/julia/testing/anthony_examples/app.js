// python -m http.server
new Vue({
    el: '#app',
    data: {
        todoText: "",
        todos: [
          { id: 1, text: "Walk the dog", completed: true, createdDate: new Date() },
          { id: 2, text: "Learn Vue", completed: false, createdDate: new Date() },
          { id: 3, text: "Drink Water", completed: false, createdDate: new Date() },
        ],
        nextTodoId: 4
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
        todo.completed = !todo.completed
      },
      removeTodo: function (todo){
        this.todos = this.todos.filter(function(oldTodo) {
          return oldTodo.id !== todo.id
        })
      }
    },
    computed: {
      incompleteTodos: function(){
        // const notCompleteTodos = []
        // for(let todo of this.todos){
        //   if(todo.completed === false){
        //     notCompleteTodos.push(todo)
        //   }
        // }
        // return notCompleteTodos
  
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