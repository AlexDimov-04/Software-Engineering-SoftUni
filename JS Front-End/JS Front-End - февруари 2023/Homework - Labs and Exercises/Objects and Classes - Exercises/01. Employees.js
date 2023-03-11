function employees(array) {
    let people = {};

    for (const name of array) {
        people[name] = name.length;
    }

    array.forEach(name => {
        console.log(`Name: ${name} -- Personal Number: ${name.length}`);
    });
}