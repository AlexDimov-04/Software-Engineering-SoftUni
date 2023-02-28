function perfectNumber(n) {
    let halfNum = n / 2;
    let sum = 0;

    for (let index = 1; index <= halfNum; index++) {
        if (n % index === 0) {
            sum += index;
        } 
    }

    if (sum === n) {
        console.log("We have a perfect number!");
    } else {
        console.log("It's not so perfect.");
    }
}