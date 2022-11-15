let vm = new Vue({
    el: '#app',
    data: {
        newTodo: '',
        todos: []
    },
    methods: {
        remove: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1);
        },
        markComplete: function(todo) {
            todo.completed = !todo.completed
        },
        createTodo: function() {
            this.todos.push({ text: this.newTodo, completed: false})
            this.newTodo = ''
        }
    },
    beforeMount: function() {
        if (localStorage.getItem('todos') !== null) {
            this.todos = JSON.parse(localStorage.getItem('todos'))
        }
    },
    updated: function() {
        localStorage.setItem('todos', JSON.stringify(this.todos))
    },

})