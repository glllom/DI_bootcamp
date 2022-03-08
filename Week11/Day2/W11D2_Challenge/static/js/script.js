if (window.location.href == "http://127.0.0.1:5000/lesson") {
    document.querySelectorAll(".item")[0].classList.add("active")
    document.querySelector(".container").style.visibility = "visible"
    document.querySelector(".container").innerHTML = document.querySelector(".container").innerText;
}
else if (window.location.href == "http://127.0.0.1:5000/exercises"){
    document.querySelectorAll(".item")[1].classList.add("active")
    document.querySelector(".container").style.visibility = "visible"
    document.querySelector(".container").innerHTML = document.querySelector(".container").innerText;
}


let nav_items = document.querySelectorAll(".item");
for (let item of nav_items) {
    item.addEventListener("click", activate);
}

function activate(e) {
    for (let item of nav_items) {
        item.classList.remove('active');
    }
    e.target.classList.add('active');
}
