function phoneBook(arr) {
    let people = {};

   for (const line of arr) {
    let [person, phone] = line.split(' ');
    people[person] = phone;
   }

   for (const name in people) {
    console.log(`${name} -> ${people[name]}`);
   }
}