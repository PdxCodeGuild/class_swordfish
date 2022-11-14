let vm = new Vue({
    el: '#app',
    data: {
        newTodo: '',
        todos: [
          { text: 'Learn JavaScript', completed: false },
          { text: 'Learn Vue', completed: true },
          { text: 'Build something awesome', completed: false },
          { text: 'rule the world', completed: true },
        ]
    },
    methods: {
        remove: function() {
            this.todos.splice(this.todos.indexOf(this.todo), 1);
        },
        markComplete: function(todo) {
            todo.completed = !todo.completed
        },
        createTodo: function() {
            this.todos.push({ text: this.newTodo, completed: false})
            this.newTodo = ''
        }
    },

})