
var app = new Vue({
  el: '#app',
  data: {
    photoInfo: {},
    randomPhotoInfo: {},
    imageGalleryInfo: {},
    searchDate: '',
  },
  methods: {
    getPhoto: function() {
      axios({
          method: "GET",
          url: 'https://api.nasa.gov/planetary/apod?api_key=wTsEGeI7sDZUbINg9RJiPLHEXgOh8bM0FsGlkbrL', 
          params: {
            date: this.searchDate 
          }          
      }).then((response) => {
          this.photoInfo = response.data
      }) 
    },
    getRandomPhoto: function() {
      axios({
          method: "GET",
          url: 'https://api.nasa.gov/planetary/apod?api_key=wTsEGeI7sDZUbINg9RJiPLHEXgOh8bM0FsGlkbrL', 
          params: {
            count: 1
          }          
      }).then((response) => {
          this.randomPhotoInfo = response.data
          this.photoInfo = this.randomPhotoInfo[0]
      }) 
    },
    imageGallery: function() {
      axios({
        method: "GET",
        url: 'https://api.nasa.gov/planetary/apod?api_key=wTsEGeI7sDZUbINg9RJiPLHEXgOh8bM0FsGlkbrL', 
        params: {
          count: 25
        } 
      }).then((response) => {
        this.imageGalleryInfo = response.data
      })
    }
  },
  computed: {

  },
  beforeMount: function () {
      this.getPhoto()
      this.imageGallery()
  }
})
