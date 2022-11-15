// python -m http.server

const todoListVue = new Vue({
    el: '#todo-list',
    data: {
      newTask : "",
      completedTask: "",
      todos: [],
      completed: []
    },
    methods: {
      addTodo: function() {
        this.todos.push({text: this.newTask})
      },
      completeTodo: function() {
          this.completed.push({text: this.})
        },
      }
    
  })
  