/*
 * Exercice 1. The World Translator
 */
language = prompt("Witch language do you speak?");
switch (language.toLowerCase()) {
    case "french":
        alert("Bonjour");
        break;
    case "english":
        alert("Hello");
        break;
    case "hebrew":
        alert("Shalom");
        break;
    default:
        alert("01110011 01101111 01110010 01110010 01111001");
}


/*
 * Exercice 2. The Grade Assigner
 */
grade = prompt("Give me your grade");

if (grade < 70)
    console.log("D");
else if (grade <= 80)
    console.log("C");
else if (grade <= 90)
    console.log("B");
else
    console.log("A");

/*
 * Exercice 3
 */

str = prompt("Give me a string. It must be a verb.");

if (str.length >= 3) {
    if (str.indexOf("ing") > 0)
        console.log(str + "ly");
    else
        console.log(str + "ing");
}
else
    console.log(str);
