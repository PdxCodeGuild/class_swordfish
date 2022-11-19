// python -m http.server

const eventSearchApi = new Vue({
    el: "#app",
    data: {
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
    },
    computed: {

    },
    methods: {
        eventSearch: function() {
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



