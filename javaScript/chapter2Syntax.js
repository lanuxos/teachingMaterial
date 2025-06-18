// chapter 2 - syntax

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