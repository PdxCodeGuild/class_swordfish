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

let distance = Number(prompt("What is the distance?"))
let units = prompt("What is the unit?:")
let output = prompt("What is the output unit?")

let total = distance * metrics[units]
let total_2 = total / metrics[output]

if (output !== units) {
    alert(`${distance} ${units} is equal to ${total_2} ${output}.`)
} else {
    alert(`${distance} ${units} is equal to ${total} ${output}.`)
}