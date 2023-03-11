function movies(array) {
    let moviesData = {};

    for (const command of array) {
        if (command.includes('addMovie')) {
            let movie = command.split('addMovie ')[1];
            moviesData[movie] = {};
            moviesData[movie].name = movie;
        } 
        else if (command.includes('directedBy')) {
            let [movie, director] = command.split(' directedBy ');
            if (moviesData.hasOwnProperty(movie)) {
                moviesData[movie].director = director;
            }
        }
        else if (command.includes('onDate')) {
            let [movie, date] = command.split(' onDate ');
            if (moviesData.hasOwnProperty(movie)) {
                moviesData[movie].date = date;
            } 
        }
    }

    for (const value of Object.values(moviesData)) {
        if (Object.keys(value).length === 3) {
            console.log(JSON.stringify(value));
        }
    }
}

