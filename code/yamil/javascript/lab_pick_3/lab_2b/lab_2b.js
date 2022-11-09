let first_digit = {
    1 : "ten",
    2 : "twenty",
    3 : "thirty",
    4 : "forty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety"
    }

let second_digit = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen"
    }

let hundreds_digit = {
    1 : "one-hundred",
    2 : "two-hundred",
    3 : "three-hundred",
    4 : "four-hundred",
    5 : "five-hundred",
    6 : "six-hundred",
    7 : "seven-hundred",
    8 : "eight-hundred",
    9 : "nine-hundred",
}


convert.addEventListener('click', function() {
    let x = document.getElementById('num')
    x = Number(x.value)
    console.log(x)
    console.log(typeof x)
    let convert = document.getElementById('convert')
    console.log(convert)
    let result = document.getElementById('result')
    
    let hundreds = Math.floor(x/100)
    let hundreds_2 = x % 100
    let hundreds_3 = hundreds_2 % 10
    let hundreds_4 = Math.floor(hundreds_2/10)
    let tens = Math.floor(x/10)
    let ones = x % 10
    let answer
    console.log(tens)

    if (x <= 19) {
        answer =(`You have entered ${second_digit[x]}.`)
    } else if (99 > x > 19 && x % 10 === 0) {
        answer =(`You have entered ${first_digit[tens]}.`)
    } else if (100 > x && Math.floor(x/10) === 0) {
        answer =(`You have entered ${first_digit[tens]}.`)
    } else if (100 > x && Math.floor(x/10) !== 0) {
        answer =(`You have entered ${first_digit[tens]}-${second_digit[ones]}.!!!`)
    } else if (x > 99 && x % 100 === 0) {
        answer =(`You have entered ${hundreds_digit[hundreds]}.`)
    } else if (x > 99 && x % 100 < 10) {
        answer =(`You have entered ${hundreds_digit[hundreds]} and ${second_digit[ones]}.`)
    } else if (x > 99 && x % 100 !== 0) {
        answer =(`You have entered ${hundreds_digit[hundreds]} and ${first_digit[hundreds_4]}-${second_digit[ones]}.`)
    } else {
        answer =("Please enter a valid number between 0 and 999.")
    }
    result.innerText = answer
})

// ---------------------------------------------------------------------------------------------------------------
