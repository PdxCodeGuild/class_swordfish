
// Lab 1: Unit Converter
/*
Version 1
-Ask the user for the number of feet
-print equivalent distance in meters
- 1 ft is 0.3048 m.
-output = meters = multiply input distance by 0.3048

let units = {
    feet: 0.3048
}
console.log(units)

//ask user for number of feet
let inputFeet = prompt('What is the distance in feet?')
// console.log(typeof input_feet)
feet = parseInt(input_feet)
// console.log(typeof feet)
let total = feet * units['feet']
// console.log(Math.round(total, 4))
alert(`${feet} ft is ${Math.round(total, 4)} m`)
*/
//-------------------------------------------------------------------------------------------------------------------------//

/*
Version 2
-Allow the user to also enter the units
-depending on the unit, convert distance-meters


let units = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000
}
console.log(units)

// ask the user to enter the distance
let inputDistance = prompt('What is the distance?')
// ask the user to enter the units
let inputUnit = prompt('What is the unit(ft, mi, m, km)?')
distance = parseInt(inputDistance)//convert to a number
let total = distance * units[inputUnit]
// console.log(Math.round(total))
alert(`${distance} ${inputUnit} is ${total.toFixed(2)} m`)
*/
//------------------------------------------------------------------------------------------------------------------//

/*
Version 3
-Add support for yards, and inches
-1 yard is 0.9144 m
-1 inch is 0.0254 m
*/

let units = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254
}
console.log(units)

//ask the user to enter the distance
let inputDistance = prompt('What is the distance?')
//ask the user to enter the unit
let inputUnit = prompt('What is the unit(ft, i, m, km, yd, in)?')
//convert inputDistance to a Number
let distance = parseInt(inputDistance)
let total = distance * units[inputUnit]
// console.log(total.toFixed(2))
alert(`${distance} ${inputUnit} is ${total.toFixed(2)} m`)