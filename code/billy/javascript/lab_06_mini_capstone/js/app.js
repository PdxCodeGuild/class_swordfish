const vm = new Vue({
    el: '#app',
    data: {
        inputName: '',
        inputType: '',

        currentName: '',
        currentType: '',

        responseData: {},
    },
    methods: {
        getAllData: function() {
            axios({
                method: 'GET',
                url: 'https://botw-compendium.herokuapp.com/api/v2/all',
                params: {
                    filter: this.currentType,
                    term: this.currentName,
                }
        }).then((response)=> {
        this.responseData = response.data
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