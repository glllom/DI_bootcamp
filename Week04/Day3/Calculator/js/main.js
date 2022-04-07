let firstVariable = null, secondVariable = null, operation = null;
let currentValue = "0";
let dot = false;

/*
 * Processes '0'-'9' press event
 */
function number(digit) {
    currentValue += digit;
    showOnScreen(Number(currentValue));
}

/*
 * Processes '.' press event
 */
function dotPressed() {
    if (!dot)
        currentValue += '.';
    showOnScreen(Number(currentValue) + '.');
}

/*
 * Processes 'clear' press event
 */
function clearScreen(){
    currentValue = '0';
    showOnScreen(Number(currentValue));
}

/*
 * Processes 'reset' press event
 */
function resetCalculator(){
    currentValue = '0';
    firstVariable = null, secondVariable = null, operation = null;
    showOnScreen(Number(currentValue));
    document.getElementById("string").textContent = '|';
}

/*
 * Processes '+','-','*','/' press event
 */
function operator(symbol) {
    if (currentValue != "")
        firstVariable = Number(currentValue);
    operation = symbol;
    document.getElementById("string").textContent = firstVariable + ' ' + operation;
    currentValue = "0";
}

function equal() {
secondVariable = Number(currentValue);
document.getElementById("string").textContent = document.getElementById("string").textContent + ' ' + secondVariable + ' =';
let result;
switch (operation) {
    case '+':
        result = Number(firstVariable + secondVariable);
        break;
    case '-':
        result = Number(firstVariable - secondVariable);
        break;
    case '*':
        result = Number(firstVariable * secondVariable);
        break;
    case '/':
        if (secondVariable != 0) { // When num2 is zero it just slide down to 'Illegal operation' message
            result = Number(firstVariable / secondVariable);
            break;
        }
    default:
        showOnScreen(`Error`);
    }
if (currentValue == ""){
        showOnScreen(`Error`);
        return;
}
showOnScreen(result);
firstVariable = result;
secondVariable = null, currentValue = "";
}

/*
 * Shows relevant info on main screen
 */
function showOnScreen(number) {
    document.getElementById("active-number").textContent = number;
}
