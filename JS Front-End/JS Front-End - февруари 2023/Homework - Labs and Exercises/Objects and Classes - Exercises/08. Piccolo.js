function piccolo(arr) {
    let parking = new Set();

    for (const line of arr) {
        let [command, number] = line.split(', ');

        if (command === 'IN') {
            parking.add(number);
        }
        else if (command === 'OUT') {
            parking.delete(number);
        }
    }

    if (parking.length === 0) {
        console.log("Parking Lot is Empty");
    } else {
        console.log([...parking].sort().join('\n'));
    }
}