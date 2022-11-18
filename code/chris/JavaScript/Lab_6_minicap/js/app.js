//Vue Component goes before App
Vue.component('city-block', {
    data: function() {
        return {

        }
    },
    props: ['weather'],
    template: 
    `<div>
       <p> {{ weather }} </p>
    </div>`
})

const weatherApp = new Vue ({
    el: "#weatherApp",
    data: {
        token: "3f5c584b1dc94e1ec5e88f43d5d6cc1e",
        inputText: "",
        searchLocation: "",
        locationObject: [],
        weatherObject: {},
    },

    methods: {
        getLocation: function() {
            this.cityName = this.inputText
            this.inputText = ""
                axios({
                    method: "GET",
                    url: "http://api.openweathermap.org/geo/1.0/direct",
                    params: {
                        q: this.searchLocation,
                        appid: this.token
                    },
                }).then((response) => { //arrow Function!!!
                    this.locationObject = response.data
                    console.log(response)
                })
        },
        getWeather: function() {
            axios({
                method: "GET",
                url: "https://api.openweathermap.org/data/2.5/weather",
                params: {
                    lat: this.locationObject[0].lat,
                    lon: this.locationObject[0].lon,
                    appid: this.token
                },
            }).then((response) => { //arrow Function!!!
                this.weatherObject = response.data
                console.log(response)
            })
        }
    },

    computed: {

    },
    // created: function(){

    // },
})