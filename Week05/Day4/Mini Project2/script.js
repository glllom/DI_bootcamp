function makeSound(event){
    const sound = event.currentTarget.id;
    console.log(`play ${sound}`);
    let audio = new Audio(`./assets/wav/${sound}.wav`)
    audio.play(); 
}