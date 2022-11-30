// Rot13 Part B 

let rot13={
    "a" : "n",
    "b" : "o",
    "c" : "p",
    "d" : "q",
    "e" : "r",
    "f" : "s",
    "g" : "t",
    "h" : "u",
    "i" : "v",
    "j" : "w",
    "k" : "x",
    "l" : "y",
    "m" : "z",
    "n" : "a",
    "o" : "b",
    "p" : "c",
    "q" : "d",
    "r" : "e",
    "s" : "f",
    "t" : "g",
    "u" : "h",
    "v" : "i",
    "w" : "j",
    "x" : "k",
    "y" : "l",
    "z" : "m",
}

// let rot = 13
let encode = document.querySelector("#Rot13")
let results = document.querySelector("#results")


encode.addEventListener('click', function (){
    console.log(encode)

    let message = document.querySelector("#message").value
    
   
    let output = ''
        for ( let char of message){
            output += rot13[char]
            console.log(char)
        }
            
    console.log(message)

        results.innerText = 'RESULTS: ' + output
    
    
    
    
    
    
    
    
})



// let user_word = prompt("Type a word: ")
// let encoded_str = ''

// for (let char of user_word){
//     encoded_str += rot13[char]
// }

// alert(encoded_str)
