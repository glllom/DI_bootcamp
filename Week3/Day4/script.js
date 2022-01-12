/*
 * Exercice 1
 */

let x = 5;
let y = 2;

if (x > y) {
    console.log("x is the biggest number");
}
else if (y > x) {
    console.log("y is the biggest number");
}
else {
    console.log("numbers are equals");
}

/*
 * Exercice 2
 */
let newDog = 'Chihuahua';

console.log(`Word "${newDog}" has ${newDog.length} letters.`);
console.log(newDog.toUpperCase(),newDog.toLowerCase());

if (newDog == 'Chihuahua'){
    console.log("I love Chihuahuas, it’s my favorite dog breed");
}
else {
    console.log("I dont care, I prefer cats");
}

/*
 * Exercice 3
 */
x = prompt("Give me the number");
if (x % 2 == 0)
    console.log("x is an even number");
else
    console.log("x is an odd number");

/*
 * Exercice 4
 */
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

switch (users.length){
    case 0:
        console.log("no one is online");
        break;
    case 1:
        console.log(`${users[0]} is online`);
        break;
    case 2:
        console.log(`${users[0]} and ${users[1]} are online`);
        break;
    default:
        console.log(`${users[0]}, ${users[1]} and ${users.length-2} more are online.`);
}
