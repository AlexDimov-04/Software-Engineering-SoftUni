function calculator(num1, num2, operator) {
    let result = {
        'multiply': num1 * num2,
        'divide': num1 / num2,
        'add': num1 + num2,
        'subtract': num1 - num2
    };

    console.log(result[operator]);
}