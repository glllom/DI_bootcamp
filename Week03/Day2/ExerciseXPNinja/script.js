/*
 * Exercice 1. Evalution
 */

console.log(5 >= 1);
// Prediction: It will output true, because 5 > 1
// Actual: true

console.log(0 === 1);
// Prediction: It will output false, because 0 is not equal to 1
// Actual: false

console.log( 4 <= 1);
// Prediction: It will output false, because 4 is not less than 1
// Actual: false

console.log(1 != 1);
// Prediction: It will output false, because 1 = 1
// Actual: false

console.log("A" > "B");
// Prediction: It will output false, because ASCII "A" less than ASCII "B"
// Actual: false

console.log("B" < "C");
// Prediction: It will output true, because ASCII "B" less than ASCII "C"
// Actual: true
    
console.log("a" > "A");
// Prediction: It will output true, because ASCII "a" greater than ASCII "A"
// Actual: true

console.log("b" < "A");
// Prediction: It will output false, because ASCII "b" greater than ASCII "A"
// Actual: false

console.log(true === false);
// Prediction: It will output false, because true is not false
// Actual: false

console.log(true != true);
// Prediction: It will output false, because true equals to true
// Actual: false
    
   
    
    
    

/*
 * Exercice 2. Ask For Numbers
 */
str = prompt("Give me the numbers separated by commas");
arr = str.split(',');
let sum = 0;
for (let i=0; i < arr.length; i++)
    sum += Number(arr[i]);
console.log(sum);


/*
 * Exercice 3. Find Nemo
 */
str = prompt("Give me a sentence containing the word “Nemo”");
arr = str.split(/(?:,| )+/)
for (let i = 0; i < arr.length; i++)
    if (arr[i] == "Nemo"){
        console.log("I found Nemo at " + i);
        break;
        }

/*
 * Exercice 4. Boom
 */

let boom = ["B","o","o","m"];
let num = prompt("Give me the number");
if (num > 2)
    for (let i = 2; i < num; i++)
        boom.splice(1,0,"o");


if (num % 2 == 0)
    boom.push("!");

let result = boom.join("");

if  (num % 5 == 0)
        result = result.toUpperCase();

console.log(result);