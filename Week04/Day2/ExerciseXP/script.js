/*
 * Exercise 1 : Information
 */
function infoAboutMe(){
    console.log("Hi. My name is Gleb. I am 39 years old and my hobby is 3D printing.");
    console.log("More about me you can find in Wiki.");
}

infoAboutMe();

function infoAboutPerson(personName, personAge, personFavoriteColor){
    console.log(`Hi. My name is ${personName}. I am ${personAge} years old and my favorite color is ${personFavoriteColor}.`);
}
infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

/*
 * Exercise 2 : Tips
 */
function calculateTip(){
    amountOfBill = Number(prompt("What is amount of the bill?"));
    let tips;
    if (amountOfBill < 50)
        tips = amountOfBill*0.2;
    else if (amountOfBill > 200)
        tips = amountOfBill*0.1;
    else
        tips = amountOfBill*0.15;
    console.log(`Final bill is ${amountOfBill + tips}`);
}

calculateTip();

/*
 * Exercise 3 :Find The Numbers Divisible By 23
 */
function isDivisible(divisor, fromNumber=0, toNumber=500){
    let numbers = [], sum = 0;
    for (let i=fromNumber; i <= toNumber; i++){
        if(i % divisor == 0){
            numbers.push(i);
            sum += i;
        }
    }
    console.log(`Here are all the numbers from ${fromNumber} to ${toNumber} diviseble by ${divisor}: ${numbers}`);
    console.log(`Sum: ${sum}`);
}

isDivisible(Number(prompt('Insert a divisor, please. It must be more than zero')));

/*
 * Exercise 4 : Shopping List
 */

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ['banana', 'orange', 'apple'];

function myBill(){
    let total = 0;
    for(item of shoppingList){
        if (stock[item] > 0){
            total += prices[item];
            stock[item]--;
        }
    }
    return total;
}
console.log(myBill());

/*
 * Exercise 5 : What’s In My Wallet ?
 */

function changeEnough(itemPrice, amountOfChange){
    return (itemPrice <= (amountOfChange[0]*.25 + amountOfChange[1]*.1 + amountOfChange[2]*.05 + amountOfChange[3]*.01))
}

/*
 * Exercise 6 : Vacations Costs
 */
function hotelCost(){
    let nights;
    do
        nights = prompt("How many nights you would like to stay in the hotel?")
    while (!parseInt(nights));
    return 140 * nights;
 }

function planeRideCost(){
    let destination;
    do
        destination = prompt("What is your destination?")
    while (parseInt(destination) || destination.trim() == "");
    switch (destination){
        case 'London':
            return 183;
        case 'Paris':
            return 220;
        default:
            return 300;
    }
}

function rentalCarCost(){
    let days;
    do
        days = prompt("How many days you would like to rent the car.?")
    while (!parseInt(days));
    return 40 * days * (1 - 0.05*(days > 10)); // Fare with discount if rent is more than 10 days 
}

function totalVacationCost(){
    let tickets = planeRideCost();
    let hotelBill = hotelCost();
    let carRent = rentalCarCost();
    return `The car cost: $${carRent}, the hotel cost: $${hotelBill}, the plane tickets cost: $${tickets}.`
} 
console.log(totalVacationCost());
