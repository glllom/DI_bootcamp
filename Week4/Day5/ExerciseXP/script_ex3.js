function action(){
    let myDiv = document.querySelector("div");
    myDiv.setAttribute("style", "background-color: lightblue;")
    let names = document.getElementsByTagName("li");
    names[0].setAttribute("hidden", "true");
    names[1].setAttribute("style", "border: 2px solid;");
    document.querySelector("body").setAttribute("style", "font-size: larger;")
    // console.log(document.querySelector("body"));
}

