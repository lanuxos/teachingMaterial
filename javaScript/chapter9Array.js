// chapter9Array.js

let mobile = ["Apple", "Oppo", "Huawei", "Samsung"];
let mobilePrice = [299, 79, 99, 179];
let googleService = [true, 1, false, "yes"];

console.log(mobile[3]);

mobile[4] = "Nokia";

console.log(mobile);

mobile.length

mobilePrice.push(149);

googleService.pop();

mobile.shift();

mobile.unshift("Blackberry");

mobile.splice(4, 0, "Sony"); // start deleteCount [insertData]

mobile.slice(0, 3); // start end[notInclude]

// loop
let chars = ["a", "b", "c", "d", "e"]
for (let i = 0; i < chars.length; i++) {
    console.log(chars[i]);
}

let nums = [1, 2, 3, 4, 5]
for (let num of nums) {
    console.log(num);
}

let arrVar = [1, "a", 2, "b", 3, "c"]
arrVar.forEach(function (item) {
    console.log(item);
});

/*
<ul id="list"></ul>
*/

let asean = [
    "Brunei",
    "Cambodia",
    "Indonesia",
    "Laos",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Vietnam",
];
let list = document.getElementById("list");
asean.forEach(function (country) {
    let li = document.createElement('li');
    li.textContent = country;
    list.appendChild(li);
});

for (let i = 0; i < asean.length; i++) {
    let li = document.createElement("li");
    li.textContent = asean[i];
    list.appendChild(li);
}

for (country of asean) {
    let li = document.createElement("li");
    li.textContent = country;
    list.appendChild(li);
}

