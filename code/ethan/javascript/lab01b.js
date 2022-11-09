
let distance = document.getElementById('distance')

let inputunit = document.getElementById('inputunit')

let output = document.getElementById('output')

let convert = document.getElementById('convert')

let result = document.getElementById('result')



// let ft = .3048
// let mi = 1609.34
// let m = 1.0
// let km = 1000

convert.addEventListener('click', function() {
    let answer

    let outputvalue

    if (output.value === 'feet') {
        outputvalue = .3048
    } else if (output.value === 'miles') {
        outputvalue = 1609.34
    } else if (output.value === 'meters') {
        outputvalue = 1
    } else if (output.value === 'kilometers') {
        outputvalue = 1000
    }
    
    if (inputunit.value === 'feet') {
        let meters = parseFloat(distance.value) * .3048
        let conversion = meters/outputvalue
        answer = conversion
    } else if (inputunit.value === 'miles') {
        let meters = parseFloat(distance.value) * 1609.34
        let conversion = meters/outputvalue
        answer = conversion
    } else if (inputunit.value === 'meters') {
        let meters = parseFloat(distance.value) * 1
        let conversion = meters/outputvalue
        answer = conversion
    } else if (inputunit.value === 'kilometers') {
        let meters = parseFloat(distance.value) * 1000
        let conversion = meters/outputvalue
        answer = conversion
    }
    result.innerText = answer
})