let meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'in': 0.0254
}

let distance = prompt('Enter in distance:')
let in_unit = prompt('Enter starting units:')
let input_value = meters[in_unit]
let out_value = prompt('Enter output unit:')

let in_conversion = distance * input_value

for (key in meters){
    if (out_value == key){
        console.log(key)
        let conversion = in_conversion / meters[key]
        console.log(conversion)
        alert(conversion)
    }
}

// if (out_value === 'ft'){
//     conversion = in_conversion / meters['ft']
// } else if (out_value === 'mi'){
//     conversion = in_conversion / meters['mi']
// } else if (out_value === 'm'){
//     conversion = in_conversion / meters['m']
// } else if (out_value === 'km'){
//     conversion = in_conversion / meters['km']
// } else if (out_value === 'yard'){
//     conversion = in_conversion / meters['yard']
// } else if (out_value === 'in'){
//     conversion = in_conversion / meters['in']
// }

// alert(conversion)