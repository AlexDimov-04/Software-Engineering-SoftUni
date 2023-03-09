function meetings(arr) {
    let meetingsSchedule = {};

    for (const line of arr) {
        let [day, name] = line.split(' ');

        if (!meetingsSchedule.hasOwnProperty(day)) {
            meetingsSchedule[day] = name;
            console.log(`Scheduled for ${day}`);
        } else {
            console.log(`Conflict on ${day}!`);
        }
    }

    for (const day in meetingsSchedule) {
        console.log(`${day} -> ${meetingsSchedule[day]}`);
    }
}