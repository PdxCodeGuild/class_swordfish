
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
        searchType: "keyword",
        responseData: {},
        parameters: {},
        searchCheck: false,
    },
    methods: {
        getQuotes: function() {
            axios({
                method: "GET",
                url: "https://favqs.com/api/quotes",
                headers: {Authorization: "Token token=8b2febc277e0f4d1f9a0e395db2eab35",},
                params: this.parameters

            }).then((response) => {
                this.responseData = response.data
                if (this.responseData.quotes[0].body === "No quotes found") {
                    this.responseData.last_page = true
                }
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
            let checkString = this.searchText
            if (this.searchText.replace(/\s+/g, '') != "") { // checks that search input isn't empty or spaces
                this.parameters = {page:1, filter:this.searchText, type:this.searchType}
                this.searchCheck = true
                this.getQuotes()
            }
            
        },
        new25: function() {
            this.getQuotes()
        },
        clearSearch: function() {
            this.parameters = {}
            this.searchCheck = false
            this.searchText = ''
            this.getQuotes()
        }
    },
    computed: {

    },
    beforeMount: function () {
        this.getQuotes()
    }
})