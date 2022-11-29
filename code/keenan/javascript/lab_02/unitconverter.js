// code for a prompt based measurement converter

let input = prompt('Enter the number of meters to convert: ')
let unit_out = prompt('Please provide the conversion unit in its abbreviated form. What is the output unit? ')
let output

let unit_in


// can probably consolidate my rounding logic at the same time i fix that last double error
// if output units is meters, run main section. if output is any of the others, convert m again to output

if (unit_out === 'ft') {
    output = input / 0.3048
    output = output.toFixed(2)
}
else if (unit_out === 'mi') {
    output = input / 1609.34
    output = output.toFixed(2)
}
else if (unit_out === 'm') {
    output = input
} 
else if (unit_out === 'km') {
    output = input / 1000
    output = output.toFixed(2)
}
else if (unit_out === 'yd') {
    output = input / 0.9144
    output = output.toFixed(2)
}
else if (unit_out === 'in') {
    output = input / 0.0254
    output = output.toFixed(2)
}
else {
    alert('enter a correct unit')
}

// getting an undefined error because this is running after the 'else' statement
alert(input + " meters is " + output + ' ' + unit_out)
