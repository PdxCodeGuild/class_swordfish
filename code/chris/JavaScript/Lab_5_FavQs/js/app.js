const favQ = new Vue ({
    el: "#favQapp",
    data: {
        randomQuotes: []
    },

    methods: {
        getQuotes: function() {
            this.randomQuotes = []
            axios({
                method: "GET",
                url: "https://favqs.com/api/qotd",
                headers: {
                    'Authorization': `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(function() {}
            
            })
        }
    },

    computed: {

    }, 
})