Vue.component('', {
    template:`
    
    `,
    props: [],
    methods: {}
})

let grounder = new Vue({
    el: '#app',
    data: {
        searchText:'',
        params: {},
        data:[],
        ingredients: [],
        measurements: []
    },
    methods: {
        drinkSearch: function(){
            axios({
                method: "GET",
                url: "https://www.thecocktaildb.com/api/json/v1/1/",
                params: this.params
            }).then((response) => {
                this.data = response.data.drinks
            })
        },
        initialDrink: function(){
            axios({
                method: "GET",
                url: "https://www.thecocktaildb.com/api/json/v1/1/random.php",
                params: this.params
            }).then((response) => {
                this.data = response.data.drinks
                this.ingredientList()
                this.measurementList()
                console.log(this.data)
                console.log(this.ingredients)
                console.log(this.measurments)
            })
            
        },
        ingredientList: function(){
            let i=0
            // let ingre = ''
            // let measure = ''
            while (i < this.data.length){
                for (let key in this.data[i]){
                    if (key.includes('Ingredient') && this.data[i][key] !== null){
                        this.ingredients.push(this.data[i][key])}
                    // }else if (key.includes('Measure')){
                    //     measure = this.data[i][key]
                    // }    
                    // this.ingredients.push(ingre + measure)
                }    
                i++
            }
        },
        measurementList: function(){
            let i=0
            while (i < this.data.length){
                for (let key in this.data[i]){
                    if (key.includes('Measure') && this.data[i][key] !== null){
                        this.measurements.push(this.data[i][key])}}
                i++
            }
        }
    },
    computed: {

    },
    beforeMount: function(){
        this.initialDrink()
        console.log(this.ingredients)
    }
})