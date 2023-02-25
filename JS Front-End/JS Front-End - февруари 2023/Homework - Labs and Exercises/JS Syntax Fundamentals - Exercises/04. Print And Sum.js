function sum(start, end) {
    let arr = [];

    for (let index = start; index <= end; index++) {
        arr.push(index);
    }

    console.log(arr.join(' '));
    console.log(`Sum: ${arr.reduce((total, num) => total + num, 0)}`);
}

