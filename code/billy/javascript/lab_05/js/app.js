Vue.component('test-component',{
  data: function() {
    return {
    }
  },
  props: ['variableInProps'],
  template:`
  <p>{{ variableInProps.quote.body}}<br><br>
  -{{ variableInProps.quote.author }}</p>
  `
})

const vm = new Vue({
  el: '#app',
  data: {
    randomQuote: {},
    inputType: '', //We want this to allow the user to choose author, keyword or tag.
    inputTerm: '', //What the user types in.
    
    currentType: '',
    currentTerm: '', //What the user last used

    newParamter: '',
    responseData: {},
  },
  methods: {
    getRandomQuote: function() {
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/qotd',
      }).then((response) => { 
        this.randomQuote = response.data
      })
    },
    getQuotes: function() {
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes',
        headers: {
          'Authorization': 'Token token="9eb8fe5d65bc94d9d25212fa234b6455", Content-Type: application/json'
        },
      }).then((response) => { 
        this.responseData = response.data
      })
    },
    searchQuotes: function(){
      this.currentTerm = this.inputTerm
      this.currentType = this.inputType
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes',
        headers: {
          'Authorization': 'Token token="9eb8fe5d65bc94d9d25212fa234b6455", Content-Type: application/json'
        },
        params: {
          filter: this.currentTerm,
          type: this.currentType,
        }
      }).then((response) => { 
        this.responseData = response.data
      })
    },
    nextPage: function() {
      console.log('trying to get the next page')
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes',
        headers: {
          'Authorization': 'Token token="9eb8fe5d65bc94d9d25212fa234b6455", Content-Type: application/json'
        },
        params: {
          filter: this.currentTerm,
          type: this.currentType,
          page: this.responseData.page + 1
        }
      }).then((response) => { 
      this.responseData = response.data
      })
    },
    previousPage: function() {
      console.log('trying to get the previous page')
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes',
        headers: {
          'Authorization': 'Token token="9eb8fe5d65bc94d9d25212fa234b6455", Content-Type: application/json'
        },
        params: {
          filter: this.currentTerm,
          type: this.currentType,
          page: this.responseData.page - 1
        }
      }).then((response) => {
      this.responseData = response.data
      })
    },
  },
  computed: {
  },
  beforeMount: function() {
    this.getRandomQuote()
    this.getQuotes()
  }
})