const unit_converter = {
    'feet': 0.3048,
    'mile': 1609.34,
    'meter': 1,
    'kilometer': 1000,
    'yard': 0.9144,
    'inch': 0.0254
}

let distance = prompt("what is the distance? (enter the numerical amount)")

let unit = prompt("what are the input units? (acceptable units of measurement are: ft, m, mi, in, y, km)")

let output_unit = prompt("what are the output units? (acceptable units of measurement are: ft, m, mi, in, y, km)")

let output_distance = distance * unit_converter[unit]

alert(output_distance / unit_converter[output_unit] + output_unit)