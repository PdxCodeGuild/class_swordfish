const vm = new Vue({
	el: '#app',
	data: {
        // created placeholder data
        todos: [
            { id: 1, text: "walk the dog", completed: false, createdDate: new Date(), },
		    { id: 2, text: "learn vue", completed: true, createdDate: new Date(), },
		    { id: 3, text: "water the cat", completed: true, createdDate: new Date(), }
        ],
        // need to create an empty variable here to allow us to reference the input text
        inputText: '', 
        nextTodoId: 4,
	},
	methods:{
        addTodo: function() {
            let newItem = {
                id: this.nextTodoId,
                text: this.inputText,
                completed: false,
                createdDate: new Date(),
            }
            console.log(newItem)
            this.todos.push(newItem)
            this.nextTodoId++
            // console.log(this.nextTodoId)
            this.inputText = "" // this resets the textfield to an empty string when the function is executed
        },
        toggleTodo: function(todos){
            todos.completed = !todos.completed
        }
	},
	computed:{
        incompleteTodos: function() {
            const temp = [] // this variable only exists in this function
            for(let todo of this.todos) { // this loops through each of the todos
                if(todo.completed===false){ 
                    temp.push(todo) // adds the todo to the 
                }
            }
            return temp
        },
        // this can also be completed with Array.filter() and works the same as above
        completeTodos: function() {
            return this.todos.filter(function(item) {
                return item.completed===true
            })
        
            // return this.todos.filter(item => item.completed === true);
            //  Option 3: his was another example from the documentation that works the same             
        }
	}
})