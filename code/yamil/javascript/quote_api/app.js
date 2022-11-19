// python -m http.server

const quotesApiVue = new Vue({
  el: '#app',
  data: {
    newSearch: "",
    quotes: [],
    searchParameter: ""
  },
  computed: {
  
  },
  methods: {
    // searchParameterFunction: function() {
    //   if (this.searchParameter === "keyword") {
    //     this.keywordSearch()
    //   }
    //   else if (this.searchParameter === "author") {
    //     this.authorSearch()
    //   }
    //   else if (this.searchParameter === "tag") {
    //     this.tagSearch()
    //   }
    // },
    nextPage: function() {
      this.page++
      author = `?filter=${this.newSearch}&type=author${this.page}`,
      keyword = `?filter=${this.newSearch}`,
      tag = `?filter=${this.newSearch}&type=tag`,
      axios({
        method: "GET",
        url: `https://favqs.com/api/quotes/`+`${author}`,
        headers: {
        'Authorization': `Token token="3b3e469abc960df09cbcc8ab225ea0f0"`
        }
      }).then((response) => {
        this.quotes = response.data
        this.page = response.data.page
      })
      // this.newSearch = ""
    },
    previousPage: function() {
      this.page = this.page - 1
      author = `?filter=${this.newSearch}&type=author${this.page}`,
      keyword = `?filter=${this.newSearch}`,
      tag = `?filter=${this.newSearch}&type=tag`,
      axios({
        method: "GET",
        url: `https://favqs.com/api/quotes/`+`${author}`,
        headers: {
        'Authorization': `Token token="3b3e469abc960df09cbcc8ab225ea0f0"`
        }
      }).then((response) => {
        this.quotes = response.data
        this.page = response.data.page
      })
      // this.newSearch = ""
    },
// ----------------------------------------------------------------------------------------------------
    authorSearch: function() {
      console.log(this.quotes.page, "quotes.page")
      console.log(this.quotes.last_page, "last page")
      author = `?filter=${this.newSearch}&type=author`,
      axios({
        method: "GET",
        url: `https://favqs.com/api/quotes/`+`${author}`,
        headers: {
        'Authorization': `Token token="3b3e469abc960df09cbcc8ab225ea0f0"`
        }
      }).then((response) => {
        this.quotes = response.data
        this.page = response.data.page
      })
      // this.newSearch = ""
    },

    tagSearch: function() {
      tag = `?filter=${this.newSearch}&type=tag`,
      axios({
        method: "GET",
        url: `https://favqs.com/api/quotes/`+`${tag}`,
        headers: {
        'Authorization': `Token token="3b3e469abc960df09cbcc8ab225ea0f0"`
        }
      }).then((response) => {
        this.quotes = response.data
        this.page = response.data.page
      })
      // this.newSearch = ""
    },

    keywordSearch: function() {
      keyword = `?filter=${this.newSearch}`,
      axios({
        method: "GET",
        url: `https://favqs.com/api/quotes/`+`${keyword}`,
        headers: {
        'Authorization': `Token token="3b3e469abc960df09cbcc8ab225ea0f0"`
        }
      }).then((response) => {
        this.quotes = response.data
        this.page = response.data.page
      })
      // this.newSearch = ""
    },

    getQuotes: function() {
      axios({
        method: "GET",
        url: "https://favqs.com/api/quotes/",
        headers: {
        'Authorization': `Token token="3b3e469abc960df09cbcc8ab225ea0f0"`
        }
      }).then((response) => {
        this.quotes = response.data
        this.page = response.data.page
      })
    }
  },
  beforeMount: function() {
    this.getQuotes()
  }
})