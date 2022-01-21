let bottles = Number(prompt("Give me the number of bottles."));
let bottlesSubstractor = 1;

function printPattern(numberOfBottles, substractor) {
    console.log(`${numberOfBottles} ${(numberOfBottles) == 1 ? 'bottle' : 'bottles'} of beer on the wall.`);
    console.log(`${numberOfBottles} ${(numberOfBottles) == 1 ? 'bottle' : 'bottles'} of beer.`);
    console.log(`Take ${Math.min(numberOfBottles,substractor)} down, pass ${(substractor == 1) || (numberOfBottles == 1) ? 'it' : 'them'} around`);
    console.log(`${numberOfBottles > substractor ? numberOfBottles - substractor : 0} ${(numberOfBottles - substractor) == 1 ? 'bottle' : 'bottles'} of beer on the wall.`);
    console.log("");
}

for (bottles; bottles > 0; bottles -= bottlesSubstractor++) {
    printPattern(bottles, bottlesSubstractor);

}

