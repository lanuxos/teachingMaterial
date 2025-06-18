// error handling
// RangeError
let arr = new Array(-1); // This will throw a RangeError

// ReferenceError
console.log(nonExistentVariable); // This will throw a ReferenceError

// SyntaxError
// let something = ;

// TypeError
let num = 42;
num.toUpperCase(); // This will throw a TypeError

// throw
throw "This is a custom error message.";
throw new Error("Throwing error by myself.");

// try-catch
function divide(a, b) {
    if (b === 0) {
        throw new Error("Division by zero is not allowed.");
    }
    return a / b;
}
try {
    console.log(divide(10, 2)); // 5
    console.log(divide(10, 0)); // This will throw an error
}
catch (error) {
    console.error("Error:", error.message);
}
// finally block [optional]
finally {
    console.log("Execution completed.");
}