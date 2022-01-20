function getWord(){
    return prompt("Player 1. Give me a word by minimum eight letters, please.").toLowerCase().trim().split("");
}

function getLetter(){
    let letter = prompt("Player 2. Guess a letter, please.").trim().toLowerCase();
    while(!/[a-z]/.test(letter) || letter.length>1){
        letter = prompt("Incorrect input. Guess a letter, please.").trim().toLowerCase();
    }
    return letter;
}

function printWord(word){
    console.log(word.map(item => item[1] ? item[0]: "*" ).join(""));
}

function printUsedLetters(usedLetters){
    console.log(`You tried: ${usedLetters.join(', ')}`);
}

function guessLetter(word, letter){
    let success = false;
    word.forEach(element => {
        if (element[0] == letter){
            element[1] = true;
            success = true;
            }
    });
    return success;
}

function wordIsGuessed(word){
    return word.map(item => item[1]).reduce(function(a,b){return a && b;});
}

let word, usedLetters = [], letter;
let tries = 10, wordMinimumLength = 8;
do{
    if(word)
      alert("The word is too short.")  
    word = getWord();
}
while (word.length < wordMinimumLength);
word = word.map(letter => [letter,false]);

console.log("Player2. let's play!")
while(tries > 0){
    printWord(word);
    if (usedLetters.length > 0)
        printUsedLetters(usedLetters);
    console.log(`You have ${tries} tries more.`)
    letter = getLetter();
    while (usedLetters.includes(letter)){
        console.log(`You already used letter "${letter}". Try again`)
        letter = getLetter();
    }
    usedLetters.push(letter);
    if (guessLetter(word, letter)){
        if (wordIsGuessed(word)){
            printWord(word);
            console.log("CONGRATS!!! YOU WIN");
            break;
        }
    }
    else{
        if (!--tries){
            printWord(word);
            console.log("YOU LOSE");
            printHangman();
        }
    }
}

function printHangman(){
    console.log("   +-----+");
    console.log("   |     | ");
    console.log("   0     | ");
    console.log("  /|\\    | ");
    console.log("  / \\    | ");
    console.log("         | ");
    console.log("===========");
}
