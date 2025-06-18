// chapter 5 - functions

function sayHello(name) {
    console.log(`Hello, ${name}`)
};
sayHello('JavaScript');

addNumber(5, 10);
function addNumber(a, b) {
    return a + b;
};

// conditional base function
let conditionalFunction;
let gender = 'female';
if (gender == 'female') {
    conditionalFunction = function () {
        console.log('Female toilet open.');
    };
} else {
    conditionalFunction = function () {
        console.log('Male toilet open.');
    };
};

// function expression
subtract(10, 5);
let subtract = function (a, b) {
    return a - b;
};

// recursive function
let factorial = function fac(n) {
    return n < 2 ? 1 : n * fac(n - 1);
};
factorial(3);

// factorial function
function factorial(n) {
    if (n === 1) return 1;       
    return n * factorial(n - 1); 
}
console.log(factorial(5)); 

// IIFE (Immediately Invoked Function Expression)
(function () {
    console.log('This is an IIFE.');
})();

// IIFE with arrow function
(() => {
    console.log("Hello IIFE with arrow function!");
})();

// global scope
let globalVariable = 'I am a global variable';
// function scope
function functionScopeExample() {
    let functionVariable = 'I am a function variable';
    console.log(functionVariable);
}
functionScopeExample();
// block scope
{
    let blockVariable = 'I am a block variable';
    console.log(blockVariable);
}

// closure example
function outerFunction() {
    let outerVariable = 'I am an outer variable';
    return function innerFunction() {
        console.log(outerVariable);
    };
}
let inner = outerFunction();
inner(); // Outputs: I am an outer variable

// closure encapsulation
function createBankAccount(initialBalance) {
    let balance = initialBalance;

    return {
        deposit(amount) {
            balance += amount;
        },
        withdraw(amount) {
            if (amount <= balance) {
                balance -= amount;
            } else {
                console.log("Insufficient balance.");
            }
        },
        getBalance() {
            return balance;
        }
    };
}

const account = createBankAccount(1000);
account.deposit(500);
console.log(account.getBalance()); // 1500

// argument object
function concatenation(separator) {
    let result = ""; // initialize list
    // iterate through arguments
    for (let i = 1; i < arguments.length; i++) {
        result += arguments[i] + separator;
    }
    return result;
}
console.log(concatenation(", ", "Red", "Green", "Blue")); // Outputs: Red, Green, Blue
console.log(concatenation(" - ", "Apple", "Banana", "Cherry")); // Outputs: Apple - Banana - Cherry  

function multiArg(args) {
    for (let i = 0; i < args.length; i++) {
        console.log(args[i]);
    }
}
multiArg(["Hello", "World", "JavaScript"]); 
multiArg(["One", 2, "Three"]); 

// function parameters
// default parameters
function multiply(a, b) {
    b = typeof b !== "undefined" ? b : 1;
    // w/o above, b would be undefined and return NaN
    return a * b;
}
console.log(multiply(5)); // 5
function multiplyWithDefault(a, b = 1) {
    return a * b;
}
console.log(multiplyWithDefault(5)); // 5

// rest parameters
function sum(...numbers) {
    let result = 0;
    for (let number of numbers) {
        result += number;
    }
    return result;
}
console.log(sum(1, 2, 3)); // 6

// arrow functions / fat arrow
const add = (a, b) => a + b;
console.log(add(5, 10)); // 15
const square = x => x * x;
console.log(square(4)); // 16
const greet = () => console.log("Hello, JavaScript!");
greet(); // Hello, JavaScript!

// arrow function have no this prop, return undefined
// regular function has this prop
const person = {
    name: "Alice",
    greet: function() {
        console.log(`Hello, ${this.name}`);
    }
};
person.greet();
// arrow function does not bind this, so it will be undefined
const personArrow = {
    name: "Bob",
    greet: () => {
        console.log(`Hello, ${this.name}`); 
    }
};
personArrow.greet(); // Hello, undefined
