let nums = document.getElementsByClassName("num")
let results = document.getElementById("results")
let calcBtn = document.getElementById("calculate")
let addNumBtn = document.getElementById("add-num")
let numDiv = document.getElementById("num-div")

addNumBtn.addEventListener('click', function() {
    let newNum = document.createElement("input")
    newNum.type = "number"
    newNum.classList.add("num")
    // newNum.addEventListener('keyup', function(event) {
    //     if (event.key === "Enter") {
    //         calculate()
    //     }
    // })

    let newNumRemove = document.createElement("button")
    newNumRemove.innerText = "×"
    newNumRemove.addEventListener('click', function() {
        newNum.previousSibling.remove()
        newNum.remove()
        newNumRemove.remove()
    })

    numDiv.append(" + ")
    numDiv.appendChild(newNum)
    numDiv.appendChild(newNumRemove)
})

function calculate() {
    let answer = 0
    for (let i=0; i < nums.length; i++) {
        if (nums[i].value === "") {
            // nums[i].value = 0
            continue
            // nums[i].remove()
            // continue
        }
        answer += parseFloat(nums[i].value)
    }
    results.innerText = answer
}

calcBtn.addEventListener('click', calculate)

for (let i=0; i < nums.length; i++) {
    nums[i].addEventListener('keyup', function(event) {
        if (event.key === "Enter") {
            calculate()
        }
    })
}

// for (let i=0; i < nums.length; i++) {
//     nums[i].addEventListener('change', calculate)
// }