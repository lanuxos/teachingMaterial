// event handling

// inline style
{/* <button onclick="alert('JavaScript')">
    Alert("JavaScript")
</button> */}

// splitted javascript style
// show date
{/* <button onclick="showDate()">
      Show Date()
    </button> */}
// onclick
showDateParagraph = document.getElementById('showDateParagraph')
function showDate() {
    const dateNow = new Date();
    showDateParagraph.innerHTML = dateNow.toLocaleString();
}

// getElementsByName
{/* <input type="password" name="password" />
    <input type="password" name="password" />

    <button onclick="checkPasswords()">Check</button> */}

function checkPasswords() {
    const [pass1, pass2] = document.getElementsByName("password");
    if (pass1.value === pass2.value) {
        pass1.style.backgroundColor = 'lightgreen';
        pass2.style.backgroundColor = 'lightgreen';
    } else {
        pass1.style.backgroundColor = 'lightyellow';
        pass2.style.backgroundColor = 'lightyellow';
    }
}

// event object
// < button onclick = "showDate()" > Show Date()</ >
// <p id="showDateParagraph"></p>

// <label for="myInput">Input</label>
// <input type="text" id="myInput" name="myInput" />
// <label for="myOutput">Output</label>
// <input id="myOutput" name="myOutput" />
// <p id="myOutput2"></p>

// <button id="eventTypeButton">clickEventTypeButton</button>
// <p id="displayEventType"></p>

// <label for="eventKeyCheck">event.key</label>
// <input type="text" id="eventKeyCheck" name="eventKeyCheck" />
// <p id="displayEventKey"></p>

// <div id="clientXY">
//   this<br>
//   is<br>
//   div<br>
//   tag<br>
//   area
// </div>
// <p id="displayClientXY"></p>

// <label for="altKeyCheck">alt key check</label>
// <input type="text" name="altKeyCheck" id="altKeyCheck">

// <form id="domForm">
//   <label for="firstName">First name</label>
//   <input type="text" name="firstName" id="firstName" />
//   <label for="lastName">Last name</label>
//   <input type="text" name="lastName" id="lastName" />
//   <button id="domFormSubmit">submit</button>
// </form>

// event.type
document
    .getElementById("eventTypeButton")
    .addEventListener("click", function (event) {
        document.getElementById("displayEventType").innerText = event.type;
    });
// event.target.value
document
    .getElementById("myInput")
    .addEventListener("input", function (event) {
        // console.log("TEXT: " + event.target.value);
        document.getElementById("myOutput").value = event.target.value;
        document.getElementById("myOutput2").innerText = event.target.value;
    });
// event.key
document
    .getElementById("eventKeyCheck")
    .addEventListener("keydown", function (event) {
        document.getElementById("displayEventKey").innerText = event.key;
    });
// event.clientX/Y
document.getElementById('clientXY').addEventListener('click', function (event) {
    document.getElementById('displayClientXY').innerText = '@' + event.timeStamp + 'millisecond on X: ' + event.clientX + '; Y: ' + event.clientY;
})
// event.altKey
document.getElementById('altKeyCheck').addEventListener('keydown', function (event) {
    if (event.altKey) {
        document.getElementById('altKeyCheck').style.backgroundColor = 'lightgreen';
    }
});

// preventDefault
domForm = document.getElementById("domForm");
domForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    alert(`Hello ${firstName} ${lastName}`);
});

// showDate
showDateParagraph = document.getElementById("showDateParagraph");
function showDate() {
    const dateNow = new Date();
    showDateParagraph.innerHTML = dateNow.toLocaleString();
}

// even handling example
{/* <p id="showDateParagraph"></p>
    <input type="text" name="" id="onFocusInput">
    <div id="mouseOver">Mouse Over<br>Here</div> */}

// onfocus
onFocusInput = document.getElementById('onFocusInput');
onFocusInput.onfocus = function () {
    onFocusInput.style.backgroundColor = 'lightblue';
}
// onblur
onFocusInput.onblur = function () {
    onFocusInput.style.backgroundColor = '';
}
// onchange by hitting enter
onFocusInput.onchange = function () {
    onFocusInput.style.backgroundColor = 'lightgreen';
}
// onkeydown
onFocusInput.onkeydown = function (event) {
    if (event.key === 'Escape') {
        alert('You pressed Escape!');
    }
}
// onmouseover/onmouseout
mouseOver = document.getElementById('mouseOver');
mouseOver.onmouseover = function () {
    mouseOver.style.backgroundColor = 'yellow';
}
mouseOver.onmouseout = function () {
    mouseOver.style.backgroundColor = '';
}
					
// add/remove event listener
/*
<div
      id="eventBox"
      style="
        width: 200px;
        height: 200px;
        background-color: lightblue;
        margin: 10px;
        padding: 10px;
      "
    >
      <p>Interact with this box</p>
      <button id="removeListenersBtn">Remove Event Listeners</button>
    </div>
    <div id="output" style="margin: 20px"></div>
*/

// Get DOM elements
const eventBox = document.getElementById("eventBox");
const output = document.getElementById("output");

// Event handler functions
// click				
function handleClick() {
    // output.innerHTML += "<p>Single click detected</p>";
    output.innerHTML = "<p>Single click detected</p>";
}
// dbclick
function handleDoubleClick() {
    // output.innerHTML += "<p>Double click detected</p>";
    output.innerHTML = "<p>Double click detected</p>";
}
// mouseenter == mouseover
function handleMouseEnter() {
    eventBox.style.backgroundColor = "lightgreen";
    // output.innerHTML += "<p>Mouse entered</p>";
    output.innerHTML = "<p>Mouse entered</p>";
}
// mouseleave == mouseout
function handleMouseLeave() {
    eventBox.style.backgroundColor = "lightblue";
    // output.innerHTML += "<p>Mouse left</p>";
    output.innerHTML = "<p>Mouse left</p>";
}

// Add event listeners
eventBox.addEventListener("click", handleClick);
eventBox.addEventListener("dblclick", handleDoubleClick);
eventBox.addEventListener("mouseenter", handleMouseEnter);
eventBox.addEventListener("mouseleave", handleMouseLeave);

// Function to remove all event listeners
function removeEventListeners() {
    eventBox.removeEventListener("click", handleClick);
    eventBox.removeEventListener("dblclick", handleDoubleClick);
    eventBox.removeEventListener("mouseenter", handleMouseEnter);
    eventBox.removeEventListener("mouseleave", handleMouseLeave);
    output.innerHTML += "<p>All event listeners removed</p>";
}

const removeBtn = document.getElementById("removeListenersBtn");
removeBtn.addEventListener("click", removeEventListeners);

