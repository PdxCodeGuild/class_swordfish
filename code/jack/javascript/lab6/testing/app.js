
axios({
    method: "GET",
    url: "https://jsonplaceholder.typicode.com/users",
}).then((response) => {
    console.log(response.data)
})
