// python -m http.server

const todoListVue = new Vue({
    el: '#todo-list',
    data: {
      newTask : "",
      todos: [],
      nextId : 0
    },
    methods: {
      addTodo: function() {
        this.todos.push({text: this.newTask, id : this.nextId, completed: false}),
        this.newTask = ""
        this.nextId++
      },
      completeTodo: function(todo) {
        todo.completed = !todo.completed   
        },

      delTodo: function(todo) {
        this.todos = this.todos.filter(function(prevTask) {
          return prevTask.id !== todo.id
        })
      }
    },
    computed: {
      unfinishedTodos: function(){
        return this.todos.filter(function(todo){
          return todo.completed === false
        })
      }, 
      finishedTodos: function (){
        return this.todos.filter(function(todo){
          return todo.completed === true
          })
        },
      }
    })