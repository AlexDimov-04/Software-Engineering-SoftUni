function cityTaxes(name, population, treasury) {
    let city = {
        name, population, treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += this.population * this.taxRate;
        },
        applyGrowth(percantage) {
            this.population += this.population * (percantage / 100);
        },
        applyRecession(percentage) {
            this.treasury -= this.treasury * (percentage / 100);
        }
    }

    return city;
}
