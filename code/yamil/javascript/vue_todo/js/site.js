// python -m http.server

const todoListVue = new Vue({
    el: '#todo-list',
    data: {
      newTask : "",
      todos: [],
      nextId : 1
    },

    methods: {
      addTodo: function() {
        this.todos.push({text: this.newTask, id : this.nextId, finished: false}),
        this.newTask = ""
        this.nextId++
      },
      completeTodo: function(todo) {
        todo.finished = !todo.finished      
        },

      delTodo: function(todo) {
        this.todos = this.todos.filter(function(prevTask) {
          return prevTask.id !== todo.id
        })
      }
    },

    computed: {
        finishedTodos: function () {
          return this.todos.filter(function(todo){
            return todo.completed === true
          })
        },
        unfinishedTodos: function() {
          return this.todos.filter(function(todo){
            return todo.completed === false
          })
        }, 
      }
    })