function perfectNumber(n) {
    let sum = 0;

    for (let index = 1; index <= n / 2; index++) {
        if (n % index === 0) {
            sum += index;
        } 
    }

    sum === n ? console.log("We have a perfect number!") : console.log("It's not so perfect.");
}
