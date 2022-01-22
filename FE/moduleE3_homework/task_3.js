// Написать функцию, которая принимает число как аргумент и возвращает функцию, 
// которая также принимает число как аргумент и возвращает сумму этих двух чисел. 
// Выведите в консоль результат.

const GetNumber = (num) => {
    return function(x = 0) {
        return num + x
    }
}

let result = GetNumber(+prompt('Enter number'))
console.log(result(+prompt('Enter number')))