
new Vue({
  el: "#app",
  data: {
    todos: []
  },
  methods: {
    getTodos: function() {
      axios({
        method: "GET",
        url: "https://jsonplaceholder.typicode.com/todos/"
      }).then((response) => {
        this.todos = response.data
      })
    }
  },
  computed: {

  },
  created: function(){

  },
  beforeMount: function() {
    this.getTodos()
  },
  mounted: function(){

  },
})


add(3, 4)
// function
function add(x, y){
  return x + y
}

// arrow function
const addArrow = (x, y) => {
  return x + y
}
addArrow()







// const getDataBtn = document.querySelector('#get-data')
const responseDiv = document.querySelector('#response')

// getDataBtn.addEventListener("click", getData)

function getData() {
  // Make the request, axios will respond with a promise
  axios({
    method: "GET",
    url: "https://jsonplaceholder.typicode.com/todos/1"
  }).then(function(response) { // handle promise success
    console.log("response", response.data)
    responseDiv.textContent = `title: ${response.data.title} completed: ${response.data.completed}`
  }).catch(function(error){  // handle promise rejection
    console.error(error)
  })
}