// Vue.component('', {
//     template:`
    
//     `,
//     props: [],
//     methods: {}
// })

let grounder = new Vue({
    el: '#app',
    data: {
        searchText:'',
        searchingBy: 's',
        params: {},
        data:[],
        // ingredients: [],
        // measurements: []
    },
    methods: {
        drinkSearch: function(){
            if (this.searchingBy === 's'){
                urlOptions = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
            } else if (this.searchingBy === 'i') {
                urlOptions = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
            }
            axios({
                method: "GET",
                url: urlOptions,
                params: this.params
            }).then((response) => {
                this.data = response.data.drinks
                console.log(this.data)
                this.ingredientsAndMeasurements()
                
            })
        },
        initialDrink: function(){
            axios({
                method: "GET",
                url: "https://www.thecocktaildb.com/api/json/v1/1/random.php",
                params: this.params
            }).then((response) => {
                this.data = response.data.drinks
                this.ingredientsAndMeasurements()
                // console.log(this.data)
                // console.log(this.ingredients)
                // console.log(this.measurments)
            })
        },
        randomDrink: function(){
            axios({
                method: "GET",
                url: "https://www.thecocktaildb.com/api/json/v1/1/random.php",
            }).then((response) => {
                this.data = response.data.drinks
                this.ingredientsAndMeasurements()
            })
        },
        naDrink: function(){
            axios({
                method: "GET",
                url: "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic",
                params: this.params
            }).then((response) => {
                this.data = response.data.drinks
                this.ingredientsAndMeasurements()
                console.log(this.data)
            })
        },
        searchDrinks: function(){
            this.params[this.searchingBy]= this.searchText
            this.drinkSearch()
            // this.ingredientList()
            // this.measurementList()
            this.params = {}
            this.searchText = ''
        },
        ingredientsAndMeasurements: function(){             // Loop through each drink, saves the ingredient and measurements, and appends it as an array on to the drink data.
            let i=0
                while (i < this.data.length){                                   
                    this.data[i].ingredients=this.ingredientList(this.data[i]) 
                    this.data[i].measurements=this.measurementList(this.data[i])
                    i++
                }
        },
        ingredientList: function(drink){
            let ingredients =[]
                for (let key in drink){
                    if (key.includes('Ingredient') && drink[key] !== null){
                        ingredients.push(drink[key])}
            }
            return ingredients
        },
        measurementList: function(drink){
            let measurements = []
                for (let key in drink){
                    if (key.includes('Measure') && drink[key] !== null){
                        measurements.push(drink[key])}}
            return measurements
        }
    },
    computed: {

    },
    beforeMount: function(){
        this.initialDrink()
        console.log(this.ingredients)
    }
})