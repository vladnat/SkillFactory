// Создайте произвольный массив Map.
// Получите его ключи и выведите в консоль все значения в виде «Ключ — Х, значение — Y».
// Используйте шаблонные строки.

const Obj = new Map()

for (let i = 1; i < 7; i++) {
    Obj.set(i, i)
}

export const ViewObject = () => {
    Obj.forEach(function(value,key) {
        console.log(`Ключ - ${key}, значение - ${value}`);    
      });
}
