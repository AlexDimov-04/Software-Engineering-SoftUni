function matrix(n) {
    let matrix = new Array(n).fill(new Array(n).fill(n));

    matrix.forEach(arr => {
        console.log(arr.join(' '));
    });
}

// function matrix(n) {
//     for (let r = 0; r < n; r++) {
//         let row = '';
//         for (let c = 0; c < n; c++) {
//             row += n + ' ';
//         } 
//         console.log(row);
//     }
// }
