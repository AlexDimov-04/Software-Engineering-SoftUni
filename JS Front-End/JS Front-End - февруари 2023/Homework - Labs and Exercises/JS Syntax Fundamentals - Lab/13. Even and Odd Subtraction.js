function solve(arr) {
    let evenSum = 0;
    let oddSum = 0;

    for (let index = 0; index < arr.length; index++) {
        if (arr[index] % 2 === 0) {
            evenSum += arr[index]
        } else {
            oddSum += arr[index]
        }
    }

    console.log(`${evenSum - oddSum}`)
}