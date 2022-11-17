const vm = new Vue({
	el: '#app',
	data: {
        // created placeholder data
        todos: [
            { id: 1, text: "walk the dog", completed: false, createdDate: new Date(), },
		    { id: 2, text: "learn vue", completed: true, createdDate: new Date(), },
		    { id: 3, text: "drink water", completed: true, createdDate: new Date(), }
        ],
        // need to create an empty variable here to allow us to reference the input text
        inputText: '', 
	},
	methods:{
        addTodo: function() {
            let newItem = {
                id: 4,
                text: this.inputText,
                completed: false,
                createdDate: new Date(),
            }
            console.log(newItem)
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