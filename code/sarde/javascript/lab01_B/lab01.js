

let select_input_unit = document.querySelector('#select_input_unit');
console.log(select_input_unit)
let distance_input = document.querySelector('#distance_input')
console.log('distance', distance_input)
let select_output_unit = document.querySelector('#select_output_unit')
console.log(select_output_unit)
let convert_bt = document.querySelector('#convert_bt');
let output_div = document.querySelector('#output_div');
convert_bt.onclick = function () {
    let units = {
        'ft': 0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
        'yd': 0.9144,
        'in': 0.0254
    }
    // console.log(units)
    let distance = distance_input.value
    // console.log(typeof distance, distance)//string
    let convertedInputDistance = parseInt(distance)
    // // console.log('Input distance as an Integer', convertedInputDistance)
    // console.log(typeof convertedInputDistance)//number
    let inputUnit = units[select_input_unit.value]
    // console.log(inputUnit)
    // let outputUnit = units[select_output_unit.value]
    // console.log(outputUnit)
    let total = convertedInputDistance * inputUnit / distance
    // console.log('Total', total)

    output_div.innerText = `${convertedInputDistance + select_input_unit.value + ' ' + 'is' + ' ' + total.toFixed(2) + select_output_unit.value
        }`
    // console.log(output_div)

}