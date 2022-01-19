let words = prompt("Give me some words separated by comma.")
            .split(",")
            .map(word => word.trim()); //receive sentence and make an array from words
console.log(words);
let longestWord = 0;
words.forEach((word, ind) => {
    console.log(word);
    console.log(ind)
    console.log(longestWord);
    longestWord = Math.max(longestWord, word.length)}); // find the longest word in array.
let stars = '*'.repeat(longestWord+4);// create string of stars according the longest word.
words = words.map(word => word + (new Array(longestWord - word.length)
            .fill(' ')
            .join(''))); // add spaces for each word 

console.log(stars);
words.forEach(word => {console.log('* '+ word + ' *');});
console.log(stars);