// python -m http.server

const quotesApiVue = new Vue({
  el: '#app',
  data: {
    newSearch: "",
    quotes: [],
    searchParameter: "",
    searchType: ""
  },
  computed: {
  
  },
  methods: {
    nextPage: function() {
      this.page++
      console.log(this.page)
      if (this.searchType === "author") {
        this.authorSearch()
      } else if (this.searchType === "tag") {
        this.tagSearch()
      } else if (this.searchType === "keyword") {
        this.keywordSearch()
      } else {
        console.log("Error")
      }
    },
    previousPage: function() {
      this.page = this.page - 1
      if (this.searchType === "author") {
        this.authorSearch()
      } else if (this.searchType === "tag") {
        this.tagSearch()
      } else if (this.searchType === "keyword") {
        this.keywordSearch()
      } else {
        console.log("Error")
      }
    },
// ----------------------------------------------------------------------------------------------------
    authorSearch: function() {
      this.searchType = "author"
      author = `?filter=${this.newSearch}&type=author`,
      axios({
        method: "GET",
        url: `https://favqs.com/api/quotes/`+`${author}`+`&page=${this.page}`,
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
      this.searchType = "tag"
      tag = `?filter=${this.newSearch}&type=tag`,
      axios({
        method: "GET",
        url: `https://favqs.com/api/quotes/`+`${tag}`+`&page=${this.page}`,
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
      this.searchType = "keyword"
      keyword = `?filter=${this.newSearch}`,
      axios({
        method: "GET",
        url: `https://favqs.com/api/quotes/`+`${keyword}`+`&page=${this.page}`,
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