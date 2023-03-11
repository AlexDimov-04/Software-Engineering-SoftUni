function storeProvision(stock, products) {
    let provisions = {};

    for (let index = 0; index < stock.length; index += 2) {
        provisions[stock[index]] = Number(stock[index + 1]);
    }

    for (let index = 0; index < products.length; index += 2) {
        if (!provisions.hasOwnProperty(products[index])) {
            provisions[products[index]] = Number(products[index + 1]);
        } else {
            provisions[products[index]] += Number(products[index + 1]);
        }
    }

    for (const [product, quantity] of Object.entries(provisions)) {
        console.log(`${product} -> ${quantity}`);
    }
}
