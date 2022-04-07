/*
 * Exercise 1 : Is_Blank
 */
function isBlank(string){
    return string.trim() == "";
}

console.log(isBlank(prompt("Give me a string.")));

/*
 * Exercise 2 : Abbrev_name
 */
function abbrevName(string){
    let arr = string.split(" ");
    arr[arr.length-1] = arr[arr.length-1][0]+(".")
    return arr.join(' ');

}
console.log(abbrevName(prompt("Give me a name.")));

/*
 * Exercise 3 : SwapCase
 */
function swapCase(string){
    let newString = ""
    for (letter of string){
        if (/[A-Z]/.test(letter))
            newString += letter.toLowerCase();
        else
            newString += letter.toUpperCase();
    }
return newString;
}
console.log(swapCase(prompt("Give me a string.")));

/*
 * Exercise 4 : Omnipresent Value
 */

function isOmnipresent(mainArray, valueToTest){
    let result = true;
    for (element of mainArray){
        result = result && element.includes(valueToTest);
    }
    return result;
}
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1));


