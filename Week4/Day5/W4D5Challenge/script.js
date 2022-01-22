let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
let colors = ["darkred", "BlueViolet", "DodgerBlue", "red", "MediumSlateBlue", "tan", "LightSteelBlue", "MidnightBlue"];
planets.forEach((planetName, index) => {
    let planet = document.createElement("div")
    planet.setAttribute("class", "planet");
    planet.setAttribute("style", `background: ${colors[index]};`);
    document.querySelector("section").appendChild(planet);
});

