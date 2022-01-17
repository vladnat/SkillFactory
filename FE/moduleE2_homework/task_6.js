// Дан массив. Проверить, одинаковые ли элементы в массиве
// и вывести результат true или false в консоль. 
// Речь идёт не о двух рядом стоящих одинаковых элементах, а обо всех. 
// Проверить, все ли элементы в массиве одинаковые.

let array = Array(10).fill(5)
// array.push(6)

export const AllTheSameInArray = () => {
    let start = array[0]
    return array.every(elem => elem === start)
}
