// chapter 4 - control flow

// control flow - condition
// if - else if - else
let init = 7;
if (init > 10) {
    console.log("init value > 10");
} else if (10 > init && init > 0) {
    console.log("init value is 0-10");
} else {
    console.log("init value < 0");
}

let init_ = 7;
if (init_ > 10) {
    console.log("init_ value > 10");
} else if (10 > init_) {
    if (init_ > 0) {
        console.log("init_ value is 0-10");
    } else {
        console.log("init_ value < 0");
    }
}

let finalScore = 85;

if (finalScore >= 90) {
    console.log("A");
} else if (finalScore >= 80) {
    console.log("B");
} else {
    console.log("C");
}

// switch-case
let subject = "IT";
switch (subject) {
    case "IT":
        console.log("Good at computer");
        break;
    case "Finance":
        console.log("Good at Accountant");
        break;
    case "Mechanic":
        console.log("Good at fixing things");
        break;
    default:
        console.log("Good at sleeping!!!");
}

let score = prompt("Enter your score:");
if (score >= 90) {
    console.log("You got an A!");
    document.getElementById("score").innerHTML = "<h1>You got an A!</h1>";
} else if (score >= 80) {
    console.log("You got a B!");
    document.getElementById("score").innerHTML = "<h1>You got an B!</h1>";
} else if (score >= 70) {
    console.log("You got a C!");
    document.getElementById("score").innerHTML = "<h1>You got an C!</h1>";
} else if (score >= 60) {
    console.log("You got a D!");
    document.getElementById("score").innerHTML = "<h1>You got an D!</h1>";
} else {
    console.log("You got an F!");
    document.getElementById("score").innerHTML = "<h1>You got an F!</h1>";
}

// iteration - for loop
console.log("For loop example 1:");
for (let counter = 1; counter < 5; counter++) {
    console.log("Counter is:", counter);
}

console.log("For loop example 2:");
let numbers = [1, 2, 3, 4, 5];
for (let i = 0; i < numbers.length; i++) {
    console.log("Number:", numbers[i]);
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
    let result = "";
    if (Math.floor(Math.random() * 2) === 0) {
        console.log("Heads");
        result = "h";
    } else {
        console.log("Tails");
        result = "t";
    }
    if (option === result) {
        console.log("You guessed it right!");
    } else {
        console.log("You guessed it wrong!");
    }
}

// for loop
console.log("For loop example 1:");
for (let counter = 1; counter < 5; counter++) {
    console.log("Counter is:", counter);
}

// for...in loop
let forPerson = {
    name: "John",
    age: 30,
    city: "New York"
};
for (let key in forPerson) {
    console.log(key + ": " + forPerson[key]);
}

// for...of loop
for (let i of "JavaScript") {
    console.log(i);
}

// iteration - while loop
console.log("While loop example 1:");
let count = 0;
while (count < 5) {
    console.log("Count is:", count);
    count++;
}

// do-while loop
console.log("Do-while loop example 1:");
let doCount = 0;
do {
    console.log("Do Count is:", doCount);
    doCount++;
}
while (doCount < 5);

// labelled statement
console.log("Labelled statement example:");
outerLoop: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (i === 1 && j === 1) {
            console.log("Breaking out of outer loop");
            break outerLoop; // Breaks out of the outer loop
        }
        console.log(`i: ${i}, j: ${j}`);
    }
}
// break statement
console.log("Break statement example:");
for (let i = 0; i < 5; i++) {
    if (i === 3) {
        console.log("Breaking the loop at i =", i);
        break; // Exits the loop when i equals 3
    }
    console.log("Current value of i:", i);
}
// continue statement
console.log("Continue statement example:");
for (let i = 0; i < 5; i++) {
    if (i === 2) {
        console.log("Skipping iteration for i =", i);
        continue; // Skips the rest of the loop body for this iteration
    }
    console.log("Current value of i:", i);
}