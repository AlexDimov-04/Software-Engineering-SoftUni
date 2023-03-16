function calc() {
    const firstNum = document.getElementById('num1');
    const secondNum = document.getElementById('num2');
    const totalSum = document.getElementById('sum');

    let number1 = Number(firstNum.value);
    let number2 = Number(secondNum.value);
    let sum = number1 + number2;

    totalSum.value = sum;
}
