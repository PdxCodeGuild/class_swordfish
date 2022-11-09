const rot13_encryption_cipher = (encrypted) => {
    const alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM';

    return encrypted.replace(/[a-z]/gi, letter => alphabet[alphabet.indexOf(letter) + 13]);
  }

let message = prompt("please enter what you want encrypted.")

alert(rot13_encryption_cipher(message))





