function orders(product, quantity) {
    let products = {
        'coffee': 1.50 * quantity,
        'water': 1.00 * quantity,
        'coke': 1.40 * quantity,
        'snacks': 2.00 * quantity
    };

    console.log(products[product].toFixed(2));
}
