// Дана переменная Х, которая может принимать любое значение. 
// Написать программу, которая в зависимости от типа данных Х выводит в консоль 
// сообщение вида: «X — число».
// Опишите три случая: когда х = числу, строке или логическому типу. 
// В других случаях выводите сообщение:  Тип x не определён.

const EnterX = () => { 
    return prompt('Please, enter any number or string or boolean')
}

export const TypeX = () => {
    let X = EnterX()

    if (typeof(+X) === 'number' && !isNaN(+X)) return `${+X} - число`
    if (X === 'false' || X === 'true') return `${X} - логический тип`
    if (typeof(X) === 'string' && isNaN(X)) return `${X} - строка`
    return `Тип X не определён`
}