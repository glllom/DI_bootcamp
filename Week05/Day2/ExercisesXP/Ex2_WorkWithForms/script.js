let form = document.forms[0];
console.log(form);

console.log(document.getElementById("fname"));
console.log(document.getElementById("lname"));

console.log(form.elements.fname);
console.log(form.elements.lname);


form.addEventListener("submit", makeList);

function makeList(event) {
    firstName = form.elements.fname.value;
    lastName = form.elements.lname.value;
    if (firstName != "" && lastName != "") {
        ul = document.getElementsByClassName("usersAnswer")[0];
        fNameItem = document.createElement("li");
        fNameItem.innerText = firstName;
        lNameItem = document.createElement("li");
        lNameItem.innerText = lastName;
        ul.appendChild(fNameItem);
        ul.appendChild(lNameItem);
    }
    event.preventDefault();
}