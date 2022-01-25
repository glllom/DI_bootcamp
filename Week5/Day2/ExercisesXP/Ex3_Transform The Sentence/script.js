let allBoldItems=[];
getBold_items();

function getBold_items(){
    allBoldItems = document.querySelectorAll("strong");
}

function highlight(){
    for (item of allBoldItems){
        item.setAttribute("style", "color: blue;");
    }
}

function return_normal(){
    for (item of allBoldItems){
        item.setAttribute("style", "color: black;");
    }
}
document.getElementsByTagName("p")[0].addEventListener("mouseover",highlight);
document.getElementsByTagName("p")[0].addEventListener("mouseout",return_normal);
