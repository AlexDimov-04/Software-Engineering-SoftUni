function rotation(arr, num) {
    for (let index = 1; index <= num; index++) {
        arr.push(arr.shift());
    }

    console.log(arr.join(' '));
}
