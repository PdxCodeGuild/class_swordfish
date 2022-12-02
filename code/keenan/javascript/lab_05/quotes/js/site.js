Vue.component('quote-component', {
    template: `
    <div>
        <ul>
            <li v-for="quote in quotes">{{quote.body}} By: {{quote.author}}<hr></li>
        </ul>
    </div>
    `,
    props: ['quotes'],
})
// can use a header with the searchTerm as a prop for the header in the template

const vm = new Vue({
	el: '#app',
	data: {
		quotes: [],
        searchTerm: '',
        page: '',
        api_response: [],
	},
	methods:{
        loadQuotes: function() {
            axios({
                method: 'GET',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
            }).then(response => {
                this.quotes = response.data.quotes
                this.api_response = response.data
                console.log(response.data)
                console.log('data then data.quotes')
                console.log(response.data.quotes)
            })
         },
         searchKey: function() {
            axios({
                methods: 'GET',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
                params: {
                    filter: this.searchTerm
                }
            }).then((response) => {
                this.quotes = response.data.quotes
                // console.log(response.data)
            })
         },
         searchAuthor: function() {
            axios({
                methods: 'GET',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
                params: {
                    type: 'author',
                    filter: this.searchTerm
                }
            }).then((response) => {
                this.quotes = response.data.quotes
            })
         },
         searchTag: function() {
            axios({
                methods: 'GET',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
                params: {
                    type: 'tag',
                    filter: this.searchTerm
                }
            }).then((response) => {
                this.quotes = response.data.quotes
                // console.log(response.data)
            })
         },
         nextPage: function() {
            // cycle through pages of random quotes
            if (searchTerm == '') {
                this.api_response.page ++
                this.loadQuotes
            }
            // else if (  ) basically an else if for each search parameter type, like no search term, filter/searchterm exists but 
            // type === author, and type ===tag
         }
	},
	computed:{

	},	
	beforeMount: function() {
        this.loadQuotes()
    }
})


// Your app must use Vue to fetch data and interact with the results.
// Let the user enter a search term and select whether to search by keyword, author, or tag.
// Implement pagination buttons when the search returns more than 25 quotes.
// When the page first loads, show the user a set of completely random quotes.
// You must have at least one Vue component in your app.