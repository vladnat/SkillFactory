// Дан массив. Нужно вывести в консоль количество чётных и нечётных элементов в массиве.
// Если в массиве есть нулевой элемент, то он учитывается и выводится отдельно. 
// При выполнении задания необходимо учесть, что массив может содержать не только числа,
// но и, например, знаки, null и так далее.

let array = [1, 4, '87h', null, NaN, 0, false, true]

const counters = {'odd': 0, 'even': 0, 'null': 0, 'zero': 0, 'boolean': 0, 'NaN': 0, 'string': 0}

function help(arr) {
    for (let i=0; i < array.length; i++) {
        // console.log(array[i])
        let el = array[i]
        // console.log(el)
        if (typeof(el) === 'number' && el !== 0 && !isNaN(el) && (el !== false || el !== true) && typeof(el) != 'object')  {
            if (el % 2) {
                counters.odd += 1
                //console.log(el, 'odd')
            } else if (!(el % 2)) {
                counters.even += 1
                //console.log(el, 'even')
            }  
        }   else if (isNaN(el) && typeof(el) !== 'string') {
            counters['NaN'] += 1
            //console.log(el, 'NaN')
        }   else if (el === 0) {
            counters.zero += 1
            //console.log(el, 'zero')
        }   else if (el === false || el === true) {
            counters.boolean += 1
            //console.log(el, 'boolean')
        }   else if (typeof(el) == 'string') {
            counters.string += 1
            //console.log(el, 'string')
        }   else counters.null += 1
    }
    return counters
}

export const CountTypesOfMassive = () => {
    return help(array)
}
    
