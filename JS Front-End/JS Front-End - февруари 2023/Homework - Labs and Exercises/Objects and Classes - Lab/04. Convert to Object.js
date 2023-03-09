function convertToObject(string) {
    let object = JSON.parse(string);

    for (const [key, value] of Object.entries(object)) {
        console.log(`${key}: ${value}`);
    }
}