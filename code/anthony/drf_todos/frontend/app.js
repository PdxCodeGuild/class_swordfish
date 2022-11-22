
const vue = new Vue({
  el: "#app",
  data: {
    todos: []
  },
  beforeMount: function(){
    axios({
      url: "http://localhost:8000/todos/",
      method: "get"
    }).then(response => {
      console.log(response.data)
      this.todos = response.data
    })
  }
})