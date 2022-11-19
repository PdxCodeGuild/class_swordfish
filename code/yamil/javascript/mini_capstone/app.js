// python -m http.server

const eventSearchApi = new Vue({
    el: "#app",
    data: {
      searchElementView: false,
      eventsList: [],
      keyword: "",
      city: "",                
      country: "",             
      postalCode: "",          
      state: "",               
      genre: "",               
      selected: "",
      selectedText: "",
      cityMod: "&city=",
      keywordMod: "&keyword=",
      countryMod: "&countryCode=",
      postalCodeMod: "&postalCode=",
      stateMod: "&stateCode=",
      genreMod: "&classificationName=",
      testDict: {
        "city" : function() {
          this.city = this.selectedText
        }
       }
    },
    computed: {

    },
    methods: {
        eventSearch: function() {
          if (this.selected === "zip-code-option") {
            this.postalCode = this.selectedText
          }
          else if (this.selected === "city-option") {
            this.city = this.selectedText
          }
          else if (this.selected === "state-option") {
            this.state = this.selectedText
          }
          else if (this.selected === "country-option") {
            this.country = this.selectedText
          }
            this.searchElementView = true
            axios({
              method: "GET",
              url: `https://app.ticketmaster.com/discovery/v2/events.json?apikey=pFu9Kj7Vv81m3dt87AVF3GK79yGaJKBy&size=5`
              +`${this.keywordMod+this.keyword}${this.cityMod+this.city}${this.genreMod+this.genre}${this.countryMod+this.country}
              ${this.stateMod+this.state}${this.postalCodeMod+this.postalCode}`
            }).then((response) => {
              this.eventsList = response.data._embedded.events
            })
        }
    },
    // beforeMount: function() {
    //   this.eventSearch()
    // }
})

