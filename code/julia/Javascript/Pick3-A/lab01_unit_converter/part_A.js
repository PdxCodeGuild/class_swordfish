// Unit converter

let distance = {
    ft : 0.3048,
    m : 1,
    mi : 1609.34,
    km : 1000,
    yd : 0.9144,
    in : 0.0254
}

let user = prompt('What is the distance?: ')
let unit_str = prompt('What are the units?(ft, m, mi, km, yd, in): ')
let unit_str2 = prompt('What are the output units?(ft, m, mi, km, yd, in): ')

let results = user * distance[unit_str] / distance[unit_str2]

alert(results.toFixed() + unit_str2)

