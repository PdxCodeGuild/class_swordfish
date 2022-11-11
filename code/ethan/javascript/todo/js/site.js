var app4 = new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue',
      todos: [
        { text: 'Learn JavaScript' },
        { text: 'Learn Vue' },
        { text: 'Build something awesome' }
      ]
    },
    methods: {
        addTodo: function() {
            todos.push(this.message)
        }
    }
  })
