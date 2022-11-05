let distance = prompt('What is the distance? ')

let inputunit = prompt('What are the input units? ')

let output = prompt("What are the output units? ")

let outputunit 

if (output === 'feet') {
    output = .3048
    outputunit = 'ft'
} else if (output === 'miles') {
    output = 1609.34
    outputunit = 'mi'
} else if (output === 'meters') {
    output = 1
    outputunit = 'm'
} else if (output === 'kilometers') {
    output = 1000
    outputunit = 'km'
}

let ft = .3048
let mi = 1609.34
let m = 1.0
let km = 1000

if (inputunit === 'feet') {
    let meters = distance * ft
    let conversion = meters/output
    alert(distance + " ft is " + conversion + " " + outputunit)
} else if (inputunit === 'miles') {
    let meters = distance * mi
    let conversion = meters/output
    alert(distance + " mi is " + conversion + " " + outputunit)
} else if (inputunit === 'meters') {
    let meters = distance * m
    let conversion = meters/output
    alert(distance + " m is " + conversion + " " + outputunit)
} else if (inputunit === 'kilometers') {
    let meters = distance * km
    let conversion = meters/output
    alert(distance + " km is " + conversion + " " + outputunit)
}