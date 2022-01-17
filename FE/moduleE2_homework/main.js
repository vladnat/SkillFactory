import { NumIsNumber } from "/task_1.js"
import { TypeX } from "/task_2.js"
import { ReverseString } from "/task_3.js"
import { RandomNum } from "/task_4.js"
import { SummaryArray } from "/task_5.js"
import { AllTheSameInArray } from "/task_6.js"


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

let task_4 = document.querySelector('.task_4')
task_4.addEventListener('click', function() {
    console.log(RandomNum())
})

let task_5 = document.querySelector('.task_5')
task_5.addEventListener('click', function() {
    SummaryArray()
})

let task_6 = document.querySelector('.task_6')
task_6.addEventListener('click', function() {
    console.log(AllTheSameInArray())
})

