const vm = new Vue({
    el: '#app',
    data: {
        responseData: {},

        searchTerm: '',
    },
    methods: {
        getGameInformation: function() {
            axios({
                method: 'GET',
                url: `https://botw-compendium.herokuapp.com/api/v2/entry/${this.searchTerm}`,
        }).then((response)=> {
            this.responseData = response.data
            console.log(this.responseData)
        }
    )},
},
})