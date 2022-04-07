/*
 * Exercice 1. Age Difference
 */

yearOfBirth1 = prompt("Give me the year of birth of the first person");
yearOfBirth2 = prompt("Give me the year of birth of the second person");

if (yearOfBirth1 < yearOfBirth2)
    console.log(`First person will be older twice the age of the second in ${2 * yearOfBirth2 - yearOfBirth1}`);
else if (yearOfBirth1 > yearOfBirth2)
    console.log(`Second person will be older twice the age of the first in ${2 * yearOfBirth1 - yearOfBirth2}`);
else
    console.log(`They are same age.`);

/*
 * Exercice 2. Zip Codes
 */

zipCode = prompt("Give me your zip code, please.");
if (/^\d{5}$/.test(zipCode))
    console.log("success");
else
    console.log("error");


/*
 * Exercice 3. Secret Word
 */
word = prompt("Give me your secret word, please.");
console.log(word.replace(/[aeiou]/g,""));
code = {
    "a": "1",
    "e": "2",
    "i": "3",
    "o": "4",
    "u": "5"}

console.log(word.replace(/[aeiou]/g, vowel => code[vowel]));
