/*
 * Exercise 1: Random Number
 */
let randomNumber = Math.ceil(Math.random() * 100);
let arr = [];
for (let i=0; i<=randomNumber; i++)
    if (i % 2 == 0)
        arr.push(i);
console.log(arr);

/*
 * Exercise 2: Capitalized Letters
 */
function capitalize(string){
    let arr = ["",""];
    for (i in string)
    if (i % 2 == 0){
        arr[0] += string[i].toUpperCase();
        arr[1] += string[i].toLowerCase();
    }
    else{
        arr[0] += string[i].toLowerCase();
        arr[1] += string[i].toUpperCase();
    }
    return arr;
}
console.log(capitalize("abcdef"));

/*
 * Exercise 3 : Is Palindrome?
 */
function isPalindrome(string){
    let arr = [];
    for (char of string)
        if (/[a-z]|[A-Z]/.test(char))
            arr.push(char.toLowerCase());
    for (let i=0; i<=arr.length/2; i++)
        if (arr[i] != arr[arr.length-1-i])
            return false;
    return true;
}

console.log(isPalindrome("Was it a car or a cat I saw?"));

/*
 * Exercise 4 : Biggest Number
 */
function biggestNumberInArray(arrayNumber) {
    let biggestNumber = 0;
    arrayNumber.forEach(num => {biggestNumber = Math.max(biggestNumber, num)});
    return biggestNumber;
}

console.log(biggestNumberInArray(['a', 3, 4, 2]));