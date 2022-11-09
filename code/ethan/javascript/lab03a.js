const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

let tens = ['void', 'void', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

let num = prompt('Type a number between 1-999. ')


if (num < 20) {
    alert(numbers[num])
} else if (num > 20 && num < 100) {
    Array.from(num)
    let digit_one = num[0]
    let digit_two = num[1]
    alert(tens[digit_one] + numbers[digit_two])
} else if (num > 99 && num < 1000) {
    Array.from(num)
    let digit_one = num[0]
    let digit_two = num[1]
    let digit_three = num[2]
    alert(numbers[digit_one] + "hundred and " + tens[digit_two] + numbers[digit_three] )
}