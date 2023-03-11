function inventory(array) {
    let heroes = [];

    for (const data of array) {
        let [hero, level, ...items] = data.split(' / ');
        
        let currentHero = {
            'hero': hero,
            'level': level,
            'items': items.join(', ')
        };

        heroes.push(currentHero);
    }

    heroes.sort((a, b) => a.level - b.level);

    for (const obj of heroes) {
        console.log(`Hero: ${obj.hero}`);
        console.log(`level => ${Number(obj.level)}`);
        console.log(`items => ${obj.items}`);
    }
}