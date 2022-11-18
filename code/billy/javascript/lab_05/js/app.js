const vm = new Vue({
  el: '#app',
  data: {
    inputType: '', //We want this to allow the user to choose author, keyword or tag.
    inputTerm: '', //What the user types in.
    
    currentType: '',
    currentTerm: '', //What the user last used.

    currentPage: 1,

    newParamter: '',
    responseData: {},
  },
  methods: {
    getQuotes: function() {
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes',
        headers: {
          'Authorization': 'Token token="9eb8fe5d65bc94d9d25212fa234b6455", Content-Type: application/json'
        },

      }).then((response) => { 
        console.log('response', response)
        this.responseData = response.data

      })
    },
    searchQuotes: function(){
      this.currentTerm = this.inputTerm
      this.currentType = this.inputType
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes/?filter=""&type=""',
        headers: {
          'Authorization': 'Token token="9eb8fe5d65bc94d9d25212fa234b6455", Content-Type: application/json'
        },
        params: {
          filter: this.currentTerm,
          type: this.currentType,
        }

      }).then((response) => { 
        console.log('response', response)
        this.responseData = response.data
      })
    },
    nextPage: function() {
      console.log('trying to get the next page')
     
    }
  },

  computed: {

  },
  beforeMount: function() {
    this.getQuotes()
  }

  
})

//this is the path to 'this.responseData.last_page'