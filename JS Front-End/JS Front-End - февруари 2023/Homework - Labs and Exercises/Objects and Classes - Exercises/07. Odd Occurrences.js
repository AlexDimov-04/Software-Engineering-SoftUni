function oddOccurrences(string) {
    function Counter(array) {
        let count = {};
        let output = [];

        array.forEach(el => {
            el = el.toLowerCase();
            count[el] = (count[el] || 0) + 1;
        });

        for (const [key, value] of Object.entries(count)) {
            if (value % 2 !== 0) {
                output.push(key);
            }
        }

        console.log(...output);
    }

    Counter(string.split(' '));
}