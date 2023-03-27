function attachEvents() {
    const input = document.getElementById('location');
    const btn = document.getElementById('submit');
    const forecast = document.getElementById('forecast');
    const currentWeatherDiv = document.getElementById('current');
    const upcomingWeatherDiv = document.getElementById('upcoming');
    const BASE_URL = 'http://localhost:3030/jsonstore/forecaster/locations/';
    const TODAY_URL = 'http://localhost:3030/jsonstore/forecaster/today/';
    const UPCOMING_URL = 'http://localhost:3030/jsonstore/forecaster/upcoming/';
    let code;
    let icons = {
        'Sunny': '☀',
        'Partly sunny': '⛅',
        'Overcast': '☁',
        'Rain': '☂'
    };

    btn.addEventListener('click', () => {
        fetch(BASE_URL)
            .then(res => res.json())
            .then(data => {
                for (const line of data) {
                    if (input.value === line['name']) {
                        code = line['code'];
                    }
                }

                fetch(TODAY_URL + code)
                    .then(res => res.json())
                    .then(data => {
                        forecast.style.display = 'block';

                        const forecasts = document.createElement('div');
                        forecasts.classList.add('forecasts');

                        const symbol = document.createElement('span');
                        symbol.classList.add('condition');
                        symbol.classList.add('symbol');

                        const condition = document.createElement('span');
                        condition.classList.add('condition');

                        const location = document.createElement('span');
                        location.classList.add('forecast-data');

                        const temprature = document.createElement('span');
                        temprature.classList.add('forecast-data');

                        const conditionForecast = document.createElement('span');
                        conditionForecast.classList.add('forecast-data');

                        location.textContent = data.name;
                        temprature.textContent = `${data['forecast']['low']}°/${data['forecast']['high']}°`
                        conditionForecast.textContent = data['forecast']['condition'];
                        symbol.textContent = icons[conditionForecast.textContent];

                        condition.appendChild(location);
                        condition.appendChild(temprature);
                        condition.appendChild(conditionForecast);

                        forecasts.appendChild(symbol);
                        forecasts.appendChild(condition);

                        currentWeatherDiv.appendChild(forecasts);
                    });

                fetch(UPCOMING_URL + code)
                    .then(res => res.json())
                    .then(data => {
                        const forecastInfo = document.createElement('div');
                        forecastInfo.classList.add('forecast-info');
                        upcomingWeatherDiv.appendChild(forecastInfo);

                        for (const line of data.forecast) {
                            const upcoming = document.createElement('span');
                            upcoming.classList.add('upcoming');

                            upcoming.innerHTML += `
                                <span class="symbol">${icons[line.condition]}</span>
                                <span class="forecast-data">${line.low}°/${line.high}°</span>
                                <span class="forecast-data">${line.condition}</span>
                            `;

                            forecastInfo.appendChild(upcoming);
                        }
                    })
            })
            .catch(err => {
                forecast.textContent = 'Error';
            })
    })
}

attachEvents();