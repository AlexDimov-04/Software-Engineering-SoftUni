function names(namesArr) {
    namesArr.sort((a, b) => a.localeCompare(b));

    for (let index = 0; index < namesArr.length; index++) {
        console.log(`${index + 1}.${namesArr[index]}`);
    }
}

