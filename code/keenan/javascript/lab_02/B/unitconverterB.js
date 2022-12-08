let input = document.getElementById('input')
let unit_in = document.getElementById('unit_in')
let unit_out = document.getElementById('unit_out')

const meters = {
    mi:1609.34,
    ft:0.3048,
    m:1,
    km:1000,
    yd:0.9144,
    in:0.0254,
}

convertBtn.addEventListener('click', function () {
    // console.log(unit_in.value)
    // console.log(parseFloat(input.value) * 1000)
    let output_distance = parseFloat(input.value) * meters[unit_in.value] / meters[unit_out.value]
    // console.log(output_distance)
    // console.log(output_distance.toFixed(2))
    output_distance = output_distance.toFixed(2)
    let output = 'Your output distance is ' + output_distance + ' ' + unit_out.value
    // console.log(output)
    let pTag = document.getElementById('output')
    pTag.innerText = output
    // alert('Your output distance is ' + output_distance + ' ' + unit_out.value)
})