const unitConverter = {
    'feet': 0.3048,
    'mile': 1609.34,
    'meter': 1,
    'kilometer': 1000,
    'yard': 0.9144,
    'inch': 0.0254,
}
    let submit = document.getElementById('submit')
    let result = document.getElementById('result')
    
    
    submit.addEventListener('click', function() {
        let unitLength = Number(document.getElementById('unitLength').value)
        let originalUnit = document.getElementById('originalUnit').value
        let convertedUnit = document.getElementById('convertedUnit').value
    
        let length = unitLength * unitConverter[originalUnit]
    
        let conversionResult
        for (let unit of Object.getOwnPropertyNames(unitConverter)) {
            if (convertedUnit == unit) {
                conversionResult = length / unitConverter[unit]
                result.innerText = conversionResult.toString()
            }
        }
    })