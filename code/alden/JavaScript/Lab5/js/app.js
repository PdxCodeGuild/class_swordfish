Vue.component('quote-content', {
    template:`
    <div :class="className">
        <h3>{{ header }} </h3>
        <ul>
            <li v-for="(quote, i) in quotes">{{ quote.body }}<br> -{{quote.author}}</li>
        </ul>
    </div>
    `,
    props: ["className", "header", 'quotes'],
    methods: {
        
    },
})

new Vue({
    el: '#app',
    data: {
        heading: '',
        newParam: '',
        quotes: [],
        data: [],
        param:{
            page: 1,
            filter: '',
            type: '',
        }
    
    },
    methods: {
        getQuotes: function() {
            axios({
                method: "GET",
                url: "https://favqs.com/api/quotes/",
                headers: {
                    'Authorization': 'Token token="9eb8fe5d65bc94d9d25212fa234b6455"'
                },
                params: this.param
                
            }).then((response) => {
                this.quotes = response.data.quotes
                this.data = response.data
                // console.log(this.data)
            }) 
        },
        getQotd: function() {
            axios({
                method: "GET",
                url: "https://favqs.com/api/quotes/",
                headers: {
                    'Authorization': 'Token token="9eb8fe5d65bc94d9d25212fa234b6455"'
                },
            }).then((response) => {
                this.quotes = response.data.quotes
                this.data = response.data
                // console.log(this.data)
            }) 
        },
        searchKeyword: function(){
            this.param.filter = this.newParam
            this.heading = this.newParam
            this.param.type = ''
            this.newParam =''
            this.getQuotes()
        },
        searchAuthor: function(){
            this.param.filter = this.newParam
            this.param.type = 'author'
            this.heading = this.newParam
            this.newParam =''
            this.getQuotes()
        },
        searchTag: function(){
            this.param.filter = this.newParam
            this.param.type = 'tag'
            this.heading = this.newParam
            this.newParam =''
            this.getQuotes()
        },
        nextPage: function(){
            if (this.param.filter !== ''){
                this.param.page += 1
                this.getQuotes()
            }
            else {
                this.getQotd()
            }
        },
        previousPage: function(){
            if (this.param.filter !== ''){
                this.param.page -= 1
                this.getQuotes()
            }
            else {
                this.getQotd()
            }
        }
    },
    computed: {

    },
    beforeMount: function() {
        this.getQotd()
    }

})