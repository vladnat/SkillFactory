// Определить иерархию электроприборов. Включить некоторые в розетку.
// Посчитать потребляемую мощность. 
// Таких приборов должно быть, как минимум, два (например, настольная лампа и компьютер).
// Выбрав прибор, подумайте, какими свойствами он обладает.
// План:
// 1. Определить родительскую функцию с методами, которые включают/выключают прибор из розетки.
// 2. Создать делегирующую связь [[Prototype]] для двух конкретных приборов.
// 3. У каждого из приборов должны быть собственные свойства и, желательно, методы,
//    отличные от родительских методов.
// 4. Создать экземпляры каждого прибора.
// 5. Вывести в консоль и посмотреть результаты работы, гордиться собой. :)

function ElectricalUser (name, power) {
    this.name = name,
    this.power = power
}

ElectricalUser.prototype.getOn = function (status) {
    this.capacity = status ? this.power : 0
    this.status = status ? 'on' : 'off'
    return `Device ${this.name} is turned ${this.status} and uses ${this.capacity} watts of energy.`
}

function ElectricalHome (name, power) {
    this.position = 'room'
    this.name = name,
    this.power = power
}

ElectricalHome.prototype = new ElectricalUser()

const laptop = new ElectricalHome('laptop', 60)
const lamp = new ElectricalHome('lamp', 100)
console.log(laptop.getOn(0))
console.log(lamp.getOn(1))
console.log(laptop.capacity + lamp.capacity)

