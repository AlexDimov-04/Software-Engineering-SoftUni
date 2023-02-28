function palindromeIntegers(array) {
    for (const num of array) {
        if (String(num) === String(num).split('').reverse().join('')) {
            console.log('true');
        } else {
            console.log('false');
        }
    }
}