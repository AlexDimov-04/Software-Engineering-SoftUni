function oddAndEvenSum(num) {
    let stringNum = String(num);
    let oddSum = 0;
    let evenSum = 0;

    for (const n of stringNum) {
        if (Number(n) % 2 === 0) {
            evenSum += Number(n);
        } else {
            oddSum += Number(n);
        }
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}