
Vue.component('quote-card', {
    data: function() {
        return {
        }
    },
    props: ['quote'],
    template: `
    <div class='quote-card'>
    <h4>{{quote.body}}</h4>
    <p><em>-{{quote.author}}</em></p>
    </div>
    `,
})

let vm = new Vue({
    el: "#app",
    data: {
        searchText: "",
        searchType: null,
        responseData: {},
        parameters: {},
    },
    methods: {
        getQuotes: function() {
            console.log(this.parameters)
            axios({
                method: "GET",
                url: "https://favqs.com/api/quotes",
                headers: {Authorization: "Token token=8b2febc277e0f4d1f9a0e395db2eab35",},
                params: this.parameters

            }).then((response) => {
                this.responseData = response.data
            })
        },
        nextPage: function() {
            this.parameters.page ++
            this.getQuotes()
        },
        previousPage: function() {
            this.parameters.page --
            this.getQuotes()
        },
        searchQuotes: function() {
            this.parameters = {page:1, filter:this.searchText, type:this.searchType}
            this.getQuotes()
        },
        new25: function() {
            this.getQuotes()
        },
        clearSearch: function() {
            this.parameters = {}
            this.getQuotes()
        }
    },
    computed: {

    },
    beforeMount: function () {
        this.getQuotes()
    }
})