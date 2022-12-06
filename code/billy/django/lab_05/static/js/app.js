const vm = new Vue({
    el: '#app',
    delimiters: ['[[',']]'],
    data: {
        // .this when calling attributes and methods
        pokemons: '',
        urlEndPoint: '/apis/v1/pokemon/',
        csrf_token: '',
        pokemon: '',
        editPokemonMode: false,
        newPokemon: {
            number: '',
            name: '',
            height: '',
            weight: '',
            image_front: '',
            image_back: '',
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
                }).catch(error => {
                    console.log(error.response),
                    console.log(error.response.data)
                })
            }
        },
        updatePokemon: function() {
            axios({
                method: 'PUT',
                url: this.urlEndPoint + this.pokemon.id + '/',
                headers: {
                    'X-CSRFToken': this.csrf_token,
                },
                data: this.pokemon
            }).then(response => {
                this.pokemon = response.data
                console.log('updating',this.pokemon)
            }).catch(error => {
                console.log(error.response),
                console.log(error.response.data)
            })
        },
        deletePokemon: function(id) {
            axios({
                method: 'DELETE',
                url: this.urlEndPoint + id + '/',
                headers: {
                    'X-CSRFToken': this.csrf_token,
                },
                data: this.pokemon
            }).then(response => {
                this.pokemon = response.data
                console.log('deleting', this.pokemon)
                this.getPokemonInfo()
            }).catch(error => {
                console.log(error.response),
                console.log(error.response.data)
            })
        },
        createPokemon: function() {
            axios({
                method: 'POST',
                url: this.urlEndPoint,
                data: this.newPokemon,
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
    created: function() {
        this.getPokemonInfo()
    }
})