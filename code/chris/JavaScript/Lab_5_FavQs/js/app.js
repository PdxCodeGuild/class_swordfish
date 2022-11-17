Vue.component('quote-block', {
    data: function() {
        return {

        }
    },
    props: ['quote'],
    template: 
    `<div>
        <ul>
            <li>{{quote.body}} -- {{quote.author}}</li>
        </ul>
    </div>`
})

const favQ = new Vue ({
    el: "#favQapp",
    data: {
        randomQuotes: [],
        search: "",
        keywordQuoteslist: []
    },

    methods: {
        getQuotes: function() {
            this.randomQuotes = []
            this.keywordQuoteslist = []
            // JS for loop
            for (let i=0; i<5; ++i) {
                axios({
                    method: "GET",
                    url: "https://favqs.com/api/qotd",
                    headers: {
                        'Authorization': `Token token="855df50978dc9afd6bf86579913c9f8b"`
                    }
                }).then((response) => { //arrow Function!!!
                    // this.randomQuotes = response.data
                    let singleQuote = response.data.quote
                    this.randomQuotes.push(singleQuote)
                })
            }
        }, 
        keywordQuotes: function() {
            this.randomQuotes = []
            this.keywordQuoteslist = []
                axios({
                    method: "GET",
                    url: "https://favqs.com/api/quotes",
                    params: {
                        filter: this.search,
                        type: 'keyword'
                    },
                    headers: {
                        'Authorization': `Token token="855df50978dc9afd6bf86579913c9f8b"`
                    }
                }).then((response) => { //arrow Function!!!
                    console.log(response) // got 200 message
                    this.keywordQuoteslist = response.data.quotes
                    this.keyword = ""
                })
        },
        nextPage: function() {
     
        },
    },

    computed: {
    
    }, 
    created: function() {
        this.getQuotes()
    }
})