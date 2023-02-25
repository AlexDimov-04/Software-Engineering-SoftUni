function sumDigits(number) {
    let numbers = number.toString().split('');
    console.log(numbers.reduce((total, num) => total + Number(num), 0));
}
