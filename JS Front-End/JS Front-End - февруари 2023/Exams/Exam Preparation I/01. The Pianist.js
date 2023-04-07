function pianist(array) {
    let pieces = Number(array.shift());
    let composers = {};
    let commandParser = {
        'Add': addPiece,
        'Remove': removePiece,
        'ChangeKey': changeKey
    };

    for (let index = 1; index <= pieces; index++) {
        const [piece, composer, key] = array.shift().split('|');
        composers[piece] = { composer, key };
    }

    for (const line of array) {
        if (line === 'Stop') {
            break;
        }

        let commmand = line.split('|');
        commandParser[commmand[0]](...commmand.slice(1));
    }

    printResult();

    function addPiece(piece, composer, key) {
        if (composers.hasOwnProperty(piece)) {
            console.log(`${piece} is already in the collection!`);
        } else {
            composers[piece] = { composer, key };
            console.log(`${piece} by ${composer} in ${key} added to the collection!`)
        }

    }

    function removePiece(piece) {
        if (!composers.hasOwnProperty(piece)) {
            console.log(`Invalid operation! ${piece} does not exist in the collection.`);
        } else {
            delete composers[piece];
            console.log(`Successfully removed ${piece}!`);
        }

    }

    function changeKey(piece, newKey) {
        if (!composers.hasOwnProperty(piece)) {
            console.log(`Invalid operation! ${piece} does not exist in the collection.`)
        } else {
            composers[piece]['key'] = newKey;
            console.log(`Changed the key of ${piece} to ${newKey}!`)
        }

    }

    function printResult() {
        for (const [key, value] of Object.entries(composers)) {
            console.log(`${key} -> Composer: ${value.composer}, Key: ${value.key}`)
        }
    }
}

pianist([
    '3',
    'Fur Elise|Beethoven|A Minor',
    'Moonlight Sonata|Beethoven|C# Minor',
    'Clair de Lune|Debussy|C# Minor',
    'Add|Sonata No.2|Chopin|B Minor',
    'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
    'Add|Fur Elise|Beethoven|C# Minor',
    'Remove|Clair de Lune',
    'ChangeKey|Moonlight Sonata|C# Major',
    'Stop'
]
)