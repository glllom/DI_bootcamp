let sentence = prompt("Give me the sentence");

//Option 1
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");;

if (wordBad > (wordNot + 3))
    console.log(sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad + 3, sentence.length));
else
    console.log(sentence);

//Option 2
console.log(sentence.replace(/not(.)+bad/, "good"));

