// let fonts = [];
let letterA = [0,0,1,1,1,0,0,
               0,1,0,0,0,1,0,
               0,1,0,0,0,1,0,
               0,1,0,0,0,1,0,
               0,1,1,1,1,1,0,
               0,1,0,0,0,1,0,
               0,1,0,0,0,1,0];

for (let i = 0; i < 49; i++){
   pixel = document.createElement("div"); 
   pixel.setAttribute("class","pixel");
   document.getElementById("letter").appendChild(pixel);
   if (letterA[i])
    pixel.innerHTML = "*";
}