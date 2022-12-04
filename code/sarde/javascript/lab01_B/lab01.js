

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
    console.log('PRINTING', typeof distance, distance)//string 12
    let inputUnit = units[select_input_unit.value]
    console.log('PRINTING', inputUnit)//0.3048
    let outputUnit = units[select_output_unit.value]
    console.log('PRINTING', outputUnit)//0.0254
    // let convertedInputDistance = parseInt(distance)
    // // // console.log('Input distance as an Integer', convertedInputDistance)
    // // console.log(typeof convertedInputDistance)//number
    // let convertedInputUnit = units[inputUnit]
    // let convertedOutputUnit = units[outputUnit]

    // let total = convertedInputDistance * inputUnit / distance
    let total = distance * inputUnit//12 * 0.3048
    console.log('Total', total)//3.6576
    let result = total / outputUnit
    console.log(result)//144.00000000000003

    output_div.innerText = `${distance}${select_input_unit.value} is ${(result.toFixed(4))}${select_output_unit.value}`
    // console.log(output_div)

}