new Vue({
  el: '#app',
  data: {
    quotes: []
  },
  methods: {
    getQuotes: function() {
      axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes',
        headers: {
          'Authorization': 'Token token="9eb8fe5d65bc94d9d25212fa234b6455"'
        },
      }).then((response) => {
        this.quotes = response.data
      })
    }
  },
  computed: {

  },
  created: function(){

  },
  beforeMount: function() {
    this.getQuotes()
  },
  mounted: function(){

  },
})