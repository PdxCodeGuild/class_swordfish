const vm = new Vue({
	el: '#app',
	data: {
        message: 'Vue Connected',
		quotes: {},

	},
	methods:{
        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => 
				// console.log(response.data))
                this.quotes = response.data)

         },
	},
	computed:{

	},	
	created: function() {
        this.loadQuotes()
    }
})


// Your app must use Vue to fetch data and interact with the results.
// Let the user enter a search term and select whether to search by keyword, author, or tag.
// Implement pagination buttons when the search returns more than 25 quotes.
// When the page first loads, show the user a set of completely random quotes.
// You must have at least one Vue component in your app.