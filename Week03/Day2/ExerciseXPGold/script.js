/*
 * Exercice 1
 */

let me = ["my","favorite","color","is","blue"];
console.log(me.join(" "));

/*
 * Exercice 2
 */

let str1 = "mix";
let str2 = "pod";

temp = str1;

str1 = str2.slice(0, 2) + str1.slice(2);
str2 = temp.slice(0, 2) + str2.slice(2);


let str3 = str1 + " " + str2;
console.log(str3);

/*
 * Exercice 3. Calculator
 */

let num1 = Number(prompt("Give me the first number"));
let num2 = Number(prompt("Give me the Second number"));
let operation = prompt("What kind of operation we gonna do (+ - * /)?");
switch (operation){
    case '+':
        alert(`${num1} + ${num2} = ${num1 + num2}`);
        break;
    case '-':
        alert(`${num1} - ${num2} = ${num1 - num2}`);
        break;
    case '*':
        alert(`${num1} * ${num2} = ${num1 * num2}`);
            break;
    case '/':
        if (num2 !=0){ // When num2 is zero it just slide down to 'Illegal operation' message
            alert(`${num1} / ${num2} = ${num1 / num2}`);
            break;
            }
    default:
        alert(`Illegal operation`);
}
