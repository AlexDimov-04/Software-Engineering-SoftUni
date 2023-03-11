function dictionary(array) {
    let terms = {};

    for (const line of array) {
        let term = JSON.parse(line);      
        for (const key in term) {
            terms[key] = term[key];
        }
    }

    for (const [key, value] of Object.entries(terms).sort()) {
        console.log(`Term: ${key} => Definition: ${value}`)
    }
}