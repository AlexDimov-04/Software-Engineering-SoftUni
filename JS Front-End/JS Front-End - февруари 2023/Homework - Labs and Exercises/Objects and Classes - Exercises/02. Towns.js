function towns(arr) {
    let townsData = [];

    for (const line of arr) {
        let [town, latitude, longitude] = line.split(' | ');
        
        const currentTown = {
            town: town,
            latitude: parseFloat(latitude).toFixed(2),
            longitude: parseFloat(longitude).toFixed(2)
        }

        townsData.push(currentTown);
    }

    townsData.forEach(t => {
        console.log(t);
    });
}