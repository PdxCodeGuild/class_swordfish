var app4 = new Vue({
    el: '#app',
    data: {
      message: 'Todo text',
      incompleteTodos: [{text: 'walk the dog', completed: false}],
      completeTodos: [],
    },
    methods: {
        addTodo: function() {
          let newTodo = {
            text: this.message,
            completed: false}
          this.incompleteTodos.push(newTodo),
          this.message = ''
        },
        deleteTodo: function(index) {
          this.incompleteTodos.splice(index, 1)
        },
        deleteCompleteTodo: function(index) {
          this.completeTodos.splice(index, 1)
        },
        completeTodo: function(index) {
          let completeTodo = {
            text: index.text,
            completed: true
          }
          this.completeTodos.push(completeTodo)
          this.incompleteTodos.splice(index, 1)
        },
        incompleteTodo: function(index) {
          this.incompleteTodos.push(index)
          this.completeTodos.splice(index, 1)
        }
    }
  })
