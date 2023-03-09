function solve(arr) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }
    for (let item of arr){
        let [name, age] = item.split(' ');
        let catObj = new Cat(name, age);
        catObj.meow();
    }
}

// for (const line of arr) {
//     [catName, age] = line.split(' ');
//     console.log(`${catName}, age ${age} says Meow`)
// }