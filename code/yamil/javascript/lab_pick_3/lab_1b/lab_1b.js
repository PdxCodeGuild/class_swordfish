let metrics = {
    ft : 0.3048,
    feet : 0.3048,
    foot : 0.3048,
    mile : 1609.34,
    miles : 1609.34,
    meter : 1,
    meters : 1,
    km : 1000,
    kilometer : 1000,
    kilometers : 1000,
    yard : 0.9144,
    yards : 0.9144,
    inch : 0.0254,
    inches : 0.0254
}

let distance = document.getElementById('distance')            // Number(prompt("What is the distance?"))
let units = document.getElementById('input_unit')             //prompt("What is the unit?:")
let output = document.getElementById('output_unit')           //prompt("What is the output unit?")
let convert = document.getElementById('convert')
let result = document.getElementById('result')


convert.addEventListener('click', function() {
    let answer
    let total = parseFloat(distance.value) * metrics[units.value]
    console.log(total)
    let total_2 = total / metrics[output.value]
    console.log(total_2)
    if (output.value !== units.value) {
        answer = `${distance.value} ${units.value} is equal to ${total_2} ${output.value}.`
    } else {
        answer = `${distance.value} ${units.value} is equal to ${total} ${output.value}.`
    }
    result.innerText = answer
})