function shoppingList(array) {
    let groceries = array[0].split('!');

    for (const line of array) {
        if (line === 'Go Shopping!') {
            break;
        }

        let command = line.split(' ');

        if (command.includes('Urgent')) {
            let item = command[1];

            if (!(groceries.includes(item))) {
                groceries.unshift(item);
            }
        }
        else if (command.includes('Unnecessary')) {
            let item = command[1];

            if (groceries.includes(item)) {
                groceries.pop(groceries.indexOf(item));
            }
        }
        else if (command.includes('Correct')) {
            let [_c, oldItem, newItem] = command;

            if (groceries.includes(oldItem)) {
                groceries[groceries.indexOf(oldItem)] = newItem;
            }
        }
        else if (command.includes('Rearrange')) {
            let item = command[1];

            if (groceries.includes(item)) {
                groceries.pop(groceries.indexOf(item));
                groceries.push(item);
            }
        }
    }

    console.log(groceries.join(', '));
}

shoppingList((["Milk!Pepper!Salt!Water!Banana",
"Urgent Salt",
"Unnecessary Grapes",
"Correct Pepper Onion",
"Rearrange Grapes",
"Correct Tomatoes Potatoes",
"Go Shopping!"])

)