// Записать в переменную случайное целое число в диапазоне [0; 100]. Используйте объект Math.

export const RandomNum = () => {
    return `случайное целое число в диапазоне [0; 100] - ${Math.floor(Math.random() * 101)}`
}