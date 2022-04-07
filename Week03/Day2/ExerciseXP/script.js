/*
 * Exercice 1
 */

let favoriteFood = "lasagne";
let favoriteMeal = "dinner";

console.log(`I eat ${favoriteFood} every ${favoriteMeal}`);

/*
 * Exercice 2
 */

let watchedSeries = ["Black mirror", "Money heist", "The Big Bang Theory"];
let watchedSeriesLength = 2;
let myWatchedSeries = "money heist, and the big bang theory";

console.log(`I watched ${watchedSeriesLength} series : ${myWatchedSeries}`);

watchedSeries[2] = "Friends";
watchedSeries.push("Scrubs");
watchedSeries.splice(0,0,"Lucifer");
watchedSeries.splice(1,1);

console.log(watchedSeries[1][2]);
console.log(watchedSeries);

/*
 * Exercice 3
 */

let celcius = 100;
let fahrenheit = celcius * 9 / 5 + 32;

console.log(celcius + "°C is " + fahrenheit + "°F.");

/*
 * Exercice 4
 */

let c;
let a = 34;
let b = 21;

console.log(a + b) //first expression
// Prediction: It will output 55, because 'a' and 'b' are numbers 34 and 21.
// Actual: 55

a = 2;

console.log(a + b) //second expression
// Prediction: It will output 23, because 'a' and 'b' are numbers 2 and 21.
// Actual: 23


// 3) Value of 'c' is undefined

// 4) console.log(3 + 4 + '5');
//    Prediction: It will output string "75", because 3 and 4 are numbers and it equal to 7. In other hand, '5' is char
//                and 7 is concated with 5.
//    Actual: 75            

/*
 * Exercice 5
 */

console.log(typeof(15))
// Prediction: It will output integer, because 15 is integer number.
// Actual: number

console.log(typeof(5.5))
// Prediction: It will output float, because 5.5 is float number.
// Actual: number

console.log(typeof(NaN))
// Prediction: It will output object, because NaN is object.
// Actual: number

console.log(typeof("hello"))
// Prediction: It will output string, because "hello" is string.
// Actual: string

console.log(typeof(true))
// Prediction: boolean
// Actual: boolean

console.log(typeof(1 != 2))
// Prediction: It will output boolean, because "1 != 2" is boolean comparison.
// Actual: boolean

console.log("hamburger" + "s")
// Prediction: It will output "hamburgers", because "hamburger" and "s" are strings. 
// Actual: hamburgers

console.log("hamburgers" - "s")
// Prediction: It will output NaN, because "hamburger" and "s" are strings and it is impossible to make subtruction with them.
// Actual: NaN

console.log("1" + "3")
// Prediction: It will output "13", because "1" and "3" are strings. 
// Actual: 13

console.log("1" - "3")
// Prediction: It will output NaN, because "1" and "3" are strings and it is impossible to make subtruction with them.
// Actual: -2

console.log("johnny" + 5)
// Prediction: It will output "johny5", because "johny" is string. And it is possible to concat it with number. 
// Actual: johny5   

console.log("johnny" - 5)
// Prediction: It will output NaN, because "johny" is string. And it is impossible to make subtruction with it.
// Actual: NaN

console.log(99 * "hello")
// Prediction: It will output NaN, because "hello" is string and it is impossible to make multiplication with it.
// Actual: NaN

console.log(1 != 1)
// Prediction: It will output False, because 1 equal to 1 (surprised).
// Actual: false

console.log(1 == "1")
// Prediction: It will output True, because 1 equal to 1, and it doesn't care about the type
// Actual: true

console.log(1 === "1")
// Prediction: It will output False, because type of 1 is number, but type of "1" is string
// Actual: false


/*
 * Exercice 6
 */

console.log(5 + "34");
// Prediction:  It will output 534 because 34 is string.
// Actual: 534

console.log(5 - "4");
// Prediction: It will output 1 because it is impossible to make substraction with string, and it changhes the type to number 4
// Actual: 1

console.log(10 % 5);
// Prediction: It will output 0 becacuse 10 / 5 = 2 without any remainder
// Actual: 0

console.log(5 % 10);
// Prediction: It will output 5 because 5 / 10 = 0 with remainder 5
// Actual: 5

console.log("Java" + "Script");
// Prediction: It will output JavaScript because "Java" and "Script" are strings
// Actual: JavaScript

console.log(" " + " ");
// Prediction: It will output "  " because " " and " " are strings
// Actual: "  "

console.log(" " + 0);
// Prediction: It will output " 0" because " " is string and it is possible to concat it with number. 
// Actual: " 0"

console.log(true + true);
// Prediction: It will output true because true and true is true
// Actual: 2

console.log(true + false);
// Prediction: It will output false because true and false is false
// Actual: 1

console.log(false + true);
// Prediction: It will output false because false and true is false 
// Actual: 1 

console.log(false - true);
// Prediction: It will output NaN because false and true are booleans and it is impossible to make subtruction with them.
// Actual: -1

console.log(!true);
// Prediction: It will output false because  opposit of true is false
// Actual: false

console.log(3 - 4);
// Prediction: It will output -1 because it is arithmetic operation
// Actual: -1

console.log("Bob" - "bill");
// Prediction: It will output NaN because "Bob" and "bill" are strings and it is impossible to make subtruction with them.
// Actual: NaN