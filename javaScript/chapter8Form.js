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
<style>
      .error-message {
        color: red;
        font-size: 12px;
        margin-top: 5px;
      }

      input:invalid {
        border-color: red;
      }

      input:valid {
        border-color: green;
      }
    </style>
<form
      id="regForm"
      style="width: 240px; height: auto; border: 2px solid lightblue; border-radius: 10px; padding: 20px; background-color: aliceblue;"
    >
      <input type="radio" name="title" id="mr" required/>
      <label for="mr">mr</label>
      <input type="radio" name="title" id="ms" />
      <label for="ms">ms</label>
      <br />

      <label for="firstName">First Name</label><br />
      <input type="text" id="firstName" name="firstName" required /><br />

      <label for="lastName">Last Name</label><br />
      <input type="text" id="lastName" name="lastName" required /><br />

      <label for="email">Email</label><br />
      <input type="text" id="email" name="email" required /><br />

      <label for="password">Password</label><br />
      <input type="password" id="password" name="password" required /><br />

      <label for="rePassword">Re-password</label><br />
      <input type="password" id="rePassword" name="password" /><br />

      <label for="tel">Tel</label><br />
      <input type="text" id="tel" name="tel" /><br />

      <input type="checkbox" name="accept" id="accept" />
      <label for="accept">I accept all the terms of use and conditions.</label><br />

      <button type="submit" id="register">Register</button>
    </form>
*/
document.getElementById("regForm").addEventListener("submit", function (event) {
    let isValid = true;

    const errorMessages = document.querySelectorAll(".error-message");
    errorMessages.forEach((msg) => msg.remove());

    const title = document.querySelector('input[name="title"]:checked');
    if (!title) {
        isValid = false;
        showError("title", "Please select a title (Mr/Ms).");
    }

    const firstName = document.getElementById("firstName").value.trim();
    if (!firstName) {
        isValid = false;
        showError("firstName", "First name is required.");
    }

    const lastName = document.getElementById("lastName").value.trim();
    if (!lastName) {
        isValid = false;
        showError("lastName", "Last name is required.");
    }

    const email = document.getElementById("email").value.trim();
    const emailPattern = /^[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$/;
    if (!email || !emailPattern.test(email)) {
        isValid = false;
        showError("email", "Please enter a valid email.");
    }

    const password = document.getElementById("password").value;
    const passwordPattern = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;
    if (!password || !passwordPattern.test(password)) {
        isValid = false;
        showError("password", "Password must be at least 8 characters long and include uppercase, lowercase, and a number.");
    }

    const rePassword = document.getElementById("rePassword").value;
    if (rePassword !== password) {
        isValid = false;
        showError("rePassword", "Passwords do not match.");
    }

    const tel = document.getElementById("tel").value.trim();
    if (tel && !/^\d+$/.test(tel)) {
        isValid = false;
        showError("tel", "Phone number must be numbers only.");
    }

    const acceptTerms = document.getElementById("accept").checked;
    if (!acceptTerms) {
        isValid = false;
        showError("accept", "You must accept the terms and conditions.");
    }

    if (!isValid) {
        event.preventDefault();
    } else {
        alert("Your registration form is recorded.");
    }
});

function showError(inputId, message) {
    const inputField = document.getElementById(inputId);
    const errorMessage = document.createElement("div");
    errorMessage.classList.add("error-message");
    errorMessage.style.color = "red";
    errorMessage.innerText = message;
    inputField.insertAdjacentElement("afterend", errorMessage);
    inputField.style.borderColor = "red"; // Add red border for error
}

// Real-time password matching check
document.getElementById("rePassword").addEventListener("input", function () {
    const password = document.getElementById("password").value;
    const rePassword = this.value;

    // Check if passwords match and update UI
    if (rePassword !== password) {
        showError("rePassword", "Passwords do not match.");
        clearError("rePassword");
    } else {
        clearError("rePassword");
        document.getElementById("rePassword").style.borderColor = "green"; // Set green border for matching passwords
    }
});

function clearError(inputId) {
    const inputField = document.getElementById(inputId);
    const errorMessages = inputField.nextElementSibling;
    if (errorMessages && errorMessages.classList.contains("error-message")) {
        errorMessages.remove();
    }
    inputField.style.borderColor = "green"; // Set green border for valid input
}


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
