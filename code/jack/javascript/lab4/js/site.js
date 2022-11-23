new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        todos: [
          { id: 1, text: 'Learn JavaScript', completed: false },
          { id: 2, text: 'Learn Vue', compeleted: true },
          { id: 3, text: 'Build something awesome', completed: false }
        ]
    },
    computed: { // use computed properties to get complete/incomplete arrays from todos array
        get_completed: function(todos) {
            console.log(todos)
            let completed_todos = []
            for (const todo in todos) {
                if (todo.completed === true) {
                    completed_todos.push(todo)
                }
            }
            return completed_todos
        }
    }

})