function charactersInRange(chr1, chr2) {
    let startCode = chr1.charCodeAt(0);
    let endCode = chr2.charCodeAt(0);

    if (startCode > endCode) {
        [startCode, endCode] = [endCode, startCode];
    }

    let result = [];
    for (let index = startCode + 1; index < endCode; index++) {
        result.push(String.fromCharCode(index));  
    }

    console.log(result.join(' '));
}