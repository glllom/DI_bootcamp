newOption = document.createElement("option");
newOption.innerText = "Classic";
newOption.setAttribute("value", "classic");
newOption.setAttribute("selected", true);
document.querySelectorAll('option').forEach(element => {
    element.removeAttribute("selected");});
document.querySelector('select').appendChild(newOption)

function show(event){
    document.querySelector("h1").innerText = event.target.value;
    console.log(event.target);
    
}