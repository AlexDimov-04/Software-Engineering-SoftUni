function employees(array) {
    let people = {};

    for (const name of array) {
        people[name] = name.length;
    }

    for (const key in object) { 
        console.log(`Name: ${key} -- Personal Number: ${people[key]}`);
    }
}