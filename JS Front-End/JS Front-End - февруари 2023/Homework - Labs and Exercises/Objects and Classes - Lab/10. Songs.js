function solve(arr) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    let songs = [];
    arr.shift();
    let typeSong = arr.pop();

    for (const line of arr) {
        let [typeList, name, time] = line.split('_');
        let song = new Song(typeList, name, time);
        songs.push(song);
    }

    if (typeSong === 'all') {
        songs.forEach((s) => console.log(s.name));
    } else {
        let filtered = songs.filter((s) => s.typeList === typeSong);
        filtered.forEach((i) => console.log(i.name));
    }

}