function ex_1(){
    let myDiv = document.getElementById("navBar");
    myDiv.setAttribute("id","socialNetworkNavigation");
    let newli = document.createElement("li");
    newli.innerHTML = '<a href="#">Logout</a>';
    myDiv.firstElementChild.appendChild(newli);
}

function ex_2(){
    let myLi = document.querySelector("#container+ul :last-child");
    myLi.textContent = "Richard";
    let liToMyName = document.querySelectorAll(".list :first-child");
    liToMyName.forEach(li => li.textContent = "Gleb")
    }

