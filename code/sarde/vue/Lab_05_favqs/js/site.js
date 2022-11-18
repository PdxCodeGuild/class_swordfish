// Vue.component('quote-item', {
//     props: ['theMessage'],
//     template: `
//     <div>
//     {{theMessage}}
//     </div>
//     `,

// })

// Vue.component('test-item', {
//     props: ['testProperty'],
//     template: `
//     <div>
//     {{testProperty}}
//     </div>
//     `,
// })

Vue.component('display-quote', {
    props: ['quote'],
    template: `
    <div>
    <h3>{{quote.author}}</h3
    <p>{{quote.body}}</p>
    <p>{{quote.tags}}</p>
    </div>
    `,
})



const vm = new Vue({
    el: '#app',
    data: {
        message: 'Random Quotes',
        quotesList: [],
        keyword: '',
        author: '',
        tag: '',
        responseData: '',
        page: 1,

    },
    methods: {
        // loopTest: function () {
        //     for (let i = 0; i < 5; ++i) {
        //         console.log('i:', i)

        //     }

        // },
        getQotd: function () {
            this.quotesList = []
            //iterate
            for (let i = 0; i < 5; ++i) {
                console.log("get qotd")
                axios({
                    method: 'get',
                    url: 'https://favqs.com/api/qotd'
                }).then((response) => {
                    console.log("response", response.data)
                    //get the quote from the response = theQuote
                    let theQuote = response.data.quote
                    this.quotesList.push(theQuote)
                    console.log(theQuote)
                })
            }
        },
        filterQotd: function () {
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes?filter=${this.keyword}`,
                headers: { 'Authorization': 'Token token=3537013a6e89bef1f6bb12916f4fa4c8' }
            }).then((response) => {
                console.log("response.data", response.data)
                this.responseData = response.data
                this.quotesList = this.responseData.quotes
            })
        },
        selectByAuthor: function () {
            axios({
                method: 'get',
                // https://favqs.com/api/quotes/?filter=Mark+Twain&type=author
                url: `https://favqs.com/api/quotes/?filter=${this.author}&type=author`,
                headers: { 'Authorization': 'Token token=3537013a6e89bef1f6bb12916f4fa4c8' }
            }).then((response) => {
                console.log("response.data", response.data)
                this.responseData = response.data
                this.quotesList = this.responseData.quotes
            })
        },
        selectByTag: function () {
            axios({
                method: 'get',
                // https://favqs.com/api/quotes/?filter=funny&type=tag
                url: `https://favqs.com/api/quotes/?filter=${this.tag}&page=${this.page}&type=tag`,
                headers: { 'Authorization': 'Token token=3537013a6e89bef1f6bb12916f4fa4c8' }
            }).then((response) => {
                console.log("response", response.data)
                this.responseData = response.data
                this.quotesList = this.responseData.quotes
            })

        },
    },
    created: function () {
        console.log("Created")
        this.getQotd()
    }




})

