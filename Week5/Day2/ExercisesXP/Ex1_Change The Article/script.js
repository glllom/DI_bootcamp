//prints text in console
let h1_someFacts = document.querySelector("h1").firstChild;
console.log(h1_someFacts.textContent);

//removes last paragraph
articleLastParagraph = document.querySelector("article :last-child");
document.querySelector("article").removeChild(articleLastParagraph);

// sets background red
document.getElementsByTagName("h2")[0].addEventListener("click",function() {
    document.getElementsByTagName("h2")[0].setAttribute("style", "background-color: red;");
});

// removes h3 
document.getElementsByTagName("h3")[0].addEventListener("click",function() {
    document.getElementsByTagName("h3")[0].setAttribute("style", "display: none;");
});

//adds button and changes text to bold
buttonBold = document.createElement("button");
buttonBold.textContent = "Bold"
buttonBold.addEventListener("click", allParagraphsToBold);
document.body.appendChild(buttonBold);

function allParagraphsToBold(){
    for (p of document.querySelectorAll('p')){
        p.setAttribute("style", "font-weight: bold;")
    }
}

//Bonus. Increase font size;
document.getElementsByTagName("h1")[0].addEventListener("mouseover",function() {
    document.getElementsByTagName("h1")[0]
    .setAttribute("style", `font-size: ${Math.floor(Math.random() * 101)}px;`);
});

//Bonus. Fades out
document.querySelectorAll('p')[1].addEventListener("mouseover",function() {
    document.getElementsByTagName("p")[1]
    .setAttribute("style", "opacity: 0.2;");
});

document.querySelectorAll('p')[1].addEventListener("mouseout",function() {
    document.getElementsByTagName("p")[1]
    .setAttribute("style", "opacity: 1;");
});