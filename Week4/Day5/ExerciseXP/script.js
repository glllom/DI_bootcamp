function ex_1() {
    let myDiv = document.getElementById("navBar");
    myDiv.setAttribute("id", "socialNetworkNavigation");
    let newli = document.createElement("li");
    newli.innerHTML = '<a href="#">Logout</a>';
    myDiv.firstElementChild.appendChild(newli);
}

function ex_2() {
    let myLi = document.querySelector("#container+ul :last-child");
    myLi.textContent = "Richard";
    let liToMyName = document.querySelectorAll(".list :first-child");
    liToMyName.forEach(li => li.textContent = "Gleb")

    let allElementsUL = document.querySelectorAll(".list");
    allElementsUL.forEach(ul => {
        let heyLi = document.createElement("li");
        heyLi.textContent = "Hey, students";
        ul.appendChild(heyLi);
        ul.classList.add("student_list");
    });
    allElementsUL[0].classList.add("university","attendance");
    // console.log(allElementsUL[1].querySelectorAll("li"));
    allElementsUL[1].querySelectorAll("li").forEach((li, index, arr) => 
        {if (li.textContent == "Sarah")
                 arr[index].remove(li);});
}


