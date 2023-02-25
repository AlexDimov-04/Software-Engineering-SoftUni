function elements(stringsArr, step) {
    let newArr = [];
    for (let index = 0; index < stringsArr.length; index += step) {
        newArr.push(stringsArr[index]);
    }

    return newArr;

} 