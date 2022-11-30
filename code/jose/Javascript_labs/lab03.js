let letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
  'w', 'x', 'y', 'z']

  let message = document.getElementById('message')
  let rotation = document.getElementById('rotnumber')

  textencode.addEventListener("click", function(){
    let messageencoded = []
    for (let char of message.value){
        if (letters.includes(char)){
            messageencoded.push(letters[(letters.indexOf(char) + parseFloat(rotation.value)) % letters.length])
        }
    }
    encodedtext.innerText = messageencoded.join('')
  })