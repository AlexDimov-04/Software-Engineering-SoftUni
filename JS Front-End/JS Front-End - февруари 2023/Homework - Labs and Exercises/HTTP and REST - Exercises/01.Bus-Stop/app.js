function getInfo() {
    const stopID = document.getElementById('stopId');
    const stopNameDiv = document.getElementById('stopName');
    const busesContainer = document.getElementById('buses');
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/businfo/';
    const stopIdValue = stopID.value;

    busesContainer.textContent = '';
    fetch(`${BASE_URL}${stopIdValue}`)
        .then(res => res.json())
        .then(data => {
            const { name, buses } = data;
            stopNameDiv.textContent = name;

            for (const busId in buses) {
                const li = document.createElement('li');
                li.textContent = `"Bus ${busId} arrives in ${buses[busId]} minutes"`;
                busesContainer.appendChild(li);
            }
        })
        .catch(err => {
            stopNameDiv.textContent = 'Error';
        })
}