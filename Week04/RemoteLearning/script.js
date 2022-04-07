function remove(){
    let elem = document.getElementsByTagName("li")
    // console.log(typeof(elem))
    for (item of elem){
        item.removeAttribute("style")
        }
    
    elem.forEach(element => console.log(element));
}