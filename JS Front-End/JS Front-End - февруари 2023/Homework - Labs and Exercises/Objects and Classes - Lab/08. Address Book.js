function addressBook(array) {
    let people = {};

    for (const line of array) {
        let [name, address] = line.split(':');
        people[name] = address
    }

    let sortedNames = Object.keys(people).sort((a, b) => a.localeCompare(b));

    for (const name of sortedNames) {
        console.log(`${name} -> ${people[name]}`);
    }
}