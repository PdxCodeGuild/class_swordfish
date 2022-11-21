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
    keywordSearch: "",
    authorSearch: "",
    tagSearch: "",
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
    getQuotesKeyword: function() {
      axios({
          method: "GET",
          url: "https://favqs.com/api/quotes/",
          headers: {
              'Authorization': 'Token token="9daa8830e1b3e3a7b44eda726857db04"'
          },
          params: {
            filter: this.keywordSearch,
            type: 'keyword'
          }
      }).then((response) => {
          this.quotes = response.data
      }) 
    },
    getQuotesAuthor: function() {
      axios({
          method: "GET",
          url: "https://favqs.com/api/quotes/",
          headers: {
              'Authorization': 'Token token="9daa8830e1b3e3a7b44eda726857db04"'
          },
          params: {
            filter: this.authorSearch,
            type: 'author'
          }
      }).then((response) => {
          this.quotes = response.data
      }) 
    },
    getQuotesTag: function() {
      axios({
          method: "GET",
          url: "https://favqs.com/api/quotes/",
          headers: {
              'Authorization': 'Token token="9daa8830e1b3e3a7b44eda726857db04"'
          },
          params: {
            filter: this.tagSearch,
            type: 'tag'
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
          page: this.quotes.page + 1
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