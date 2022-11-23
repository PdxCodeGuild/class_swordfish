
Vue.component('pet-card', {
  data: function() {
    return {

    }
  },
  props: ['pet'],
  template: `
  <div>
  <h3>{{pet.name}}</h3>
  <p>{{pet.type}} -- {{pet.age}}</p>
  <slot></slot>
  <button @click="speak">Speak</button>
  </div>
  `,
  methods: {
    speak: function() {
      this.$emit('shout', this.pet.type)
    }
  }
})

const app = new Vue({
  el: "#app",
  data: {
    numOfTimesSpoken: 0,
    pets: [
      { name: "Rain", type: "dog", age: 1},
      { name: "Cloud", type: "dog", age: 4},
      { name: "Bunbun", type: "cat", age: 14},
      { name: "Magnus", type: "cat", age: 2},
      { name: "Fresvik", type: "cat", age: 3},
      { name: "Moxie", type: "cat", age: 3},
      { name: "Gary", type: "snail", age: 1},
      { name: "Howl", type: "cat", age: 8},
    ]
  },
  methods: {
    kaw: function(type) {
      alert('I am a... ' + type)
      this.numOfTimesSpoken++
    }
  }
})