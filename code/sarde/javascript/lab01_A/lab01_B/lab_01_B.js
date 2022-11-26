

let select_input_unit = document.querySelector('#select_input_unit');
console.log(select_input_unit)
let distance_input = document.querySelector('#distance_input')
console.log('distance', distance_input)
let select_output_unit = document.querySelector('#select_output_unit')
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
    let input_unit = select_input_unit.value
    console.log(input_unit)
    let output_unit = select_output_unit.value
    console.log(output_unit)
    let convertedInputUnit = units[input_unit]
    console.log('convertedInputUnit', convertedInputUnit)
    let convertedOutputUnit = units[output_unit]
    console.log('convertedOutputUnit', convertedOutputUnit)
    let total = distance_input * convertedInputUnit
    console.log('total', total)
    output_div.innerText = total / convertedOutputUnit;
    console.log('output', output_div)

}