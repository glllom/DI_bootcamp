function action(){
    let myDiv = document.querySelector("div");
    myDiv.setAttribute("style", "background-color: lightblue; padding: 10px;")
    let names = document.getElementsByTagName("li");
    names[0].setAttribute("hidden", "true");
    names[1].setAttribute("style", "border: 2px solid;");
    document.querySelector("body").setAttribute("style", "font-size: larger;")
    if(myDiv.getAttribute("style") == "background-color: lightblue;"){
        alert(`Hello ${names[0].textContent} and ${names[1].textContent}.`);
    }

}

