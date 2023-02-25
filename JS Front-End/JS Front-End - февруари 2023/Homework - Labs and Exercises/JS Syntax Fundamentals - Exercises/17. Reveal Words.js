function solve(words, string) {
    words = words.split(', ')
    strings = string.split(' ')

    for (let i = 0; i < strings.length; i++) {
        for (const word of words) {
            if (strings[i].includes('*') && strings[i].length === word.length) {
                strings[i] = word
            }
        }
    }

    console.log(strings.join(' '))
}

