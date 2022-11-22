// Unit converter

let distance = {
    ft : 0.3048,
    m : 1,
    mi : 1609.34,
    km : 1000,
    yards : 0.9144,
    inches : 0.0254
}

let user = prompt('What is the distance?: ')
let unit_str = prompt('What are the units?: ')
let unit_str2 = prompt('What are the output units?: ')

let answer = user
let unit = distance[unit_str]
let results = unit * user
console.log(user + " " + unit_str + " is " + results + " " + unit_str2 )
alert(user + " " + unit_str + " is " + results + " " + unit_str2 )