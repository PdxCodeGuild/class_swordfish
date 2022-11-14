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
        remove: function(todo, todos) {
            this.todos.splice(todos.indexOf(todo), 1);
        },
        markComplete: function(todo, todos) {
            todo.completed = !todo.completed
        },
        createTodo: function() {
            this.todos.push({ text: this.newTodo, completed: false})
        }
    },

})