var app4 = new Vue({
    el: '#app',
    data: {
      message: 'Todo text',
      incompleteTodos: [],
      completeTodos: [],
    },
    methods: {
        addTodo: function() {
          this.incompleteTodos.push(this.message)
        },
        deleteTodo: function(index) {
          this.incompleteTodos.splice(index, 1)
        },
        deleteCompleteTodo: function(index) {
          this.completeTodos.splice(index, 1)
        },
        completeTodo: function(index) {
          this.completeTodos.push(this.message)
          this.incompleteTodos.splice(index, 1)
        }
    }
  })
