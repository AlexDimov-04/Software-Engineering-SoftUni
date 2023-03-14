function pianist(array) {
    let pieces = Number(array.shift());
    let composers = {};

    for (let index = 1; index <= pieces; index++) {
        let [piece, composer, key] = array.shift().split('|');
        composers[piece] = { composer, key };
    }

    for (const line of array) {
        if (line === 'Stop') {
            break;
        }     
        let command = line.split('|');

        if (command.includes('Add')) {
            let [_c, piece, composer, key]  = command;

            if (!composers.hasOwnProperty(piece)) {
                composers[piece] = {composer, key};
                console.log(`${piece} by ${composer} in ${key} added to the collection!`);
            } else {
                console.log(`${piece} is already in the collection!`);
            }
        }
        else if (command.includes('Remove')) {
            let [_c, piece] = command;

            if (composers.hasOwnProperty(piece)) {
                delete composers[piece];
                console.log(`Successfully removed ${piece}!`);
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            }
        }
        else if (command.includes('ChangeKey')) {
            let [_c, piece, newKey] = command;

            if (composers.hasOwnProperty(piece)) {
                composers[piece].key = newKey;
                console.log(`Changed the key of ${piece} to ${newKey}!`);
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection."`);
            }
        }
        
    }

    for (const [key, value] of Object.entries(composers)) {
        console.log(`${key} -> Composer: ${value.composer}, Key: ${value.key}`);
    }
}

pianist([
    '4',
    'Eine kleine Nachtmusik|Mozart|G Major',
    'La Campanella|Liszt|G# Minor',
    'The Marriage of Figaro|Mozart|G Major',
    'Hungarian Dance No.5|Brahms|G Minor',
    'Add|Spring|Vivaldi|E Major',
    'Remove|The Marriage of Figaro',
    'Remove|Turkish March',
    'ChangeKey|Spring|C Major',
    'Add|Nocturne|Chopin|C# Minor',
    'Stop'
  ]
  
)