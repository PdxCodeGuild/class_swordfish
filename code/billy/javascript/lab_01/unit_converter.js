const unit_converter = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'y': 0.9144,
    'in': 0.0254
}

let distance = prompt("what is the distance?")

let unit = prompt("what are the input units?")

let output_unit = prompt("what are the output units?")

let output_distance = distance * unit_converter[unit]

alert(output_distance / unit_converter[output_unit])