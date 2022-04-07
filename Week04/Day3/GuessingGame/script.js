/*
 *  Main function
 */ 
function playTheGame(){
    if (confirm("Would you like to play the game?")){
        let computerNumber = Math.floor(Math.random() * 11); 
        for (let chances = 3; chances > 0; chances--){
            let userNumber = getNumber();
            if (test(userNumber, computerNumber, chances))
                break;
        }      
    }
    else
        alert("No problem, Goodbye");
}

/*
 *  Copmares two numbers
 */ 
function test(userNumber,computerNumber, chances){
    if (userNumber > computerNumber)
        alert("Your number is bigger then the computer's" + (chances > 1 ? ", guess again":". Out of chances"));
    else if (userNumber < computerNumber)
        alert("Your number is smaller then the computer's" + (chances > 1 ? ", guess again":". Out of chances"));
    else{
        alert("WINNER");
        return true;
        }
    return false;
}

/*
 *  Gets a number from user
 */ 
function getNumber(){
    let number = prompt("Enter a number between 0 and 10");
    if (!parseInt(number)){
        alert("Sorry Not a number");
        return getNumber();
    }
    else if (number < 0 || number > 10){
        alert("Sorry it's not a good number");
        return getNumber();
    }
    return number;
}
