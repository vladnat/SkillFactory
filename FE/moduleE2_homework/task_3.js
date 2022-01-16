// Дана строка. Необходимо вывести в консоль перевёрнутый вариант. Например, "Hello" -> "olleH".

const EnterString = () => {
    return prompt('Enter any word or string')
}

export const ReverseString = () => {
   let str = EnterString()
   return `Your reversed string is - ${str.split('').reverse().join('')}`
}