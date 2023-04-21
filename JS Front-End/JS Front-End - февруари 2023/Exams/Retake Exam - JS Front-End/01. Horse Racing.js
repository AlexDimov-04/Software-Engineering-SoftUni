function horseRacing(array) {
    const horses = [];
    const commandParser = {
        'Retake': retake,
        'Trouble': trouble,
        'Rage': rage,
        'Miracle': miracle
    };

    for (const line of array) {
        if (line.includes('|')) {
            let names = line.split('|');

            names.forEach(horseName => {
                horses.push(horseName);
            });
        } else {
            break;
        }
    }

    for (const line of array) {
        if (line === 'Finish') {
            break;
        }
        else if (!line.includes('|')) {
            let command = line.split(' ');
            commandParser[command[0]](...command.slice(1));
        }
    }

    printOutput();

    function retake(overtakingHorse, overtakenHorse) {
        const indexOvertakingHorse = horses.indexOf(overtakingHorse);
        const indexOvertakenHorse = horses.indexOf(overtakenHorse);

        if (indexOvertakingHorse < indexOvertakenHorse) {
            horses[indexOvertakenHorse] = overtakingHorse;
            horses[indexOvertakingHorse] = overtakenHorse;

            console.log(`${overtakingHorse} retakes ${overtakenHorse}.`);
        }
    }

    function trouble(horseName) {
        if (horses.indexOf(horseName) > 0) {
            let indexOfGivenHorse = horses.indexOf(horseName);
            let indexOfPreviousHorse = indexOfGivenHorse - 1;
            let nameOfPreviousHorse = horses[indexOfPreviousHorse];

            horses[indexOfPreviousHorse] = horseName;
            horses[indexOfGivenHorse] = nameOfPreviousHorse;

            console.log(`Trouble for ${horseName} - drops one position.`);
        }
    }

    function rage(horseName) {
        let indexOfGivenHorse = horses.indexOf(horseName);

        if (horses.indexOf(horseName) === horses.length - 1) {
            console.log(`${horseName} rages 2 positions ahead.`)
        }
        else if (horses.indexOf(horseName) === horses.length - 2) {
            horses.splice(indexOfGivenHorse, 1);
            horses.push(horseName);
            console.log(`${horseName} rages 2 positions ahead.`)
        } else {
            let indexToMove = indexOfGivenHorse + 2;
            
            if (indexOfGivenHorse === 0) {
                horses.shift();
                horses.splice(indexToMove, 0, horseName);
            } else {
                horses.splice(indexOfGivenHorse, 1);
                horses.splice(indexToMove, 0, horseName);
            }
            console.log(`${horseName} rages 2 positions ahead.`)
        }
    }

    function miracle() {
        let nameOfLastHorse = horses.shift();
        horses.push(nameOfLastHorse);

        console.log(`What a miracle - ${horses[horses.length - 1]} becomes first.`);
    }

    function printOutput() {
        console.log(horses.join('->'))
        console.log(`The winner is: ${horses[horses.length - 1]}`);
    }
}

horseRacing(['Onyx|Domino|Sugar|Fiona',
'Rage Sugar',
'Finish'])








