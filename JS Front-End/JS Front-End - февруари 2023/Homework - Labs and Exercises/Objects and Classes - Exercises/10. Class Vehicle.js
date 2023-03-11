class Vehicle {
    constructor(type, model, parts, fuel) {
        this.type = type;
        this.model = model;
        this.parts = parts;
        this.fuel = fuel;

        parts.quality = parts.engine * parts.power;
    }

    drive(loss) {
        this.fuel -= loss;
        if (this.fuel < 0) {
            this.fuel = 0;
        }

        return this.fuel;
    }
}