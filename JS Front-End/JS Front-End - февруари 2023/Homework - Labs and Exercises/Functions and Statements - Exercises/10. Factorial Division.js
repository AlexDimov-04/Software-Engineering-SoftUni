function factorialDivision(num1, num2) {
    function factorial(n) {
        if (n === 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    const result = (factorial(num1) / factorial(num2)).toFixed(2);
    console.log(result);
}