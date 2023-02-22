function solve(text, word) {
    text = text.split(' ');
    let counter = 0;

    for (const el of text) {
        if (el === word) {
            counter++;
        }
    }

    console.log(counter);
}
