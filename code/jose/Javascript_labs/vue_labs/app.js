
const vm = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!',
    messages: {
      message1: "Hello Vue!",
      message2: "Goodbye Vue!"
    },
    todos: [
      { id: 1, text: 'Learn JavaScript' },
      { id: 2, text: 'Learn Vue' },
      { id: 3, text: 'Build something awesome' }
    ],
     todo :{}
  },
  methods: {
      addItem: function() {
          this.todos.push({text: this.todo})
      },
      removeItem: function(){
        this.todos.slice(this.todos.indexOf(todo), 1)
      }
      
}})