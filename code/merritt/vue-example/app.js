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
      ]
    },
    methods: {
        addExclaimation: function() {
            this.messages.message1 += "!"
            console.log("that's one more exclaimation mark!")
        },
        tellLi: function(liIndex, todoId) {
            console.log(`Todo ${todoId} is li number ${liIndex}`)
        }
    },
    updated: function() {
        console.log("somethign was updated! i wonder what it was?")
    }
  })