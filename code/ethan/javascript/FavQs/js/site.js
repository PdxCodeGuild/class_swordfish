Vue.component('quotes', {
  data: function() {
      return {
      }
  },
  props: ['quote'],
  template: 
  `<div>
      <ul>
          <li>{{quote.body}}<br>
           - {{quote.author}}</li>
      </ul>
  </div>`
})

var app = new Vue({
  el: '#app',
  data: {
    search: "",
    quotes: {},
    parameters:{},

  },
  methods: {
    getQuotes: function() {
      axios({
          method: "GET",
          url: "https://favqs.com/api/quotes/",
          headers: {
              'Authorization': 'Token token="9daa8830e1b3e3a7b44eda726857db04"'
          },
          params: this.parameters
      }).then((response) => {
          this.quotes = response.data
          console.log(this.data)
      }) 
    }  
  },
  computed: {

  },
  beforeMount: function () {
      this.getQuotes()
  }
})