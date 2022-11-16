const toDo = new Vue({
  el: '#toDo',
  data: {
    task: "",
    todos: [
      { id:1, text: 'Call Michelle', complete: false},
      { id:2, text: 'Call Anthony', complete: false},
    ],
    nextId: 3,
  },
  computed: {
    completed: function () {
      return this.todos.filter(function(todo) {
        return todo.complete === true
      })
    },
    incomplete: function () {
        return this.todos.filter(function(todo) {
          return todo.complete === false
        })
    },
  },
  methods: {
    createTodo: function() {
      lenTodos = this.todos.length
      newId = this.nextId
      this.nextId++
      console.log(lenTodos)
      this.todos.push({id: newId, text: this.task, complete: false})
    },
    removeButton: function(payload) {
      this.todos.indexOf(payload)
      console.log(payload)
      console.log(this.todos.indexOf(payload))
      this.todos.splice(this.todos.indexOf(payload), 1)
    },
    toggleButton: function(payload) {
      let objectTomove = this.todos.indexOf(payload)
      this.todos[objectTomove].complete = !this.todos[objectTomove].complete
      // console.log(objectTomove)
    }
  }
})