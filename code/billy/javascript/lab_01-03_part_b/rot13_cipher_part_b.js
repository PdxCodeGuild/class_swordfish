let submit = document.getElementById('submit')
let encryptedMessage = document.getElementById('encryptedMessage')

const rot13EncryptionCipher = (encrypted) => {
    const alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM';
    return encrypted.replace(/[a-z]/gi, letter => alphabet[alphabet.indexOf(letter) + 13]);
  }

submit.addEventListener('click', function(){
    let originalMessage = document.getElementById('originalMessage').value

    let message = (rot13EncryptionCipher(originalMessage))

    encryptedMessage.innerText = message
})
