function nums(number) {
    let numbers = number.toString().split('');
    let sameNumbers = true;

    for (let index = 0; index < numbers.length - 1; index++) {
        if (numbers[index] !== numbers[index + 1]) {
            sameNumbers = false;
            break;
        }
    }

    console.log(sameNumbers)
    console.log(numbers.reduce((total, num) => total + Number(num), 0));
}