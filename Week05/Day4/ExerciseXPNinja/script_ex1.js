function colorGenerator() {
    let rgbColor = [Math.floor(Math.random() * 256), Math.floor(Math.random() * 256), Math.floor(Math.random() * 256)];
    return rgbColor;
}

function prepareNewColor() {
    newColor = colorGenerator();
    creator.style.color = `rgb(${newColor[0]},${newColor[1]},${newColor[2]})`;
}

function createSquare() {
    newSquare.setAttribute("style", `width: 160px;
            height:160px;
            background-color: rgb(${newColor[0]},${newColor[1]},${newColor[2]});`)
    newSquare = document.createElement("div");
    newSquare.setAttribute("class", "square");
    document.getElementById("container").appendChild(newSquare);
    prepareNewColor();
    
}



let creator = document.getElementById("creator");
let newColor;
prepareNewColor();
let newSquare = document.createElement("div");
document.getElementById("container").appendChild(newSquare);
newSquare.setAttribute("class", "square");