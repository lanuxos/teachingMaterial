/* 
# mdn web docs - javascript guide

## introduction
- grammar and types
- control flow and error handling
- loops and iteration
- functions
- expression and operators
- numbers and strings
- representing dates and times
- regular expressions
- indexed collections
- keyed collections
- working with objects
- using class
- using promises
- javascript typed arrays
- iterator and generators
- internationalization
- javascript modules

## intermediate
- advanced javascript objects
- asynchronous javascript
- client side web apis
- language overview
- javascript data structures
- equality comparisons and sameness
- enumerability and ownership of properties
- closures

## advanced
- inheritance and the prototype chain
- meta programming
- memory management
*/

var caseSensitive;
var CaseSensitive;

// one-line comment

/* 
multi-line
comment
*/

// escape characters
var singleQuote = 'This is a single quote: \'';
var doubleQuote = "This is a double quote: \"";

console.log("Hello, JavaScript!");

// scope
{
    var withOutInitial;
    // console.log(withOutInitial); // undefined
    let initialLater; initialLater = "Initialized later";
    // console.log(initialLater); // "Initialized later"
    var globalVariable = "I am global";
    let blockVariable = "I am block scoped";
    const constantVariable = "I am a constant";
    constantVariable = "I can not be changed"; // This will throw an error
    // console.log(constantVariable);
    // mutation of constant variable
    const theObject = { name: "John" };
    theObject.name = "Doe"; // This is allowed without error
    console.log(theObject.name); // "Doe"
    // array can be change even if it is a constant
    const theArray = [1, 2, 3];
    theArray.push(4); // This is allowed without error
    console.log(theArray); // [1, 2, 3, 4]
}

console.log(globalVariable); // "I am global"
// console.log(blockVariable); // ReferenceError: blockVariable is not defined
// console.log(constantVariable); // ReferenceError: constantVariable is not defined

// data types
let stringVariable = "This is a string"; // String
let numberVariable = 42; // Number
let booleanVariable = true; // Boolean
let bigIntVariable = BigInt(1234567890123456789012345678901234567890); // BigInt
let bigIntVariableN = 1234567890123456789012345678901234567890n; 
let nullVariable = null; // Null
let undefinedVariable; // Undefined
let objectVariable = { key: "value" }; // Object
let arrayVariable = [1, 2, 3]; // Array[Object]
// console.log(...)

// type conversion - typeof
let numString = "123";
let convertedNumber = Number(numString);

numString = 123;

operatorNumber = numString + "";

operatorNumber = numString * 1; // - * /

let anotherString = "456.789";
intNumber = parseInt(anotherString); 
floatNumber = parseFloat(anotherString); 
number_ = Number(anotherString);
string_ = String(intNumber);
boolean_ = Boolean(1);

unaryNumber = +anotherString;

// operators
// assignment operators
// destructuring assignment
let array1 = [1, 2, 3];
let [a, b, c] = array1; // a = 1, b = 2, c = 3

// arithmetic operators
let arith1 = 1;
let prefixArith = ++arith1;
console.log(arith1); 
console.log(prefixArith);

let prefixInit = 0;
while (++prefixInit < 5) {
    console.log("Prefix Init:", prefixInit);
}

let arith2 = 1;
let postfixArith = arith2++;
console.log(arith2);
console.log(postfixArith);

for (let postFixInit = 0; postFixInit < 5; postFixInit++){
    console.log("Postfix Init:", postFixInit);
}

// prompt - return string
let userInput = prompt("Please enter your name:");
console.log(userInput);

// random number 0-1
let randomNumberTo9 = Math.floor(Math.random() * 10); // 1-9
console.log("Random number between 1 and 9:", randomNumberTo9);
let randomNumberTo10 = Math.floor(Math.random() * 11); // 1-10
console.log("Random number between 1 and 10:", randomNumberTo10);
let randomNumberTo99 = Math.floor(Math.random() * 100); // 1-99
console.log("Random number between 1 and 99:", randomNumberTo99);
let randomNumberTo100 = Math.floor(Math.random() * 100) + 1; // 1-100
console.log("Random number between 1 and 100:", randomNumberTo100);

// getElementById
document.getElementById("lucky").innerText = randomNumberTo99;

// control flow - condition
// if - else if - else
let score = prompt("Enter your score:");
if (score >= 90) {
    console.log("You got an A!");
    document.getElementById('score').innerHTML = '<h1>You got an A!</h1>';
}
else if (score >= 80) {
    console.log("You got a B!");
    document.getElementById('score').innerHTML = '<h1>You got an B!</h1>';
}
else if (score >= 70) {
    console.log("You got a C!");
    document.getElementById('score').innerHTML = '<h1>You got an C!</h1>';
}
else if (score >= 60) {
    console.log("You got a D!");
    document.getElementById('score').innerHTML = '<h1>You got an D!</h1>';
}
else {
    console.log("You got an F!");
    document.getElementById('score').innerHTML = '<h1>You got an F!</h1>';
}

// iteration - for loop
console.log("For loop example 1:");
let numbers = [1, 2, 3, 4, 5];
for (let i = 0; i < numbers.length; i++) {
    console.log("Number:", numbers[i]);
}

console.log("For loop example 2:");
for (let counter = 0; counter < 5; counter++) {
    console.log("Counter is:", counter);
}

console.log("For loop example 3:");
let amount = prompt("Enter an amount:");
let net = 0;
for (let i = 0; i < amount; i++) {
    price = prompt("Enter a price:");
    net = net + parseFloat(price);
    // net += price;
}
console.log("Current net amount:", net);

console.log("For loop example 4:");
let times = prompt("How many times do you want to repeat?");
for (let i = 0; i < times; i++) {
    let option = prompt("Enter an option (h for Heads/t forTails):");
    let result = '';
    if(Math.floor(Math.random() * 2) === 0) {
        console.log("Heads");
        result = 'h';
    } else {
        console.log("Tails");
        result = 't';
    }
    if (option === result) {
        console.log("You guessed it right!");
    } else {
        console.log("You guessed it wrong!");
    }
}

// iteration - while loop
console.log("While loop example 1:");
let count = 0;
while (count < 5) {
    console.log("Count is:", count);
    count++;
}

// function
function sayHello(name) {
    console.log(`Hello, ${name}!`);
}
sayHello("JavaScript Developer");

// return function
function addNumbers(a, b) {
    return a + b;
}
let sum = addNumbers(5, 10);
console.log("Sum of 5 and 10 is:", sum);

// function with parameters
function greetUser(name, age) {
    return `Hello, ${name}! You are ${age} years old.`;
}
greet = greetUser("Alice", 30); // arguments
alert(greet);

// nested function
function outerFunction(a, b) {
    function innerFunction(x) {
        return x * x;
    }
    return innerFunction(a) + innerFunction(b);
}
console.log(outterFunction(2, 3)); // 13
