// code for a prompt based measurement converter

alert('Please provide all units of measure in abbreviated form.')

let input = prompt('Enter a distance  to convert: ')
let unit_in = prompt('Provide the units for the intial distance to convert: ')
let unit_out = prompt('What unit would you like to convert this distance to? ')
let output
let meters

// can probably consolidate my rounding logic at the same time i fix that last double error
// if output units is meters, run main section. if output is any of the others, convert m again to output


if (unit_in === 'ft') {
    meters = input * 0.3048
}
else if (unit_in === 'mi') {
    meters = input * 1609.34
}
else if (unit_in === 'm') {
    meters = input
}
else if (unit_in === 'km') {
    meters = input /  1000
}
else if (unit_in === 'yd') {
    meters = input * 0.9144
}
else if (unit_in === 'in') {
    meters = input * 0.0254
}
else {
    alert('Enter a correct unit for the input distance')
}

// alert(meters + " meters")

if (unit_out === 'm') {
    output = meters
} 
else if (unit_out === 'ft') {
    output = meters / 0.3048
    output = output.toFixed(2)
}
else if (unit_out === 'mi') {
    output = meters / 1609.34
    output = output.toFixed(2)
}

else if (unit_out === 'km') {
    output = meters / 1000
    output = output.toFixed(2)
}
else if (unit_out === 'yd') {
    output = meters / 0.9144
    output = output.toFixed(2)
}
else if (unit_out === 'in') {
    output = meters / 0.0254
    output = output.toFixed(2)
}
else {
    alert('enter a correct unit')
}


// getting an undefined error because this is running after the 'else' statement
alert(input + ' ' + unit_in+ ' ' + output + ' ' + unit_out)
