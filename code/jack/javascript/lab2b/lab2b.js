// unit converter lab in js

// let length_input = Number(prompt('enter a length'))
// let unit_input = prompt('what is the unit of entered length? (ft, mi, m, km)')
// let unit_output = prompt('what is the unit to convert to? (ft, mi, m, km)')

converstions = { // no let?
    'ft':0.3048,
    'mi':1609.34,
    'm':1,
    'km':1000,
}


let calculate = document.getElementById('calculate')
let length_output = document.getElementById('length_output')

let length_input = document.getElementById('length_input')
let unit_input = document.getElementById('unit_input')
let unit_output = document.getElementById('unit_output')

calculate.addEventListener('click', function() {
    length_input_value = Number(length_input.value)
    unit_input_value = unit_input.value
    unit_output_value = unit_output.value

    let length_m = length_input_value * converstions[unit_input_value]

    let result
    for (let unit of Object.getOwnPropertyNames(converstions)) {
        if (unit_output_value == unit) {
            result = length_m / converstions[unit]
            length_output.innerText = result.toString()
        }
    }
    // console.log(length_output)
})
