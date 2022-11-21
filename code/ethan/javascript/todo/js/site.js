var app4 = new Vue({
    el: '#app',
    data: {
      todoText: 'Todo text',
      todos: [
        {id: 1, text: 'walk the dog', completed: false},
        {id: 2, text: 'brush teeth', completed: false},
        {id: 3, text: 'do homework', completed: true},
      ],
      nextId: 4
    },
    methods: {
        addTodo: function() {
          let newTodo = {
            id: this.nextId,
            text: this.todoText,
            completed: false}
          this.todos.push(newTodo)
          this.todoText = ''
          this.nextId++

        },
        deleteTodo: function(todo) {
          console.log("deleteing",todo)
          let indexToDelete = this.todos.indexOf(todo)
          console.log("index to delete", indexToDelete)
          this.todos.splice(indexToDelete, 1)
        },
        toggleTodo: function(todo) {
          console.log("Toggling,", todo)
          todo.completed = !todo.completed
        }
    
    },
    computed: {
      incompleteTodos: function() {
        return this.todos.filter(
          function(
            todo
          ){
            return todo.completed === false
          }
        )
      },
      completeTodos: function() {
        return this.todos.filter(
          function(
            todo
          ){
            return todo.completed === true
          }
        )
      }
    }
  })
