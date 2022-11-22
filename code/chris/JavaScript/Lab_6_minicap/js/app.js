//Vue Component goes before App
Vue.component('city-block', {
    data: function() {
        return {

        }
    },
    props: ['weather'],
    template: 
    `<div>
       <h4>{{ weather.name }} real-time weather is: {{ weather.main.temp.toFixed(0) }}F</h4>
       <h4>It feels like:  {{ weather.main.feels_like.toFixed(0) }}F</h4>
       <p>{{ weather.name }} Weather Description: {{ weather.weather[0].description }}</p>
    </div>`
})

Vue.component('forecast-block', {
    data: function() {
        return {

        }
    },
    props: ['forecast'],
    template: 
    `<div>
       <ul>
            <li>{{ forecast.dt_txt }} -- {{ forecast.main.temp.toFixed(0) }}F</li>
       </ul>
    </div>`
})

const weatherApp = new Vue ({
    el: "#weatherApp",
    data: {
        home: url = "http://127.0.0.1:5500/code/chris/JavaScript/Lab_6_minicap/index.html",
        token: "3f5c584b1dc94e1ec5e88f43d5d6cc1e",
        imperial: "imperial",
        inputText: "",
        searchLocation: "",
        timeLimit: 9,
        locationObject: [],
        weatherObject: {},
        forecastObject: [],
    },

    methods: {
        getLocation: function() {
            this.searchLocation = this.inputText
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
                    this.getWeather()
                    console.log(response)
                    this.page = response.data.page
                    this.forecastObject = []
                })
        },
        getWeather: function() {
            axios({
                method: "GET",
                url: "https://api.openweathermap.org/data/2.5/weather",
                params: {
                    lat: this.locationObject[0].lat,
                    lon: this.locationObject[0].lon,
                    units: this.imperial,
                    appid: this.token
                },
            }).then((response) => { //arrow Function!!!
                this.weatherObject = response.data
                console.log(Object.keys(this.weatherObject))
                console.log(response)
            })
        },
        getForecastLocation: function() {
            this.searchLocation = this.inputText
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
                    this.getForecast()
                    console.log('Forecast Location', response)
                    this.page = response.data.page
                    this.weatherObject = {}
                })
        },
        getForecast: function() {
            axios({
                method: "GET",
                url: "https://api.openweathermap.org/data/2.5/forecast",
                params: {
                    lat: this.locationObject[0].lat,
                    lon: this.locationObject[0].lon,
                    units: this.imperial,
                    cnt: this.timeLimit,
                    appid: this.token
                },
            }).then((response) => { //arrow Function!!!
                this.forecastObject = response.data
                console.log('Forecast', response)
            })
        }
    },

    computed: {

    },
    // created: function(){

    // },
})