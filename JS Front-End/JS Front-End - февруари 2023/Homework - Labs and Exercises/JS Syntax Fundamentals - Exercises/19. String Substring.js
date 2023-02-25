function substring(word, text) {
    text = text.split(' ')
    let founded = false;

    for (const w of text) {
        if (word.toLowerCase() === w.toLowerCase()) {
            console.log(word)
            founded = true;
        }
    }

    if (!founded) {
        console.log(`${word} not found!`)
    }
}
