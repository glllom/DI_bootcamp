let form = document.forms[0];
form.addEventListener("submit", calculateVolume);


function calculateVolume(event){
    let rad = form.radius.value;
    let volume = 4/3*Math.PI*Math.pow(rad,3);
    console.log(`Radius = ${rad}, Volume = ${volume} `);
    form.volume.value = volume;
    event.preventDefault();

}