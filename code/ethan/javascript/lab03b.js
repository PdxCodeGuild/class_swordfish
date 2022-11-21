let num = document.getElementById('num')

digits_to_string.addEventListener('click', function() {
    
    const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    let tens = ['void', 'void', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    let number = num.value

    let answer

    if (number < 20) {
        answer = numbers[number]
    } else if (number > 20 && number < 100) {
        Array.from(number)
        let digit_one = number[0]
        let digit_two = number[1]
        answer = tens[digit_one] + numbers[digit_two]
    } else if (number > 99 && number < 1000) {
        Array.from(number)
        let digit_one = number[0]
        let digit_two = number[1]
        let digit_three = number[2]
        answer = numbers[digit_one] + "hundred and " + tens[digit_two] + numbers[digit_three]
    }        
    result.innerText = answer
})