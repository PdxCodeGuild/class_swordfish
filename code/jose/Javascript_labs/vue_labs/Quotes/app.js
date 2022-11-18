// new Vue({
//     el: "#app",
//     data: {
//         result: "",
//         responseAvailable: false,
//         apiKey: '34803f76fbb9908169a9377a0111f0cb'
//     },
//     })  
    // Send a POST request
    // let req = new XMLHttpRequest();
    // req.addEventListener("progress", function(e) {
    //     console.log(e.loaded);
    // });
    // req.addEventListener("error", function(e) {
    //     console.log(e.status);
    // });
    // req.addEventListener("load", function(e) {
    //     console.log(req.responseText);
    //     let responsetext = response.quotes
    //     console.log(responsetext)
    // });
    // req.open("GET", "https://favqs.com/api/");
    // req.setRequestHeader("Authorization", 'Token token="34803f76fbb9908169a9377a0111f0cb"');
    // req.send()

let target = document.getElementById("target");
let getQuoteButton = document.getElementById("quote-button");

getQuoteButton.addEventListener("click", function(e) {
    let req = new XMLHttpRequest();
    req.addEventListener("progress", function(e) {
        console.log(e.loaded);
        target.innerText = "Loading...";
    });
    req.addEventListener("error", function(e) {
        console.log(e.status);
        target.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function(e) {
        console.log(req.responseText);
        let response = JSON.parse(req.responseText);
        console.log(response);
        let resultHTML = `
            <p>${response.quotes.body}</p>
            <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
            `
        textTarget.innerHTML = resultHTML;
    });
    req.open("GET", "https://favqs.com/api/");
    req.setRequestHeader("Authorization", 'Token token="34803f76fbb9908169a9377a0111f0cb"');
    req.send()
});
    


