function sumTable() {
    const tds = Array.from(document.querySelectorAll('tr:not(:last-child) td:nth-child(even)'));
    const total = document.getElementById('sum');
    let sums = [];

    tds.forEach(td => {
        sums.push(Number(td.innerHTML));
    });

    let totalSum = sums.reduce((a, b) => {
        return a + b;
    })

    total.textContent = totalSum;
}