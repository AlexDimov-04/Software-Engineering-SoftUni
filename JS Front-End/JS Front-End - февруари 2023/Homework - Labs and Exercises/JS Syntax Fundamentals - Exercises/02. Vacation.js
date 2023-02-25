function vacaction(people, group, day) {
    let totalPrice;

    switch (day) {
        case "Friday":
            if (group === "Students") {
                totalPrice = 8.45 * people;
            }
            else if (group === "Business") {
                if (people >= 100) {
                    people -= 10;
                }
                totalPrice = 10.90 * people;
            }
            else if (group === "Regular") {
                totalPrice = 15 * people;
            }
            break;

        case "Saturday":
            if (group === "Students") {
                totalPrice = 9.80 * people;
            }
            else if (group === "Business") {
                if (people >= 100) {
                    people -= 10;
                }
                totalPrice = 15.60 * people;
            }
            else if (group === "Regular") {
                totalPrice = 20 * people;
            }
            break;

        case "Sunday":
            if (group === "Students") {
                totalPrice = 10.46 * people;
            }
            else if (group === "Business") {
                if (people >= 100) {
                    people -= 10;
                }
                totalPrice = 16 * people;
            }
            else if (group === "Regular") {
                totalPrice = 22.50 * people;
            }
            break;
    }

    if (group === "Students" && people >= 30) {
        totalPrice -= totalPrice * 0.15;
    }

    else if (group === "Regular" && people >= 10 && people <= 20) {
        totalPrice -= totalPrice * 0.05
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`)
}
