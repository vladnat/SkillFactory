// Переписать консольное приложение из предыдущего юнита на классы.


class ElectricalUser {
    constructor (name, power) {
        this.name = name;
        this.power = power;
    }

    getOn(status) {
        this.capacity = status ? this.power : 0
        this.status = status ? 'on' : 'off'
        return `Device ${this.name} is turned ${this.status} and uses ${this.capacity} watts of energy.`
    }
}

class ElectricalHome extends ElectricalUser {
    constructor (name, power) {
        super(name, power);
        this.position = 'room';
    }
    
    getOn(status) {
        return super.getOn()
    }
    
}

const laptop = new ElectricalHome('laptop', 60)
const lamp = new ElectricalHome('lamp', 100)

console.log(laptop.getOn(1))
console.log(lamp.getOn(1))