let labels = document.querySelectorAll(".search-type-tab");


function activate(elem) {
    if (elem == labels[0]) {
        labels[0].classList.add('active');
        labels[1].classList.remove('active');
        document.getElementById("phone_number").disabled = true;
        document.getElementById("name").disabled = false;
        document.getElementById("phone_number").value = "";

    } else {
        labels[1].classList.add('active');
        labels[0].classList.remove('active');
        document.getElementById("name").disabled = true;
        document.getElementById("phone_number").disabled = false;
        document.getElementById("name").value = "";
    }
}