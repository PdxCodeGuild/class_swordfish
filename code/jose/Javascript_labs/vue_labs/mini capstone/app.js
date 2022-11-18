new Vue({
  el: '#app',
  data () {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get('https://api.openbrewerydb.org/breweries')
      .then(response => (this.info = response.data))
      console.log(response)
      // let data = info.data
      // console.log(data)
  }
})