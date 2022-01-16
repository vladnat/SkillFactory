import { NumIsNumber } from "/task_1.js"
import { TypeX } from "/task_2.js"
import { ReverseString } from "/task_3.js"


let task_1 = document.querySelector('.task_1')
task_1.addEventListener('click', function() {
    console.log(NumIsNumber())
})

let task_2 = document.querySelector('.task_2')
task_2.addEventListener('click', function() {
    console.log(TypeX())
})

let task_3 = document.querySelector('.task_3')
task_3.addEventListener('click', function() {
    console.log(ReverseString())
})