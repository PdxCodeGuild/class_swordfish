<template>
    <div>
        <i>"{{ quotes }}"</i>
    </div>
</template>




<script>
import axios from 'axios'
import { ref } from 'vue'

export default {
    setup () {

    const quotes = ref('')

        axios.get('https://favqs.com/api/quotes')
            .then(response =>{
                quotes.value = response
            })
            return {
                quotes
            }
    }
}
</script>
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>