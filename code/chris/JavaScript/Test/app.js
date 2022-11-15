// Start server:
// python -m http.server 8000

Vue.component('the-lone-element', {
    template: `
    <s>
    BIG STRING in Vue.component('the-lone-element', {template})!!!
    </s>
    `
})

const app1 = new Vue({
    el: '#app1'
})