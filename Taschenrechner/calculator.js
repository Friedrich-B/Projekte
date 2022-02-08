var display;
var ZAHL = "";
var result;

function load() {
    //don't know why this code has to be in load();
    display = document.getElementById("DISPLAY");
    display.innerHTML = ZAHL;
}

function C() {
    //clears the display
    ZAHL = "";
    display.innerHTML = ZAHL;
}

function number(num) {
    //adds a new number to the equation
    ZAHL += num;
    display.innerHTML = ZAHL;
}
function PLUS() {
    //adds the + operator to the equation
    display.innerHTML += " + ";
    ZAHL = display.innerHTML;
}
function MINUS() {
    //adds the - operator to the equation
    display.innerHTML += " - ";
    ZAHL = display.innerHTML;
}
function MAL() {
    //adds the * operator to the equation
    display.innerHTML += " * ";
    ZAHL = display.innerHTML;
}
function GETEILT() {
    //adds the / operator to the equation
    display.innerHTML += " / ";
    ZAHL = display.innerHTML;
}
function DOT() {
    //adds a dot to the equation
    ZAHL += ".";
    display.innerHTML = ZAHL;
}
function Left() {
    //adds a brace (left part only)
    ZAHL += "( ";
    display.innerHTML = ZAHL;
}
function Right() {
    //adds a brace (right part only)
    ZAHL += " )";
    display.innerHTML = ZAHL;
}
function DELETE() {
    //deletes the last char of the equation
    ZAHL = ZAHL.slice(0, -1);
    display.innerHTML = ZAHL;
}
function ENTER() {
    //solves the equation
    result = ZAHL;
    result = eval(result).toFixed(6);
    ZAHL = "";
    //fills in the solution or replaces Nan and Infinity
    if ((Math.sign(result) != 1 && Math.sign(result) != -1 && Math.sign(result) != 0) || result == Infinity) {
        display.innerHTML = "Dividieren durch 0 nicht möglich!";
    } else {
        display.innerHTML = result;
    }
}
