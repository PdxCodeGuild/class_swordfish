const vm = new Vue({
    el: '#app',
    data: {
        inputName: '',
        inputType: '',

        currentName: '',
        currentType: '',

        responseData: {},

        description: '',
        name: '',
        location: '',

        searchTerm: '',

    },
    methods: {
        getAllData: function() {
            axios({
                method: 'GET',
                url: 'https://botw-compendium.herokuapp.com/api/v2/all',
                // url: 'https://botw-compendium.herokuapp.com/api/v2/entry/',
                params: {
                    // filter: this.currentType,
                    // term: this.currentName,
                    term: this.searchTerm,
                }
        }).then((response)=> {
        this.responseData = response.data
        for(let i = 0; i < 36; i++){
            console.log(i)
            console.log(this.description = response.data.data.creatures.food[i].name)
        }
        // console.log(this.description)
        })
    },
},
    computed: {
    },
    beforeMount: function() {
        this.getAllData()
        console.log(this.getAllData)
    }
})