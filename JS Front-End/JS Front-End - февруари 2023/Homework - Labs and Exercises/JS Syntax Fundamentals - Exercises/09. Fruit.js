function grocery(fruit, grams, kilogramsPrice) {
    console.log(`I need $${((grams / 1000) * kilogramsPrice).toFixed(2)} to buy ${(grams / 1000).toFixed(2)} kilograms ${fruit}.`);
}

