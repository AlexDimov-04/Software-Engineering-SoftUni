function wordTracker(words) {
    let targetWords = words.shift().split(' ');
    let wordsCounter = {};

    targetWords.forEach(w => {
        wordsCounter[w] = 0;
    });

    for (const word of words) {
        if (wordsCounter.hasOwnProperty(word)) {
            wordsCounter[word] += 1;
        }
    }

    for (const [word, count] of Object.entries(wordsCounter).sort((a, b) => b[1] - a[1])) {
        console.log(`${word} - ${count}`);
    }
}