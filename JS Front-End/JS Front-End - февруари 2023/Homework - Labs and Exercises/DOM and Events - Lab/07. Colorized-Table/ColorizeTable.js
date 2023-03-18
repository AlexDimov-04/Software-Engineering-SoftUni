function colorize() {
    const tableRows = Array.from(document.querySelectorAll('table tr:nth-child(even)'));
    tableRows.map((tr) => tr.style.backgroundColor = 'Teal');
}