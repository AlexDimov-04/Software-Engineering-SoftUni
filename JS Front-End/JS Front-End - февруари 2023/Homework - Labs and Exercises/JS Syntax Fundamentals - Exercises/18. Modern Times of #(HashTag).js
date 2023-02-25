function solve(text) {
    let textArr = text.split(' ');
    let foundNum = false;
    let output = [];

    for (const word of textArr) {
        if (word[0] === '#' && word.length > 1) {
            for (const ch of word) {
                if (!isNaN(ch)) {
                    foundNum = true;
                    break;
                }  
            }

            if (foundNum) {
                foundNum = false;
                continue;
            } else {
                output.push(word.slice(1, word.length));
            }

        }
        
    }

    console.log(output.join('\n'))
}