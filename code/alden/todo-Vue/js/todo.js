let app = new Vue({
    el: '#app',
    data: {
        message: '',
        todos: [                                // To do list with fillers.
        { id: 1, text: 'Learn JavaScript' },
        { id: 2, text: 'Learn Vue' },
        { id: 3, text: 'Build something awesome' }
      ],
        completed: [],                          // Completed list holder.
        nextId: 4                               // Allow the id to be unique.

    },
    methods: {
        addTodo: function(){                    // Function to add to the to do list.
            let newTodo = {id: this.nextId, text:this.message}
            this.nextId++                       // Adds one to the nextId to make sure the id is unique.
            this.todos.push(newTodo)
        },
        deleteTodo: function(liIndex){          // Removes for list based off index possition.
            this.todos.splice(liIndex, 1)
        },
        completeTodo: function(liIndex){
            this.completed.push(this.todos[liIndex])
            this.todos.splice(liIndex, 1)
        },
        redoTodo: function(liIndex){
            this.todos.push(this.completed[liIndex])
            this.completed.splice(liIndex, 1)
        },
        completeDeleteTodo: function(liIndex){
            this.completed.splice(liIndex, 1)
        }
    }
})