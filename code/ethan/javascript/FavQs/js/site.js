Vue.component('quotes', {
  data: function() {
      return {
      }
  },
  props: ['quote'],
  template: 
  `
  <div>
      <ul>
          <li>{{quote.body}}<br>
           - {{quote.author}}</li>
      </ul>
  </div>
  `
})

var app = new Vue({
  el: '#app',
  data: {
    type: "",
    keywordSearch: "",
    inputSearch: "",
    inputType: "",    
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
      }).then((response) => {
          this.quotes = response.data
      }) 
    },
    getQuotesSearch: function() {
      this.inputSearch = this.keywordSearch
      this.inputType = this.type
      axios({
          method: "GET",
          url: "https://favqs.com/api/quotes/",
          headers: {
              'Authorization': 'Token token="9daa8830e1b3e3a7b44eda726857db04"'
          },
          params: {

            filter: this.inputSearch,
            type: this.inputType
          }
      }).then((response) => {
          this.quotes = response.data
      }) 
    },
    
    nextPage: function() {
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes',
        headers: {
            'Authorization': 'Token token="9daa8830e1b3e3a7b44eda726857db04"'
        },
        params: {
          filter: this.inputSearch,
          type: this.inputType,
          page: this.quotes.page + 1
        }
      }).then((response) => { 
          this.quotes = response.data
      })
    },
    previousPage: function() {
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes',
        headers: {
            'Authorization': 'Token token="9daa8830e1b3e3a7b44eda726857db04"'
        },
        params: {
          filter: this.inputSearch,
          type: this.inputType,
          page: this.quotes.page - 1
        }
      }).then((response) => { 
          this.quotes = response.data
      })
    },

  },
  computed: {

  },
  beforeMount: function () {
      this.getQuotes()
  }
})