/*
 * Exercise 1 : List Of People
 */
let people = ["Greg", "Mary", "Devon", "James"];

people.shift();
people.splice(people.length-1,1,"Jason");
people.push("Gleb");
console.log(people);
console.log(people.indexOf("Mary"));





