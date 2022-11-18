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
        theRandomQuotes: [],
        keywordQuoteslist: [],
        tagQuoteslist: [],
        authorQuoteslist: [],
        page: 1,
        inputText: "",
        search: "",
        tags: "",
        author: "",
        currentType: "",
        currentSearch: ""
    },

    methods: {
        getQuotes: function() {
            this.theRandomQuotes = []
            this.keywordQuoteslist = []
            this.authorQuoteslist = []
            this.tagQuoteslist = []
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
                    this.theRandomQuotes.push(singleQuote)
                })
            }
        }, 
        keywordQuotes: function() {
            this.search = this.inputText
            this.inputText = ""
            this.theRandomQuotes = []
            this.keywordQuoteslist = []
            this.page = 1
                axios({
                    method: "GET",
                    url: "https://favqs.com/api/quotes",
                    params: {
                        filter: this.search,
                    },
                    headers: {
                        'Authorization': `Token token="855df50978dc9afd6bf86579913c9f8b"`
                    }
                }).then((response) => { //arrow Function!!!
                    this.keywordQuoteslist = response.data.quotes
                })
        },
        authorQuotes: function() {
            this.currentSearch = this.inputText
            this.currentType = "author"
            this.inputText = ""
            this.theRandomQuotes = []
            this.authorQuoteslist = []
            this.page = 1
                axios({
                    method: "GET",
                    url: "https://favqs.com/api/quotes",
                    params: {
                        type: this.currentType,
                        filter: this.currentSearch
                    },
                    headers: {
                        'Authorization': `Token token="855df50978dc9afd6bf86579913c9f8b"`
                    }
                }).then((response) => { //arrow Function!!!
                    this.authorQuoteslist = response.data.quotes
                    console.log("author data", response.data.quotes)
                })
        },
        taggingQuotes: function() {
            this.currentSearch = this.inputText
            this.currentType = "tag"
            this.inputText = ""
            this.theRandomQuotes = []
            this.tagQuoteslist = []
            this.page = 1
                axios({
                    method: "GET",
                    url: "https://favqs.com/api/quotes",
                    params: {
                        type: this.currentType,
                        filter: this.currentSearch
                    },
                    headers: {
                        'Authorization': `Token token="855df50978dc9afd6bf86579913c9f8b"`
                    }
                }).then((response) => { //arrow Function!!!
                    this.tagQuoteslist = response.data.quotes
                })
        },
        nextPage: function() { 
            this.page++
            this.theRandomQuotes = []
            this.keywordQuoteslist = []
            this.tagQuoteslist = []
            this.authorQuoteslist = []
                axios({
                    method: "GET",
                    url: "https://favqs.com/api/quotes",
                    params: {
                        filter: this.currentSearch,
                        type: this.currentType,
                        page: this.page
                    },
                    headers: {
                        'Authorization': `Token token="855df50978dc9afd6bf86579913c9f8b"`
                    }
                }).then((response) => { //arrow Function!!!
                    if(this.currentType === 'author') {
                        this.authorQuoteslist = response.data.quotes
                    } else if(this.currentType === 'tag') {
                        this.tagQuoteslist = response.data.quotes
                    } else {
                        this.keywordQuoteslist = response.data.quotes
                    }
                    this.page = response.data.page
                })
        },
        
    },
    computed: {
    
    }, 
    created: function() {
        this.getQuotes()
    },
})