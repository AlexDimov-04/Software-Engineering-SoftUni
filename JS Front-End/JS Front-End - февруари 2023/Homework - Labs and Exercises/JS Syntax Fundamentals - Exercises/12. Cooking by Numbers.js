function cookingByNumbers(num, op1, op2, op3, op4, op5) {
    num = Number(num);
    const operations = {
        chop: (n) => n / 2,
        dice: (n) => Math.sqrt(n),
        spice: (n) => n + 1,
        bake: (n) => n * 3,
        fillet: (n) => n * 0.8,
    };

    [op1, op2, op3, op4, op5].forEach((op) => {
        num = operations[op](num);
        console.log(num);
    });
}