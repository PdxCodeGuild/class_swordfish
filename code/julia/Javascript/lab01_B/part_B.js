// Unit converter Part B
let unit = {
    ft : 0.3048,
    m : 1,
    mi : 1609.34,
    km : 1000,
    yards : 0.9144,
    inches : 0.0254
}

let button = document.querySelector("#bt")

button.addEventListener('click', function(){
    console.log("button pressed")
    
    let distance = document.querySelector("#distance").value
    let input_unit = document.querySelector("#input").value
    let output_unit = document.querySelector("#output").value
    let convert_unit = document.querySelector("#result")
    let answer = converter(distance, input_unit, output_unit)
    console.log("answer" , answer) 
    convert_unit.innerText = answer
    

})

function converter(distance,input_unit,output_unit){
    let value = unit[input_unit]
    let value2 = unit[output_unit]
    let result = value / value2 * distance

    

    console.log("value", value)
    console.log(value2)
    console.log("results", result)
    return result
   
}





// let answer = user
// let unit = distance[unit_str]
// let results = unit * user
// console.log(user + " " + unit_str + " is " + results + " " + unit_str2 )
// alert(user + " " + unit_str + " is " + results + " " + unit_str2)