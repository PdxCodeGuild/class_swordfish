new Vue({
  el: '#app',
  data () {
    return {
      info: null,
      user_input:'',
      attributes: null

    }
  },
  mounted () {
    axios
      .get('https://api.openbrewerydb.org/breweries')
      .then(response => (this.info = response.data))
      // console.log(response.data)
      // let data = info.data
      // console.log(data)
  },
  methods:{
    submit: function(){
      let user_input = document.getElementById('user_input')
      let userinput = user_input.value
      let attribute = document.getElementById('select_attribute')
      let attributes = attribute.value
      if (attributes = 'City'){
        axios.get('https://api.openbrewerydb.org/breweries?by_city='+userinput+'&per_page=50')
        .then(response => {this.info = response.data})
        console.log(userinput)
        console.log(this.info)
      }
        else if (attributes = 'Name'){
          axios.get('https://api.openbrewerydb.org/breweries?by_name='+userinput+'&per_page=50')
          .then(response=> {this.info = response.data})
          console.log(this.info)
      }
        else if (attributes = 'Type'){
          axios.get('https://api.openbrewerydb.org/breweries?by_type='+userinput+'&per_page=50')
          .then(response=> {this.info = response.data})
          console.log(this.info)
      }
      // console.log(response.data)


    }

  }
})
// let user_input = document.getElementById('user_input')
// let attribute = document.getElementById('select_attribute')



