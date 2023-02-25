function solve(string) {
    let output = [];
    let words = '';
    let iteration = 0;

    for (const ch of string) {
        iteration += 1;

        if (ch === ch.toUpperCase() && iteration > 1) {
            words += ' ' + ch
        } else {
            words += ch 
        }
    }

    words = words.split(' ')
    console.log(words.join(', '))
}