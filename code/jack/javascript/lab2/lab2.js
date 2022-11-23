// unit converter lab in js

let distance_input = Number(prompt('enter a distance'))
let unit_input = prompt('what is the unit of entered distance? (ft, mi, m, km)')
let unit_output = prompt('what is the unit to convert to? (ft, mi, m, km)')

converstions = {
    'ft':0.3048,
    'mi':1609.34,
    'm':1,
    'km':1000,
}

let distance_m
for (let unit of Object.getOwnPropertyNames(converstions)) {
    if (unit_input == unit) {
        distance_m = distance_input * converstions[unit]
    }
}

let distance_output
for (let unit of Object.getOwnPropertyNames(converstions)) {
    if (unit_output == unit) {
        distance_output = distance_m / converstions[unit]
    }
}

alert(distance_input + ' ' + unit_input + ' = ' + distance_output + ' ' + unit_output)