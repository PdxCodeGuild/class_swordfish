let conversion_values = { 'feet': 0.3048,
'miles': 1609.34, 
'meters': 1, 
'kilometers': 1000,
'yards': 0.9144,
'inches': 0.0254 
}

let conversion_values_meters = {'feet': 3.2808399,
'miles': .00621,
'kilometers': .001,
'yards': 1.0936133,
'inches': 39.3700787
}

let user_distance = document.getElementById("user-distance")
let user_units = document.getElementById("user-units")
let desired_units = document.getElementById("desire-units")

let submit = document.getElementById("submit")
let result = document.getElementById("result")

submit.addEventListener('click', function(){
    let conversion_to_meters = parseInt(user_distance) * conversion_values_meters[user_units]
    alert(conversion_to_meters)
    let conversion = conversion_to_meters * conversion_values[desired_units]
    result.innerText =  conversion
})