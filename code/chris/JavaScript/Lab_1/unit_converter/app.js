let distance = prompt("What is the distance you would like to convert? ")
distance = parseInt()
let units = prompt("What are the units? ")
let units_output = prompt("What is your desired unit output? ")

let m = 1
let mi = 1609.34
let ft = 0.3048
let km = 1000
let yd = 0.9144
let inches = 0.0254

if (units === 'm') {
    users_unit = m
} else if (units === 'mi') {
    users_unit = mi
} else if (units === 'ft') {
    users_unit = ft
} else if (units === 'km') {
    users_unit = km
} else if (units === 'yd') {
    users_unit = yd
} else if (units === 'inches') {
    users_unit = inches
}

if (units_output === 'm') {
    users_converter = m
} else if (units === 'mi') {
    users_converter = mi
} else if (units === 'ft') {
    users_converter = ft
} else if (units === 'km') {
    users_converter = km
} else if (units === 'yd') {
    users_converter = yd
} else if (units === 'inches') {
    users_converter = inches
}

let conversion = users_unit * users_unit

alert(math.round(conversion / users_converter))