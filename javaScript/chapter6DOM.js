// DOM

let helloDOM = document.getElementById("helloDOM")
helloDOM.innerHTML = "Hello, <b>JavaScript!</b>";

// task list
// html
{/* <input id="taskInput" placeholder="Add task" />
    <button id="addTask">Add</button>
    <ul id="taskList"></ul> */}
// js
document.getElementById("addTask").addEventListener("click", function () {
    const task = document.getElementById("taskInput").value;
    const li = document.createElement("li");
    li.textContent = task;
    li.addEventListener("click", () => li.remove()); // click to remove task
    document.getElementById("taskList").appendChild(li);
    document.getElementById("taskInput").value = "";
});

