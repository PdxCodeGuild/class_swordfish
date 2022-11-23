let meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'in': 0.0254
}

let distance = document.getElementById('distance')
let inUnit = document.getElementById('in-unit')

let out_value = document.getElementById('out_value')


convert.addEventListener('click', function(){
    let input_value = meters[inUnit.value]
    let in_conversion = parseFloat(distance.value) * input_value
    for (key in meters){
        if (out_value.value == key){
            let conversion = in_conversion / meters[key]
            result.innerText = conversion
        }
    }
})