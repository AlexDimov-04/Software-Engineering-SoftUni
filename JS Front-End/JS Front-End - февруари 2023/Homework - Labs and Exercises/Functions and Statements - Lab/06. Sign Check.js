function checkSign(num1, num2, num3) {
    let counterNegative = 0;

    if (num1 < 0) {
        counterNegative += 1;
    }
    if (num2 < 0) {
        counterNegative += 1;
    }
    if (num3 < 0) {
        counterNegative += 1;
    }

    return counterNegative % 2 === 0 ? 'Positive' : 'Negative';
}