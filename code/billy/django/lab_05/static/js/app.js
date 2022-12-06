const vm = new Vue({
    el: '#app',
    delimiters: ['[[',']]'],
    data: {
        // .this when calling attributes and methods
        pokemons: '',
        hardCodedString: 'goodbye fellow humans',
        urlEndPoint: '/apis/v1/pokemon/',
        csrf_token: '',
        pokemon: '',
        testPokemonId: 200,
        hardCodedPokemon: {
            "number": 239,
            "name": "ivysaur",
            "height": 1.0,
            "weight": 13.0,
            "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png",
            "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/2.png",
        },

    },
    methods: {
        getPokemonInfo: function() {
            this.clearSinglePokemon()
            axios({
                method: 'GET',
                url: this.urlEndPoint,
            }).then(response => {
                this.pokemons = response.data
                console.log(this.pokemons)
            }).catch(error => {
                console.log(error.response),
                console.log(error.response.data)
            })
        },
        getSinglePokemonInfo: function(id) {
            if (id===''){
                id = this.testPokemonId
            } else {
                this.clearPokemons()
                axios({
                    method: 'GET',
                    url: this.urlEndPoint + id // id is a local variable to this function.
                }).then(response => {
                    this.pokemon = response.data
                    console.log(this.pokemon)
                }).catch(error => {
                    console.log(error.response),
                    console.log(error.response.data)
                })
            }
        },
        createPokemon: function() {
            axios({
                method: 'POST',
                url: this.urlEndPoint,
                data: this.hardCodedPokemon,
                headers: {
                    'X-CSRFToken': this.csrf_token,
                },
            }).then(response => {
                console.log(response.data)
            }).catch(error => {
                console.log(error.response),
                console.log(error.response.data)
            })
        },
        clearPokemons: function() {
            this.pokemons = ''
        },
        clearSinglePokemon: function() {
            this.pokemon = ''
        }
    },
    mounted: function() {
        console.log("Mounted")
        this.csrf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value
    },
})