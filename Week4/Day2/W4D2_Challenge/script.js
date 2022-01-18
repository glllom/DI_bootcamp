let words = prompt("Give me some words separated by comma.").split(",").map(word => {return word.trim()}); //receive sentence and make an array from words
let longestWord = 0;
words.forEach(word => {longestWord = Math.max(longestWord, word.length)}); // find the longest word in array.
let stars = (new Array(longestWord+4)).fill('*').join(''); // create string of stars according the longest word.
words = words.map(word => {return word + (new Array(longestWord - word.length).fill(' ').join(''))}); // add spaces for each word 

console.log(stars);
words.forEach(word => {console.log('* '+ word + ' *');});
console.log(stars);