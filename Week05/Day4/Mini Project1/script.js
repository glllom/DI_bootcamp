let resolution = 1800;
for (let counter = 0; counter < resolution; counter++) {
    let pixel = document.createElement("div");
    document.getElementById("main").appendChild(pixel);
}

let colors = document.querySelectorAll("#sidebar > *:not(button)");
for (c of colors) {
    c.addEventListener("click", pickColor)
}
let pickedColor = "white";
let brushReady = false;

function pickColor() {
    colors.forEach(c => { c.setAttribute("class", "") });
    this.setAttribute("class", "activated");
    pickedColor = this.style.backgroundColor;
    console.log(pickedColor);
}

let pixels = document.querySelectorAll("#main > *")
for (p of pixels) {
    p.addEventListener("mouseup", endPaint);
    p.addEventListener("mousedown", startPaint);
    p.addEventListener("mouseover", paint);
}

function paint() {
    if (brushReady)
        this.style.backgroundColor = pickedColor;
}

function startPaint() {
brushReady = true;
this.style.backgroundColor = pickedColor;
}

function endPaint() {
    brushReady = false;
}

document.getElementsByTagName("button")[0]
    .addEventListener("click", function () {
        for (p of pixels) p.style.backgroundColor = "white";
    });
