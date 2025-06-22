// form

// domForm
/*
<form id="domForm">
      <label for="username">Username</label>
      <input type="text" name="username" id="username" />
      <br />
      <label for="password">Password</label>
      <input type="password" name="password" id="password" />
      <br />
      <input type="radio" name="role" id="member" />
      <label for="member">Member</label>
      <input type="radio" name="role" id="admin" />
      <label for="admin">Admin</label>
      <br />
      <input type="checkbox" name="showHide" id="show" />
      <label for="show">Show</label>
      <input type="checkbox" name="showHide" id="hide" />
      <label for="hide">Hide</label>
      <br />
      <button type="submit" id="login">Login</button>
    </form>
*/

const domForm = document.getElementById("domForm");
const username = document.getElementById("username");
const password = document.getElementById("password");
const member = document.getElementById("member");
const admin = document.getElementById("admin");
const show = document.getElementById("show");
const hide = document.getElementById("hide");
const loginButton = document.getElementById("login");

domForm.addEventListener("submit", function (event) {
    // loginButton.addEventListener("click", function (event) {
    event.preventDefault();
    if (member.checked) {
        alert(username.value);
    } else if (admin.checked) {
        if (show.checked) {
            // if (show.checked && !hide.checked) {
            alert(username.value + " " + password.value);
        } else {
            alert(username.value + " ********");
        }
    }
});

// form event
/*
<form id="eventForm">
  <label for="email">Email</label>
  <br>
  <input type="email" id="email">
  <br>
  <label for="password1">Password</label>
  <br>
  <input type="password" name="password" id="password1">
  <br>
  <label for="password2">Re-password</label>
  <br>
  <input type="password" name="password" id="password2">
  <br>
  <button type="submit" id="signUp">Sign Up</button>
  <p id="status"></p>
</form>
*/
const eventForm = document.getElementById("eventForm");
const email = document.getElementById("email");
const [pass1, pass2] = document.getElementsByName("password");
const msg = document.getElementById("status");
eventForm.addEventListener("input", function () {
    msg.innerText = "user is typing...";
    if (pass1.value != "" && pass1.value === pass2.value) {
        pass1.style.backgroundColor = "lightgreen";
        pass2.style.backgroundColor = "lightgreen";
    }
});
pass2.addEventListener("blur", function () {
    msg.innerText = "";
    pass1.style.backgroundColor = "";
    pass2.style.backgroundColor = "";
});
eventForm.addEventListener("submit", function (event) {
    event.preventDefault();

    if (email.value != "" && pass1.value === pass2.value) {
        alert("sign up successfully");
    } else {
        alert(
            `check your info, email:[${email.value}] pass1:[${pass1.value}] pass2:[${pass2.value}]`
        );
    }
});

// fix eventForm bug with
// add required attribute to input tag


// regForm
/*
<form
      id="regForm"
      style="
        width: 240px;
        height: auto;
        border: 2px solid lightblue;
        border-radius: 10px;
        padding: 20px;
        background-color: aliceblue;
      "
    >
      <input type="radio" name="title" id="mr" />
      <label for="mr">mr</label>
      <input type="radio" name="title" id="ms" />
      <label for="ms">ms</label>
      <br />
      <label for="firstName">First Name</label>
      <br />
      <input type="text" id="firstName" name="firstName" required />
      <br />
      <label for="lastName">Last Name</label>
      <br />
      <input type="text" id="lastName" name="lastName" required />
      <br />
      <label for="email">Email</label>
      <br />
      <input
        type="text"
        id="email"
        name="email"
        pattern="[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$"
        required
      />
      <br />
      <label for="password">Password</label>
      <br />
      <input
        type="password"
        id="password"
        name="password"
        pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
        required
      />
      <br />
      <label for="rePassword">Re-password</label>
      <br />
      <input type="password" id="rePassword" name="password" />
      <br />
      <label for="tel">Tel</label>
      <br />
      <input type="text" id="tel" name="tel" />
      <br />
      <input type="checkbox" name="accept" id="accept" required />
      <label for="accept">I accept all the term of use and conditions.</label>
      <br />
      <button type="submit" id="register">Register</button>
    </form>
*/

// input blur removeEventListener
// <input type="email" name="email" id="email" />

const emailInput = document.getElementById("email");
// input event
emailInput.addEventListener("input", function (e) {
    console.log("Typing:", e.target.value);
});
// blur
emailInput.addEventListener("blur", function () {
    alert("You left the input box!");
});

// removeEventListener
// remove after clicked three times
/*
<button id="myButton">Click Me</button>
<p id="message"></p>
*/
const button = document.getElementById("myButton");
const message = document.getElementById("message");

let clickCount = 0;
function handleClick() {
    clickCount++;
    message.innerText = `You have clicked the button ${clickCount} times.`;
    if (clickCount === 3) {
        button.removeEventListener("click", handleClick);
        message.innerText =
            "You clicked the button 3 times. Event listener removed!";
    }
}
button.addEventListener("click", handleClick);

// getElementsByName
{
    /* <input type="password" name="password" />
<input type="password" name="password" />

<button onclick="checkPasswords()">Check</button> */
}

function checkPasswords() {
    const [pass1, pass2] = document.getElementsByName("password");
    if (pass1.value === pass2.value) {
        pass1.style.backgroundColor = "lightgreen";
        pass2.style.backgroundColor = "lightgreen";
    } else {
        pass1.style.backgroundColor = "lightyellow";
        pass2.style.backgroundColor = "lightyellow";
    }
}
