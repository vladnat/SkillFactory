import { NumIsNumber } from "/task_1.js"
import { TypeX } from "/task_2.js"


// console.log(NumIsNumber)

//let num = NumIsNumber()
// console.log(num)

let task_1 = document.querySelector('.task_1')
task_1.addEventListener('click', function() {
    console.log(NumIsNumber())
})

let task_2 = document.querySelector('.task_2')
task_2.addEventListener('click', function() {
    console.log(TypeX())
})