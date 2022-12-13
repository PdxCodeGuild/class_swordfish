const flightSearchApi = new Vue({
    el: "#app",
    data: {
      flightsList: [],
      test: "",
      test2: "",
    },
    computed: {

    },
    methods: {
        flightSearch: function() {
            axios({
              method: "GET",
              headers: {
                authorization : {
                  client_id: 'qVGXBGiJqYwbLAQnxPi4QDxljsqVjdXu',
                  client_secret: 'TFf9hWYPhqgVEmBG',
                }
              },
              params: {
                originLocationCode:'MIA',
                destinationLocationCode:'BRU',
                departureDate:'2023-07-19',
                returnDate:'2023-07-26',
                adults:1,
              },
              url: `https://test.api.amadeus.com/v2`
            }).then((response) => {
              this.flightsList = response.data
            })
        }
    },
})