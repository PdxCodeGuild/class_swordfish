import Vue from 'vue';

window.axios = require('axios');

new Vue({
  el: '#app',

  components: {

  },

  mounted: function (){
    axios.get('https://favqs.com/api/quotes')
      .then(response => console.log(response))
  },

  data: {

  }
})