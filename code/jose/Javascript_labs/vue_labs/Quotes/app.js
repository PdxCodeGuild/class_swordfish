new Vue({
    el: "#app",
    data: {
      quotes: []
    },
    methods: {
      getQuotes: function() {
        axios({
          method: "GET",
          url: "https://favqs.com/api/"
        }).then((response) => {
          this.quotes = response.data
        })
      }},
    })  