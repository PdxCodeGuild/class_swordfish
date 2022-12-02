// Nasa Image of the Day Capstone
// API Key: S6bU3PcfNm6XpLCA8l4JoLYhYgnRM8ORcGbGFvmG


// You can start using this key to make web service requests. Simply pass your key in the URL when making a web request. Here's an example:
// https://api.nasa.gov/planetary/apod?api_key=S6bU3PcfNm6XpLCA8l4JoLYhYgnRM8ORcGbGFvmG


// API readme and info: https://github.com/nasa/apod-api/blob/master/README.md

const vm = new Vue({
    el: '#app',
    data: {
        nasaresponse: [],
        hdur: '',
        date: '',
        concept_tags: '',
    },
    methods:{
        loadNasa: function() {
            axios({
                method: 'GET',
                url: 'https://api.nasa.gov/planetary/apod?api_key=S6bU3PcfNm6XpLCA8l4JoLYhYgnRM8ORcGbGFvmG',
                params: {
            
                },
            }).then(response => {
                this.nasaresponse = response.data
                console.log(response.data)
            })
        },
    },
    beforeMount: function() {
        this.loadNasa()
    }
})
