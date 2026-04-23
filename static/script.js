var socket = io();

function sendMsg() {
    let username = document.getElementById("username").value;
    let msg = document.getElementById("msg").value;

    socket.send({
        username: username,
        message: msg
    });

    document.getElementById("msg").value = "";
}

socket.on("message", function(msg) {
    let li = document.createElement("li");

    let parts = msg.split(": ");
    let user = parts[0];
    let text = parts.slice(1).join(": ");

    li.innerHTML = `<span class="username">${user}</span>: ${text}`;

    document.getElementById("chat").appendChild(li);

    // auto scroll
    let chat = document.getElementById("chat");
    chat.scrollTop = chat.scrollHeight;
});

document.getElementById("msg").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMsg();
    }
});