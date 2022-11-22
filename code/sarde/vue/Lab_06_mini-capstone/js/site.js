
const vm = new Vue({
    el: '#app',
    data: {
        message: 'Yo Momma Jokes',
        jokesList: [],
        keyword: '',
        results: '',
    },
    methods: {
        getJoke: function () {
            axios({
                method: 'get',
                url: 'https:yomamma-api.herokuapp.com/jokes',
            }).then((response) => {
                console.log("response", response)
            })
        },

        getJokesList: function () {
            let count = 5
            axios({
                method: 'get',
                url: `https:yomamma-api.herokuapp.com/jokes?count=${count}`,
            }).then((response) => {
                console.log("response", response.data)
                this.jokesList = response.data
                console.log('List of jokes', this.jokesList)

            })
        },

        searchJokes: function () {
            axios({
                method: 'get',
                url: `https:yomamma-api.herokuapp.com/search?query=${this.keyword}`,
            }).then((response) => {
                console.log("response.data", response.data)
                this.results = response.data.results
                console.log('Search Results', this.results)
            })
        },




    },


    created: function () {
        console.log("Created")
        this.getJoke()
        this.getJokesList()
        this.searchJokes()
    },





})