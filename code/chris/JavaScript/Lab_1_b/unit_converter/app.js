let distance = document.getElementById('distance')
let input_unit = document.getElementById('input_unit')
let output_unit = document.getElementById('output_unit')
let convert = document.getElementById('convert')  // i don't have to match i.d. and var name
let answer = document.getElementById('answer')

const units = {
    m:1,
    mi:1609.34,
    ft:0.3048,
    km:1000,
    yd:0.9144,
    inches:0.0254,
}

// input_unit = 'ft'
// let length = units[input_unit]
// alert(length)

convert.addEventListener('click', function() {
    console.log(distance.value)
    let conversion = parseInt(distance.value) * units[input_unit.value] / units[output_unit.value]
    // conversion = parseInt(conversion.toFixed(2)) + output_unit.value
    console.log(conversion)
    answer.innerText = conversion
})