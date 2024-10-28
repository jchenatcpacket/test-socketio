const { io } = require("socket.io-client");

// const socket = io("http://server:8000")
const socket = io("http://sanic:8003")

socket.on("connect", () => {
    console.log(socket.id);
});

socket.on("disconnect", () => {
    console.log(socket.id);
});


socket.on('my event', (data) => {
    console.log('Received message:', data);
});

socket.io.on("error", (error) => {
    console.log(error)
});

socket.on("connect_error", (error) => {
    if (socket.active) {
        console.log("active connection");
    } else {
      console.log(error.message);
    }
});