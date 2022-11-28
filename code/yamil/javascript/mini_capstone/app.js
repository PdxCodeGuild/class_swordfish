// python -m http.server

const eventSearchApi = new Vue({
    el: "#app",
    data: {
      searchElementView: false,
      bannerElementView: true,
      eventsList: [],
      keyword: "",
      city: "",                
      country: "",         
      state: "",               
      genre: "",               
      selected: "state-option",
      selectedText: "",
      selection: "keyword-option",
      cityMod: "&city=",
      keywordMod: "&keyword=",
      countryMod: "&countryCode=",
      stateMod: "&stateCode=",
      genreMod: "&classificationName=",
    },
    computed: {

    },
    methods: {
        eventSearch: function() {
          if (this.selected === "city-option") {
            this.city = this.selectedText
          }
          else if (this.selected === "state-option") {
            this.state = this.selectedText
          }
          else if (this.selected === "country-option") {
            this.country = this.selectedText
          }
            this.searchElementView = true
            this.bannerElementView =  false
            axios({
              method: "GET",
              url: `https://app.ticketmaster.com/discovery/v2/events.json?apikey=pFu9Kj7Vv81m3dt87AVF3GK79yGaJKBy`
              +`${this.keywordMod+this.keyword}${this.cityMod+this.city}${this.genreMod+this.genre}${this.countryMod+this.country}
              ${this.stateMod+this.state}${this.postalCodeMod+this.postalCode}`
            }).then((response) => {
              this.eventsList = response.data._embedded.events
              this.keyword = ""
              this.genre = ""
            })
        }
    },
})

