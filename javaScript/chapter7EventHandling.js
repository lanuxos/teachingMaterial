// event handling

// show date
{/* <button onclick="showDate()">
      Show Date()
    </button>
    <p id="showDateParagraph"></p>
    <input type="text" name="" id="onFocusInput">
    <div id="mouseOver">Mouse Over<br>Here</div> */}


// onclick
showDateParagraph = document.getElementById('showDateParagraph')
function showDate() {
    const dateNow = new Date();
    showDateParagraph.innerHTML = dateNow.toLocaleString();
}
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
    if (event.key === 'Enter') {
        alert('You pressed Enter!');
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

// event object
// < button onclick = "showDate()" > Show Date()</ >
// <p id="showDateParagraph"></p>

// <form id="domForm">
//   <label for="firstName">First name</label>
//   <input type="text" name="firstName" id="firstName" />
//   <label for="lastName">Last name</label>
//   <input type="text" name="lastName" id="lastName" />
//   <button id="domFormSubmit">submit</button>
// </form>

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

// preventDefault
domForm = document.getElementById("domForm");
domForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    alert(`Hello ${firstName} ${lastName}`);
});

// event.target.value
document
    .getElementById("myInput")
    .addEventListener("input", function (event) {
        // console.log("TEXT: " + event.target.value);
        document.getElementById("myOutput").value = event.target.value;
        document.getElementById("myOutput2").innerText = event.target.value;
    });
// event.type
document
    .getElementById("eventTypeButton")
    .addEventListener("click", function (event) {
        document.getElementById("displayEventType").innerText = event.type;
    });
// event.key
document
    .getElementById("eventKeyCheck")
    .addEventListener("keydown", function (event) {
        document.getElementById("displayEventKey").innerText = event.key;
    });
// event.clientX
document.getElementById('clientXY').addEventListener('click', function (event) {
    document.getElementById('displayClientXY').innerText = '@' + event.timeStamp + 'millisecond on X: ' + event.clientX + '; Y: ' + event.clientY;
})
// event.altKey
document.getElementById('altKeyCheck').addEventListener('keydown', function (event) {
    if (event.altKey) {
        document.getElementById('altKeyCheck').style.backgroundColor = 'lightgreen';
    }
});
// showDate
showDateParagraph = document.getElementById("showDateParagraph");
function showDate() {
    const dateNow = new Date();
    showDateParagraph.innerHTML = dateNow.toLocaleString();
}